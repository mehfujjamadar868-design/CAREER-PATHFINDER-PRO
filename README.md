# Career Pathfinder Pro

Career Pathfinder Pro is a machine-learning based career recommendation application that helps users explore suitable career paths based on their academic performance, technical skills, interests, and other profile inputs.

The project was built to explore how machine learning can be used to turn user-provided information into a practical career recommendation and learning roadmap.

## Live Demo

[Try Career Pathfinder Pro](https://career-pathfinder-pro-3hezlf2usqtnqbheavsaux.streamlit.app/)

## What It Does

The application collects information about a user's profile and uses a trained machine learning model to predict a suitable career category.

Based on the prediction, the application provides a corresponding roadmap covering areas that the user can work on to develop the skills relevant to that career path.

### Current Career Categories

- AI / Machine Learning
- Web Development
- Data Science
- Cybersecurity
- Cloud Computing

## How It Works

The application follows a simple machine-learning workflow:

1. The user enters information about their academic background, skills, interests, and other profile attributes.
2. The inputs are organized into a structured dataset using Pandas.
3. The saved scaler is used to transform the input features.
4. The transformed data is passed to the trained machine-learning model.
5. The model predicts a suitable career category.
6. The application displays a learning roadmap related to the predicted career.

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
