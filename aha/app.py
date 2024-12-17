from flask import Flask, render_template, request
import joblib  # To load the saved model
import pandas as pd

app = Flask(__name__)

# Load the trained model (adjust the path if necessary)
model = joblib.load('training_files/house_price_model.pkl')

# Home route to render the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the question page to enter house details
@app.route('/question')
def question():
    return render_template('question.html')

# Route to handle form submission and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract data from the form (get input from user)
            bedrooms = int(request.form['bedrooms'])
            bathrooms = float(request.form['bathrooms'])
            sqft_living = int(request.form['sqft_living'])
            sqft_lot = int(request.form['sqft_lot'])
            floors = int(request.form['floors'])

        except ValueError:
            # Return error message if invalid input
            return render_template('result.html', price="Invalid input data. Please enter correct values.")

        # Prepare the data for prediction (model input format)
        input_data = [[bedrooms, bathrooms, sqft_living, sqft_lot, floors]]

        # Predict the price using the trained model
        predicted_price = model.predict(input_data)

        # Round the price to two decimal places
        predicted_price = round(predicted_price[0], 2)

        # Pass the result to the result page
        return render_template('result.html', price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)






