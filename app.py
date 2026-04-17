from flask import Flask, request, jsonify
from flask_cors import CORS
import PyPDF2

app = Flask(__name__)
CORS(app)  # allow frontend to connect

# Function to extract text from PDF
def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text.lower()

@app.route('/')
def home():
    return "✅ Resume Analyzer Backend Running"

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['resume']
    text = extract_text(file)

    # Skill list (you can expand later)
    skills_db = ["python", "java", "react", "sql", "html", "css"]

    found_skills = [skill for skill in skills_db if skill in text]

    score = int((len(found_skills) / len(skills_db)) * 100)

    missing_skills = list(set(skills_db) - set(found_skills))

    return jsonify({
        "score": score,
        "skills_found": found_skills,
        "missing_skills": missing_skills,
        "suggestion": "Try adding more relevant technical skills to improve ATS score"
    })

if __name__ == "__main__":
    app.run(debug=True)
