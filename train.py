import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 1. Load dataset
data = pd.read_csv("data.csv")

# 2. Separate inputs and output
X = data[
    ["study_hours", "attendance", "previous_marks",
     "assignments", "internal_marks"]
]

y = data["final_marks"]

# 3. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create linear regression model - It tries to find a mathematical equation that best fits the training data.
model = LinearRegression()

# 5. Train the model
model.fit(X_train, y_train)   


# 6. Test the model
predictions = model.predict(X_test)


# 7. Check error
error = mean_absolute_error(y_test, predictions)


# create another random forest model - it learns though many different trees
rf_model = RandomForestRegressor(
    n_estimators =100,                       #create 100 descision tree
    random_state=42
)
rf_model.fit(X_train,y_train)   #train the model in input & output data
rf_predictions = rf_model.predict(X_test)  # X_test contains input data that the model did not see during training.
rf_error = mean_absolute_error(y_test, rf_predictions)  # y_test = actual marks, predictions = predicted marks

print("AI Model trained successfully!")
print("Linear Regression MAE:", error)
print("Random Forest MAE:", rf_error)



# Save the  trained model
joblib.dump(
    {
        "model": model,
        "mae": error,
        "rf_mae": rf_error
    },
    "student_model.pkl"
)

print("Model saved successfully!")