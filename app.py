from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained AI model
model_data = joblib.load("student_model.pkl")

model = model_data["model"]
mae = model_data["mae"]
rf_mae = model_data["rf_mae"]

coefficients = dict(zip(
    model.feature_names_in_,
    model.coef_
))

@app.route("/", methods=["GET", "POST"])
def home():
   
    prediction = None
    performance = None
    recommendation = None

    study_hours = None
    attendance = None
    previous_marks = None
    assignments = None
    internal_marks = None

    if request.method == "POST":

        study_hours = float(request.form["study_hours"])
        if study_hours < 0 or study_hours> 16:                       #studyhr validation
            return "study hours must be between 1 and 16"

        attendance = float(request.form["attendance"])
        if attendance < 0 or attendance > 100:
            return " Attendance must be between 0 and 100"
        
        previous_marks = float(request.form["previous_marks"])
        if previous_marks < 0 or previous_marks > 100:
            return " Previous marks must be between 0 and 100"
        
        assignments = float(request.form["assignments"])
        if assignments < 0 or assignments > 10:
            return " Assigments must be between 0 and 10"
        
        internal_marks = float(request.form["internal_marks"])
        if internal_marks < 0 or internal_marks > 20:
            return " Internal marks must be between 0 and 20"

        # Create input with the same feature names used during training
        student = pd.DataFrame([{
            "study_hours": study_hours,
            "attendance": attendance,
            "previous_marks": previous_marks,
            "assignments": assignments,
            "internal_marks": internal_marks
        }])

        prediction = round(model.predict(student)[0], 1)

        if prediction >= 80:
            performance = "Excellent"
            recommendation = " keep maintaining your current routine."
        elif prediction >= 60:
            performance = "Good"
            recommendation = " Good progress. Focus on consistency and revision."
        elif prediction >= 40:
            performance = "Average"
            recommendation = "Increase study time and improve attendance and internal marks. "
        else:
            performance =" Need improvement"
            recommendation ="Focus on regular study, attendance, assignments and revision. "
        

    return render_template (
        "index.html",
        prediction=prediction,        # send to html
        performance=performance,
        recommendation=recommendation,
        study_hours=study_hours,
        attendance=attendance,
        previous_marks=previous_marks,
        assignments=assignments,
        internal_marks=internal_marks,
        mae=mae,
        rf_mae=rf_mae,
        coefficients=coefficients
    )


if __name__ == "__main__":
    app.run(debug=True)