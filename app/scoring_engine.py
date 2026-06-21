from app.semantic_matcher import (calculate_similarity)
def calculate_skill_score(
    matched_skills,
    total_required_skills
):

    if total_required_skills == 0:
        return 0

    return (
        len(matched_skills)
        /
        total_required_skills
    ) * 40
    
def calculate_project_score(
    projects_text,
    job_description
):

    similarity = (
        calculate_similarity(
            projects_text,
            job_description
        )
    )

    return round(
        similarity * 0.25,
        2
    )

def calculate_experience_score(
    experience_text
):

    if not experience_text:
        return 0

    keywords = [
        "intern",
        "engineer",
        "developer",
        "contributor"
    ]

    score = 0

    text = experience_text.lower()

    for keyword in keywords:

        if keyword in text:
            score += 5

    return min(score, 25)


def calculate_education_score(
    education_text
):

    if not education_text:
        return 0

    if (
        "bachelor"
        in education_text.lower()
    ):
        return 10

    return 5


def calculate_overall_score(
    matched_skills,
    total_required_skills,
    projects_text,
    experience_text,
    education_text,
    job_description
):

    skill_score = (
        calculate_skill_score(
            matched_skills,
            total_required_skills
        )
    )

    project_score = (
        calculate_project_score(
            projects_text,
            job_description
        )
    )

    experience_score = (
        calculate_experience_score(
            experience_text
        )
    )

    education_score = (
        calculate_education_score(
            education_text
        )
    )

    return round(

        skill_score
        +
        project_score
        +
        experience_score
        +
        education_score,

        2
    )