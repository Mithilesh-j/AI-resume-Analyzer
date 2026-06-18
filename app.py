from flask import Flask, render_template, request
from pdf_extractor import extract_text
from gemini_service import analyze_resume
import os

app = Flask(__name__)
os.makedirs("uploads", exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    resume = request.files["resume"]
    file_path = os.path.join("uploads", resume.filename)
    resume.save(file_path)

    resume_text = extract_text(file_path)
    job_description = request.form["job_description"]

    analysis = analyze_resume(resume_text, job_description)

    score = int(analysis.get("match_score", 0))

    return render_template(
        "result.html",
        score=score,
        matching=analysis.get("matching_skills", []),
        missing=analysis.get("missing_skills", []),
        strengths=analysis.get("strengths", []),
        weaknesses=analysis.get("weaknesses", []),
        suggestions=analysis.get("suggestions", []),
        analysis_text=analysis.get("detailed_analysis", "")
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)