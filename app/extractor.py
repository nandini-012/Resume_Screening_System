from parser import extract_text_from_pdf
import spacy
nlp = spacy.load("en_core_web_sm")

HEADINGS = {
    "skills",
    "education",
    "experience",
    "projects",
    "certifications",
    "resume",
    "curriculum vitae"
}

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



def rule_based_name(text):

    lines = text.split("\n")

    for line in lines[:15]:

        line = line.strip()

        if not line:
            continue

        if line.lower() in HEADINGS:
            continue

        words = line.split()

        if (
            1 <= len(words) <= 4
            and not any(char.isdigit() for char in line)
            and "@" not in line
        ):
            return line

    return "Unknown"

def extract_name(text):

    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return rule_based_name(text)
