from app.matcher import match_skills
from app.scoring_engine import (calculate_overall_score)


def analyze_resume(
    resume_data,
    jd_skills,
    job_description
):

    skill_result = match_skills(
        resume_data["skills"],
        jd_skills
    )
    
    report = {

        "candidate": resume_data["name"],

        "overall_score":
        calculate_overall_score(
            skill_result["matched"],
            len(jd_skills),
            resume_data["projects"],
            resume_data["experience"],
            resume_data["education"],
            job_description
        ),
        
        "matched_skills":
        skill_result["matched"],

        "missing_skills":
        skill_result["missing"],
        
        "strengths":
        generate_strengths(
        skill_result["matched"]
        ),
    
        "recommendations":
        generate_recommendations(
        skill_result["missing"]
        )

    }

    return report


    
def generate_strengths(
    matched_skills
):

    strengths = []

    for skill in matched_skills:

        strengths.append(
            f"Has {skill} skill"
        )

    return strengths

def generate_recommendations(
    missing_skills
):

    recommendations = []

    for skill in missing_skills:

        recommendations.append(
            f"Consider learning {skill}"
        )

    return recommendations


