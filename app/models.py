from pydantic import BaseModel


class JobDescriptionRequest(BaseModel):

    job_description: str
    
class ATSResponse(BaseModel):

    candidate: str

    overall_score: float

    matched_skills: list

    missing_skills: list

    strengths: list

    recommendations: list