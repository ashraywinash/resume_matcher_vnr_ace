import json
from llm.gemini_client import call_gemini 
from schema import ResumeAnalysis

SYSTEM_PROMPT = """
You are an expert resume reviewer, recruiter, and ATS optimization specialist.
You are critical, specific, and practical.
"""

def analyze_resume(
        resume_text: str,
        target_role: str = "General",
        experience_level: str = "Unknown"
    ) -> ResumeAnalysis:

    user_prompt = f"""
    Analyze the resume below.

    Target Role: {target_role}
    Experience Level: {experience_level}

    Return STRICT JSON matching this schema:

    {{
    "overall_score": number (0-100),
    "summary": [string],
    "section_feedback": {{
        "experience": {{
        "issues": [string],
        "suggestions": [string],
        "example_rewrites": [string]
        }}
    }},
    "ats_issues": [string],
    "priority_fixes": [string]
    }}

    Be specific. Provide concrete rewrite examples.

    Resume:
    \"\"\"
    {resume_text}
    \"\"\"
    """

    response = call_gemini([
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ])

    response = response.replace("```json", " ").strip()
    response = response.replace("```", " ").strip()

    parsed = json.loads(response)
    return ResumeAnalysis(**parsed)
