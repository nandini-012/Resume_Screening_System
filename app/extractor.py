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
    "machine learning",
    "tensorflow",
    "pytorch",
    "docker",
    "aws",
    "fastapi",
    "flask",
    "sql",
    "mongodb",
    "git",
    "linux",
    "numpy",
    "pandas",
    "scikit-learn"
]




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

    top_text = "\n".join(
        text.split("\n")[:10]
    )


    doc = nlp(top_text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return rule_based_name(text)


def extract_skills(text):
    found_skills = []

    text = text.lower()

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills



def extract_section(text, start_heading, end_heading):
    
    text_upper = text.upper()

    start = text_upper.find(start_heading)

    if start == -1:
        return ""

    end = text_upper.find(end_heading, start)

    if end == -1:
        return text[start:]

    return text[start:end]