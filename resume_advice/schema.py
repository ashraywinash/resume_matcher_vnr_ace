from pydantic import BaseModel
from typing import List, Dict

class SectionFeedback(BaseModel):
    issues: List[str]
    suggestions: List[str]
    example_rewrites: List[str]

class ResumeAnalysis(BaseModel):
    overall_score: int
    summary: List[str]
    section_feedback: Dict[str, SectionFeedback]
    ats_issues: List[str]
    priority_fixes: List[str]
