🤖 AI Resume Analyzer

AI Resume Analyzer is a Flask-based web application that uses Google Gemini AI to analyze a resume against a job description and generates an ATS-style report including match score, skills gap, strengths, weaknesses, and improvement suggestions.

---

## 🚀 Features

- 📊 ATS Match Score (0–100)
- 🟢 Matching Skills Extraction
- 🔴 Missing Skills Detection
- ⭐ Strengths Analysis
- ⚠️ Weaknesses Identification
- 💡 Smart Suggestions for Improvement
- 🧠 AI-powered Detailed Resume Analysis
- 📄 PDF Resume Upload Support
- ⚡ Fast and simple web interface

---

## 🛠️ Tech Stack

- Python 🐍
- Flask 🌐
- HTML5, CSS3 🎨
- JavaScript ⚡
- Google Gemini AI 🤖
- PyPDF2 📄
- dotenv 🔐

---

## 📁 Project Structure


AI_resume_analyzerfolder/
│── app.py
│── gemini_service.py
│── pdf_extractor.py
│
├── templates/
│ ├── index.html
│ └── result.html
│
├── static/
│ └── style.css
│
├── uploads/
├── venv/
└── .env


---

## ⚙️ How It Works

1. User uploads a resume (PDF file)
2. User pastes job description
3. Flask extracts text from PDF
4. Gemini AI compares resume with job description
5. AI returns structured ATS-style analysis
6. Results are displayed in a clean UI

---

## 📊 Output Example

- **ATS Score:** 72/100  
- **Matching Skills:** Python, SQL, Power BI  
- **Missing Skills:** Advanced SQL, Pandas, NumPy  
- **Strengths:** Strong project experience, certifications  
- **Weaknesses:** Lack of deep data analysis exposure  
- **Suggestions:** Improve SQL, build data projects  


