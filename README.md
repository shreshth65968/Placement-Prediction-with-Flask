
## Placement Prediction Web App

## Project Overview

This project is a web application designed to predict student placement outcomes using a machine learning model. The application is built using Flask for the backend and HTML/CSS for the frontend. A Random Forest classifier is utilized to make predictions based on student data.

## Features

- User-friendly web interface for inputting student data.
- Backend server built with Flask to handle requests and predictions.
- Random Forest classifier model to predict placement outcomes.
- Responsive design using HTML and CSS.

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

- Flask
- numpy
- joblib
- Pandas
- matplotlib
- scikit-learn==1.2.2
- gunicorn
- seaborn

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shreshth65968/Placement-Prediction-with-Flask.git
    cd Placement-Prediction-with-Flask

    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    python app.py
    ```

    The web app should now be running on `http://127.0.0.1:5000/`.

## Usage

1. **Home Page:**

    Enter the required student information into the form provided on the home page.

2. **Submit:**

    Click the "Predict placement" button to make a prediction. The result will display whether the student is likely to be placed or not.

## Project Structure

- **app.py**: The main Flask application file.
- **model.py**: Script to train and save the Random Forest model.
- **templates/**: Directory containing HTML templates.
    - **index.html**: The main page where users input data.
    
- **static/**: Directory containing static files like CSS.
    - **mystyle.css**: The CSS file for styling the web pages.
- **requirements.txt**: List of required Python packages.

## Model Training

The model is trained using a dataset of student information from kaggle. The features used for training include academic scores, extracurricular activities, and other relevant data points. The Random Forest classifier is chosen for its robustness and accuracy in handling classification problems.



working link:-  https://drive.google.com/file/d/1Kvc3oQQE1YNPPATWCaJRiGdDkUKpZdjF/view?usp=sharing


- installation
  
![install](https://github.com/shreshth65968/Placement-Prediction-with-Flask/assets/96594936/43d17245-89ca-488a-9a39-88e9fd41e52c)

- deploying

![deploy](https://github.com/shreshth65968/Placement-Prediction-with-Flask/assets/96594936/036adb57-57d1-4563-acb2-c055626974f3)

- Output 1

![view](https://github.com/shreshth65968/Placement-Prediction-with-Flask/assets/96594936/56fd9bc9-7bff-49b7-a221-a455a51a49f8)

- Output 2

![view 2](https://github.com/shreshth65968/Placement-Prediction-with-Flask/assets/96594936/3b297c5a-5b92-4013-92f9-bae136000706)

- Factors

![factors](https://github.com/shreshth65968/Placement-Prediction-with-Flask/assets/96594936/c73f43b9-e2ee-4e1e-915d-bfce20dfce27)

- prediction

![prediction](https://github.com/shreshth65968/Placement-Prediction-with-Flask/assets/96594936/0f740447-a0c3-4e9a-adef-9ad1efd810ff)




 


  
