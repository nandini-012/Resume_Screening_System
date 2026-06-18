from parser import extract_text_from_pdf, extract_text_from_pdf
from extractor import extract_skills

def extract_name(text):
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if line:
            return line

    return "Unknown"


resume_text = extract_text_from_pdf(r"C:\\Users\\hplap\\Downloads\\NANDINI_Resume_Job_Latest.pdf")

resume_data = {
    "name": extract_name(resume_text),
    "skills": extract_skills(resume_text)
}

print(resume_data)