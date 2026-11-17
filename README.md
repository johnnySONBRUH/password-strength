# Diabetes Predictor

A user-friendly web application for assessing diabetes risk based on patient health metrics. It leverages a trained Random Forest model to provide quick predictions, helping users understand their potential health indicators.

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Model](https://img.shields.io/badge/model-RandomForest-orange.svg)

## Features

- **Modern UI**: Clean, organized, and professional interface powered by Streamlit.
- **Intuitive Layout**: Input fields are grouped logically into "Demographic Info" and "Health Indicators" for a better user experience.
- **Clear Results**: Provides easy-to-understand prediction outcomes.
- **Automated Wake-up**: Includes a script to wake up the hosted application if it goes to sleep due to inactivity.

## Model Performance

| Metric | Score |
| :--- | :--- |
| Accuracy | 0.97215 |
| F1 Score | 0.8051766351871283 |
| Recall Score | 0.6738875878220141 |
| Balanced Accuracy | 0.836943793911007 |
| Precision | 1.0 |


## Project Structure

- `streamlit_app.py`: The Streamlit frontend application and prediction logic.
- `main.py`: The training script that trains the Random Forest model and saves it.
- `predictor.pkl`: The serialized pre-trained machine learning model.
- `wake_app.py`: A utility script using Selenium to wake up the hosted Streamlit app if it is sleeping.
- `requirements.txt`: Project dependencies.

## Prerequisites

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/)

## Installation

1. Clone the repository (or download the files).
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Launch the Web App
You can access the live application here: [Diabetes Predictor](https://sbskkz5w96tlxlsmvkcha7.streamlit.app/)

Alternatively, run it locally:
```bash
streamlit run streamlit_app.py
```

### Wake up the Hosted App (Optional)
If you are using the hosted version and it needs to be "woken up":
```bash
python wake_app.py
```

### Train/Retrain the Model (Optional)
If you have new data and want to retrain the model:
```bash
python main.py
```
*Note: Ensure your training data is available (the script may need adjustment depending on your data file).*

## Data Source
The dataset used in this project is sourced from Kaggle:
[Diabetes Prediction Dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset)

