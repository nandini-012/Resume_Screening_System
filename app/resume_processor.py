from parser import extract_text_from_pdf, extract_text_from_pdf
from extractor import extract_section, extract_skills,extract_name

def extract_name(text):
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if line:
            return line

    return "Unknown"


resume_text = extract_text_from_pdf(r"C:\\Users\\hplap\\Downloads\\NANDINI_Resume_Job_Latest.pdf")



lines = resume_text.split("\n")

for i, line in enumerate(lines[:20]):
    print(i, ":", line)
    
    
resume_data = {
    "name": extract_name(resume_text),
    "skills": extract_skills(resume_text)
}

print(resume_data)

education = extract_section(
    resume_text,
    "EDUCATION",
    "PROFESSIONAL EXPERIENCE"
)

print(education)

experience = extract_section(
    resume_text,
    "PROFESSIONAL EXPERIENCE",
    "PROJECTS"
)

print(experience)

projects = extract_section(
    resume_text,
    "PROJECTS",
    "TECHNICAL SKILLS"
)

print(projects)

