# Career Pathfinder Pro

Career Pathfinder Pro is a machine-learning based career recommendation application that helps users explore suitable career paths based on their academic performance, technical skills, interests, and other profile inputs.

The project was built to explore how machine learning can be used to turn user-provided information into a practical career recommendation and learning roadmap.

## Live Demo

[Try Career Pathfinder Pro](https://career-pathfinder-pro-3hezlf2usqtnqbheavsaux.streamlit.app/)

## What It Does
The application collects information about a user's academic profile, technical abilities, interests, and other development-related attributes.

A trained machine-learning model processes these inputs and generates a career-path prediction.

After the prediction, the application provides a strategic learning roadmap. Dedicated roadmap guidance is currently available for several career paths, while other predictions receive a general career-development roadmap.


## How It Works

The application follows a simple machine-learning workflow:

1. The user enters information about their academic background, skills, interests, and other profile attributes.
2. The inputs are organized into a structured dataset using Pandas.
3. The saved scaler is used to transform the input features.
4. The transformed data is passed to the trained machine-learning model.
5. The model predicts a suitable career category.
6. The application displays a learning roadmap related to the predicted career.
### Machine Learning Pipeline

```text
User Profile
     ↓
Feature Preparation
     ↓
Pandas DataFrame
     ↓
Feature Scaling
     ↓
Trained ML Model
     ↓
Career Prediction
     ↓
Learning Roadmap
```
## Input Areas

The application currently considers profile information such as:

- CGPA
- Python proficiency
- Communication skills
- Aptitude
- Interests
- Creativity
- Debugging skills
- Networking knowledge
- Projects
- Certifications
- Other profile-related inputs

## Technologies Used

- **Python** — Application development and machine-learning workflow
- **Streamlit** — Interactive web application
- **Pandas** — Data handling and preparation
- **Scikit-learn** — Machine-learning workflow
- **Pickle** — Loading the trained model and scaler

## Project Structure

```text
CAREER-PATHFINDER-PRO/
│
├── app.py
├── career_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md 
```
