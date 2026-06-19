import json
from parser import extract_text_from_pdf
from extractor import extract_section, extract_skills,extract_name
from ats_analyser import analyze_resume

resume_text = extract_text_from_pdf(r"C:\Users\hplap\Downloads\NANDINI_Resume_Job_Latest.pdf")

name = extract_name(resume_text)

skills = extract_skills(resume_text)

education = extract_section(
    resume_text,
    "EDUCATION",
    "PROFESSIONAL EXPERIENCE"
)

experience = extract_section(
    resume_text,
    "PROFESSIONAL EXPERIENCE",
    "PROJECTS"
)

projects = extract_section(
    resume_text,
    "PROJECTS",
    "TECHNICAL SKILLS"
)

resume_data = {
    "name": name,
    "skills": skills,
    "education": education,
    "experience": experience,
    "projects": projects
}





job_description = """
Looking for Machine Learning Engineer.

Skills Required:

Python
Machine Learning
Docker
AWS
"""

jd_skills = extract_skills(job_description)
report = analyze_resume(
    resume_data,
    jd_skills
)

print(
    json.dumps(
        report,
        indent=4
    )
)