from fastapi import (FastAPI,UploadFile, File,Form)
import tempfile
from app.models import JobDescriptionRequest
from app.extractor import extract_skills
from app.ats_analyser import analyze_resume
from app.resume_service import (build_resume_data)
app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Resume Screening API Running"
    }
    
@app.post("/full-analysis")
async def full_analysis(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:

        temp_file.write(
            await file.read()
        )

        resume_data = build_resume_data(
            temp_file.name
        )
        
        
        print("Candidate Name:", resume_data["name"])
        
        print("JOB DESCRIPTION:")
        print(job_description)

        jd_skills = extract_skills(job_description)
        
        print("=" * 50)

        print("CANDIDATE:")
        print(resume_data["name"])

        print()

        print("RESUME SKILLS:")
        print(resume_data["skills"])

        print()

        print("JOB DESCRIPTION:")
        print(job_description)

        print()

        print("JD SKILLS:")
        print(jd_skills)

        print("=" * 50)

    

    report = analyze_resume(
        resume_data,
        jd_skills,
        job_description
    )
    

    return report