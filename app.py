from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

from utils.pdf_parser import extract_text_from_pdf
from utils.skills_extractor import extract_skills, extract_domain_skills
from utils.matcher import match_resume

app = Flask(__name__)
CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True
)


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "AI Resume Scanner Backend Running"

# serve uploaded pdf
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route("/upload", methods=["POST"])
def upload_resume():
    files = request.files.getlist("resumes")
    job_description = request.form["job_description"]
    jd_skills = extract_domain_skills(job_description)

    results = []

    for file in files:
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        resume_text = extract_text_from_pdf(path)
        resume_skills = extract_skills(resume_text)
        missing_skills = list(set(jd_skills) - set(resume_skills))
        score = match_resume(resume_skills, jd_skills)
        results.append({
            "name": file.filename,
            "score": score,
            "skills_found": resume_skills,
            "missing_skills": missing_skills,
            "pdf_url": f"https://resume-backend-iota-green.vercel.app/uploads/{file.filename}"
        })
    results = sorted(results, key=lambda x: x["score"], reverse=True)
    return jsonify(results)

if __name__ == "__main__":
    app.run()
