# Password Strength AI

A web-based tool for assessing the strength of passwords. It uses a trained Random Forest model to analyze password features and categorize them as " Weak\ or \Strong,\ helping users improve their security.

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Model](https://img.shields.io/badge/model-RandomForest-orange.svg)

## Features

- **Modern UI**: Clean and intuitive interface powered by Streamlit.
- **Instant Analysis**: Quick assessment of password strength based on character composition and length.
- **Secure Input**: Uses masked input for password fields.

## Project Structure

- streamlit_app.py: The Streamlit frontend application and prediction logic.
- main.py: The training script that trains the Random Forest model and saves it.
- predictor.pkl: The serialized pre-trained machine learning model.
- parseInput.py: Helper script to extract features from passwords.
- data.csv: The dataset used to train the model.
- 
equirements.txt: Project dependencies.

## Prerequisites

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/)

## Installation

1. Clone the repository.
2. Install the required dependencies:
 `bash
 pip install -r requirements.txt
 `

## Usage

### Launch the Web App
Run the application locally:
`bash
streamlit run streamlit_app.py
`

### Train/Retrain the Model (Optional)
If you have new data and want to retrain the model:
`bash
python main.py
`
