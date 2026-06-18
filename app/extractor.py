from parser import extract_text_from_pdf

SKILLS = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "fastapi",
    "docker",
    "aws",
    "git",
    "react",
    "mongodb"
]

def extract_skills(text):
    found_skills = []

    text = text.lower()

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills

resume_text = extract_text_from_pdf(r"C:\Users\hplap\Downloads\NANDINI_Resume_Job_Latest.pdf")
skills = extract_skills(resume_text)
print(skills)