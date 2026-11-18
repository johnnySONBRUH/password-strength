# Password Strength AI

A comprehensive, web-based solution for evaluating password complexity and strength. By leveraging machine learning, specifically a Random Forest classifier, this tool provides instant feedback on password security. It analyzes various character composition features to classify passwords as "Weak" or "Strong," enabling users to adopt better security practices.

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Model](https://img.shields.io/badge/model-RandomForest-orange.svg)

## How it Works

The application follows a structured pipeline:
1.  **Feature Extraction**: The input password is processed via `parseInput.py`, which identifies critical features such as length, character types (uppercase, lowercase, numbers, special characters), and complexity patterns.
2.  **Prediction**: The extracted features are fed into a pre-trained `Random Forest` model (`predictor.pkl`).
3.  **Analysis**: The model classifies the password, and the results are presented to the user through a user-friendly `Streamlit` interface.

## Features

- **Modern UI**: Clean and intuitive interface powered by Streamlit.
- **Instant Analysis**: Quick assessment of password strength based on character composition and length.
- **Secure Input**: Uses masked input for password fields.

## Model Performance

The Random Forest model has been evaluated on the dataset and achieved the following performance metrics:

| Metric | Score |
| :--- | :--- |
| Accuracy Score | 0.99950000 |
| Recall Score | 0.99922299 |
| F1 Score | 0.99947233 |
| Balanced Accuracy Score | 0.99922299 |
| Precision Score | 0.99972268 |

## Project Structure

- streamlit_app.py: The Streamlit frontend application and prediction logic.
- main.py: The training script that trains the Random Forest model and saves it.
- predictor.pkl: The serialized pre-trained machine learning model.
- parseInput.py: Helper script to extract features from passwords.
- data.csv: The dataset used to train the model.
- requirements.txt: Project dependencies.

## Prerequisites

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/)

## Installation

1. Clone the repository.
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Launch the Web App
Run the application locally:
```bash
streamlit run streamlit_app.py
```

### Train/Retrain the Model (Optional)
If you have new data and want to retrain the model:
```bash
python main.py
```

## Contributing

Contributions are welcome! If you have suggestions to improve the model, UI, or overall functionality, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.


## Data Source

The dataset used for training this model was sourced from [Kaggle](https://www.kaggle.com/datasets/jeffersonvalandro/password-dataset/data).
