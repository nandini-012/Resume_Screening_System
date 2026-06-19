from fastapi import FastAPI
from app.models import JobDescriptionRequest
from app.extractor import extract_skills
from app.ats_analyser import analyze_resume
from app.resume_processor import resume_data

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Resume Screening API Running"
    }
    
@app.post("/analyze")
def analyze(job_description_request: JobDescriptionRequest):

    jd_skills = extract_skills(
        job_description_request.job_description
    )

    report = analyze_resume(
        resume_data,
        jd_skills
    )

    return report