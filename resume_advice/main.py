from resume.extractor import extract_text
from resume.normaliser import normalize_resume
from resume.analyser import analyze_resume

def run(resume_path: str):
    raw_text = extract_text(resume_path)
    clean_text = normalize_resume(raw_text)

    analysis = analyze_resume(
        resume_text=clean_text,
        target_role="Backend Engineer", # Example target role
        experience_level="Mid-Senior" # Example experience level
    )

    print("\n=== OVERALL SCORE ===")
    print(analysis.overall_score)

    print("\n=== SUMMARY ===")
    for s in analysis.summary:
        print("-", s)

    print("\n=== PRIORITY FIXES ===")
    for p in analysis.priority_fixes:
        print("-", p)

if __name__ == "__main__":
    run("resumes/22071A05B4.pdf")
