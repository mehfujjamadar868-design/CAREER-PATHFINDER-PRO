import pandas as pd
import streamlit as st
import pickle

# Page configuration for a wide, professional look
st.set_page_config(page_title="Career Pathfinder Pro", layout="wide", initial_sidebar_state="expanded")

# Advanced CSS for Digital/Cyber UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');

    .main {
        background: radial-gradient(circle at top right, #1a1a2e, #0f0f1a);
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: transparent;
    }

    /* Glassmorphism Card Style */
    .css-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    .stButton>button {
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 700;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        width: 100%;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 242, 254, 0.4);
    }

    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif !important;
        color: #00f2fe !important;
    }

    .roadmap-step {
        border-left: 3px solid #00f2fe;
        padding-left: 15px;
        margin: 10px 0;
        background: rgba(0, 242, 254, 0.05);
        border-radius: 0 10px 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Load Machine Learning Assets
try:
    with open('career_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
except Exception as e:
    st.error("Required AI model files not found. Please ensure the training cells were executed.")

# Header Section
st.markdown("<h1> CAREER PATHFINDER <span style='color:white'>PRO</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size:1.2rem; opacity:0.8;'>AI-Powered Professional Trajectory Analysis</p>", unsafe_allow_html=True)
st.divider()

# Input Form in Sidebar
with st.sidebar:
    st.markdown("### PROFILE PARAMETERS")
    cgpa = st.slider("Academic CGPA", 0.0, 10.0, 8.0, 0.1)
    python_skill = st.select_slider("Python Proficiency", options=list(range(1,11)), value=5)
    communication = st.select_slider("Communication", options=list(range(1,11)), value=5)
    aptitude = st.select_slider("Logical Aptitude", options=list(range(1,11)), value=5)

    with st.expander("Technical Interests"):
        web_interest = st.slider("Web Dev", 1, 10, 5)
        ai_interest = st.slider("AI/ML", 1, 10, 5)
        networking_skill = st.slider("Networking", 1, 10, 5)
        debugging_skill = st.slider("Debugging", 1, 10, 5)

    creativity = st.slider("Creativity Score", 1, 10, 5)
    projects = st.number_input("Projects Done", 0, 50, 2)
    certifications = st.number_input("Certifications", 0, 20, 1)

# Main Dashboard
col_info, col_res = st.columns([1, 1])

with col_info:
    st.markdown("""
    <div class='css-card'>
        <h3>System Status</h3>
        <p> AI Model Loaded <br> Scaler Active <br> Ready for Input Analysis</p>
    </div>
    """, unsafe_allow_html=True)

    predict_btn = st.button("EXECUTE PREDICTION")

if predict_btn:
    # Prepare Data
    features = [cgpa, python_skill, communication, aptitude, web_interest, ai_interest,
                creativity, debugging_skill, networking_skill, projects, certifications]
    df_input = pd.DataFrame([features], columns=["cgpa", "python_skill", "communication", "aptitude",
                                               "web_interest", "ai_interest", "creativity",
                                               "debugging_skill", "networking_skill", "projects", "certifications"])

    # Prediction Engine
    scaled_input = scaler.transform(df_input)
    prediction = model.predict(scaled_input)[0]

    with col_res:
        st.markdown(f"""
        <div class='css-card' style='border: 2px solid #00f2fe;'>
            <p style='margin:0; text-transform:uppercase; letter-spacing:2px;'>Match Identified</p>
            <h2 style='margin:0;'>{prediction}</h2>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("###  STRATEGIC ROADMAP")

    # Mapping Roadmap Data
    roadmaps = {
        "AI/ML": ["Math Foundations (Linear Algebra)", "Advanced Python & Scikit-Learn", "Deep Learning Specialization", "Open Source AI Contribution"],
        "Web Development": ["HTML/CSS/JS Core", "React/Next.js Frameworks", "Backend (Node/Python)", "Cloud Architecture & CI/CD"],
        "Data Science": ["Statistical Analysis", "SQL & Big Data Tools", "Data Storytelling & Visualization", "Automated ML Pipelines"],
        "Cybersecurity": ["Network Security Protocols", "Ethical Hacking Labs", "Security Compliance (ISO/SOC2)", "Incident Response Training"],
        "Cloud Computing": ["AWS/Azure Fundamentals", "Containerization (Docker)", "Kubernetes Management", "Infrastructure as Code (Terraform)"]
    }

    steps = roadmaps.get(prediction, ["Core Skills Audit", "Portfolio Development", "Certification Sprint", "Networking & Referrals"])

    # Visual Roadmap Display
    roadmap_cols = st.columns(len(steps))
    for idx, step in enumerate(steps):
        with roadmap_cols[idx]:
            st.markdown(f"<div class='css-card' style='height:180px; text-align:center;'><h4 style='color:#00f2fe;'>STEP {idx+1}</h4><p>{step}</p></div>", unsafe_allow_html=True)

    st.balloons()
