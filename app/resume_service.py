from app.parser import extract_text_from_pdf

from app.extractor import (
    extract_name,
    extract_skills,
    extract_section
)


def build_resume_data(
    pdf_path
):

    resume_text = (
        extract_text_from_pdf(
            pdf_path
        )
    )

    return {

        "name":
        extract_name(
            resume_text
        ),

        "skills":
        extract_skills(
            resume_text
        ),

        "education":
        extract_section(
            resume_text,
            "EDUCATION",
            "PROFESSIONAL EXPERIENCE"
        ),

        "experience":
        extract_section(
            resume_text,
            "PROFESSIONAL EXPERIENCE",
            "PROJECTS"
        ),

        "projects":
        extract_section(
            resume_text,
            "PROJECTS",
            "TECHNICAL SKILLS"
        )

    }