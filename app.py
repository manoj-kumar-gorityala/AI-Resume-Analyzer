from flask import Flask, render_template, request
import pickle
import PyPDF2
import re
from utils.ats_score import ats_score
from utils.skill_gap import skill_gap
from utils.job_recommender import recommend_jobs

app = Flask(__name__)

# Load ML model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Skill database
skills_db = [
    "python","machine learning","deep learning","tensorflow",
    "pytorch","java","html","css","javascript","react",
    "sql","docker","kubernetes","aws"
]

# -----------------------------
# Extract text from PDF
# -----------------------------
def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    return text


# -----------------------------
# Clean text
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    return text


# -----------------------------
# Extract skills
# -----------------------------
def extract_skills(resume):
    found_skills = []

    for skill in skills_db:
        if skill in resume:
            found_skills.append(skill)

    return found_skills


# -----------------------------
# Predict job role
# -----------------------------
def predict_role(resume):
    vector = vectorizer.transform([resume])
    prediction = model.predict(vector)
    return prediction[0]


# -----------------------------
# Resume scoring
# -----------------------------
def resume_score(skills):
    score = len(skills) * 10
    if score > 100:
        score = 100
    return score


# -----------------------------
# Resume suggestions
# -----------------------------
def suggestions(resume):
    tips = []

    if "github" not in resume:
        tips.append("Add GitHub profile")

    if "project" not in resume:
        tips.append("Add Projects section")

    if "certification" not in resume:
        tips.append("Add Certifications")

    if "internship" not in resume:
        tips.append("Add Internship experience")

    return tips


# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["resume"]

    text = extract_text(file)
    text = clean_text(text)

    skills = extract_skills(text)
    role = predict_role(text)
    score = resume_score(skills)

    # Advanced features
    ats = ats_score(text)
    missing_skills = skill_gap(skills)
    jobs = recommend_jobs(role)

    tips = suggestions(text)

    return render_template(
        "result.html",
        role=role,
        skills=skills,
        score=score,
        ats=ats,
        missing=missing_skills,
        jobs=jobs,
        tips=tips
    )


if __name__ == "__main__":
    app.run(debug=True)