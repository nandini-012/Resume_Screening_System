from matcher import match_skills


def analyze_resume(
    resume_data,
    jd_skills
):

    skill_result = match_skills(
        resume_data["skills"],
        jd_skills
    )

    report = {

        "candidate": resume_data["name"],

        "overall_score":
        skill_result["score"],

        "matched_skills":
        skill_result["matched"],

        "missing_skills":
        skill_result["missing"]

    }

    return report