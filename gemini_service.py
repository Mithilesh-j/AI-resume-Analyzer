import os
import json
import re
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)


def extract_json(text):
    """
    Extract JSON even if Gemini adds extra text or ```json blocks
    """
    try:
        # Remove ```json ... ```
        cleaned = re.sub(r"```json|```", "", text).strip()

        # Extract JSON part only
        start = cleaned.find("{")
        end = cleaned.rfind("}") + 1
        json_str = cleaned[start:end]

        return json.loads(json_str)

    except Exception as e:
        return {
            "match_score": 0,
            "matching_skills": [],
            "missing_skills": [],
            "strengths": [],
            "weaknesses": [],
            "suggestions": [],
            "detailed_analysis": f"JSON Parse Error: {str(e)}"
        }


def analyze_resume(resume_text, job_description=""):

    prompt = f"""
You are an expert AI Resume Analyzer.

Return ONLY valid JSON in this EXACT format:

{{
  "match_score": 0,
  "matching_skills": [],
  "missing_skills": [],
  "strengths": [],
  "weaknesses": [],
  "suggestions": [],
  "detailed_analysis": ""
}}

Rules:
- No markdown
- No explanations
- Only JSON

Resume:
{resume_text}

Job Description:
{job_description}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return extract_json(response.text)

    except Exception as e:
        return {
            "match_score": 0,
            "matching_skills": [],
            "missing_skills": [],
            "strengths": [],
            "weaknesses": [],
            "suggestions": [],
            "detailed_analysis": f"API Error: {str(e)}"
        }