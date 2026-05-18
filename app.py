import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.skills_extractor import extract_domain_skills, extract_skills
from utils.pdf_parser import extract_text_from_pdf
from utils.matcher import match_resume

app = Flask(__name__)
CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True
)

@app.route("/")
def home():
    return jsonify({"status": "healthy", "message": "AI Resume Scanner Backend Running Successfully"})

@app.route("/upload", methods=["POST"])
def upload_resume():
    if 'resumes' not in request.files:
        return jsonify({"error": "No resume files uploaded"}), 400
        
    files = request.files.getlist("resumes")
    job_description = request.form.get("job_description", "")
    
    jd_skills = extract_domain_skills(job_description)
    results = []
    
    for file in files:
        if file.filename == '':
            continue
            
        try:
            # Pass the file stream directly to the parser (No disk saving!)
            resume_text = extract_text_from_pdf(file)
            
            resume_skills = extract_skills(resume_text)
            missing_skills = list(set(jd_skills) - set(resume_skills))
            score = match_resume(resume_skills, jd_skills)
            
            results.append({
                "name": file.filename,
                "score": score,
                "skills_found": resume_skills,
                "missing_skills": missing_skills,
                "pdf_url": "In-memory processing active"
            })
        except Exception as e:
            results.append({
                "name": file.filename,
                "error": f"Failed to process file: {str(e)}"
            })
            
    results = sorted(results, key=lambda x: x.get("score", 0), reverse=True)
    return jsonify(results)

# Required for local testing, Vercel uses WSGI
if __name__ == "__main__":
    app.run(debug=True)
