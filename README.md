# Flower Classification Web Application

This is a simple web application that predicts the species of a flower based on its sepal and petal dimensions. It utilizes a machine learning model trained on the Iris dataset.

## Project Structure

- `CropClassProject/`
  - `app.py`: Flask web application that handles requests and serves the prediction page.
  - `model.py`: Python script for training the machine learning model and saving it as a pickle file.
  - `model.pkl`: Pickle file containing the trained machine learning model.
  - `Templates/`
    - `index.html`: HTML template for the prediction page.
  - `Iris.csv`: Dataset containing sepal and petal dimensions of Iris flowers.

## Setup Instructions

1. Clone this repository to your local machine.
2. Navigate to the `CropClassProject` directory.
3. Install the required Python packages by running `pip install -r requirements.txt`.
4. Run the Flask application by executing `python app.py` in the terminal.
5. Open a web browser and go to `http://localhost:5000` to access the application.

## Usage

1. Enter the sepal and petal dimensions of a flower into the input fields on the homepage.
2. Click on the "Predict" button to get the predicted species of the flower.
3. The predicted species will be displayed on the same page.

## Dependencies

- Flask
- NumPy
- pandas
- scikit-learn

## Credits

This project is created by AbayoBrian.

