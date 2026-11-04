CAREER_SKILLS = {

    "Software Developer": [
        "Python", "Java", "C", "Problem Solving",
        "SQL", "Computer Skills"
    ],

    "Data Scientist": [
        "Python", "SQL", "Data Analysis",
        "Machine Learning", "Mathematics", "Research"
    ],

    "Cybersecurity Analyst": [
        "Python", "SQL", "Problem Solving",
        "Computer Skills"
    ],

    "Research Assistant": [
        "Research", "Mathematics",
        "Problem Solving", "Communication"
    ],

    "Laboratory Technician": [
        "Research", "Mathematics",
        "Computer Skills", "Problem Solving"
    ],

    "Teacher": [
        "Teaching", "Communication",
        "Leadership", "Writing"
    ],

    "Content Writer": [
        "Writing", "Creativity", "Communication"
    ],

    "Editor": [
        "Writing", "Communication",
        "Creativity", "Problem Solving"
    ],

    "Accountant": [
        "Accounting", "Mathematics",
        "Computer Skills", "Problem Solving"
    ],

    "Financial Analyst": [
        "Accounting", "Mathematics",
        "Data Analysis", "Computer Skills"
    ],

    "HR Executive": [
        "Communication", "Leadership",
        "Social Skills", "Problem Solving"
    ],

    "Marketing Executive": [
        "Communication", "Creativity",
        "Leadership", "Social Skills"
    ],

    "Psychology Assistant": [
        "Communication", "Research",
        "Social Skills", "Writing"
    ],

    "Social Worker": [
        "Communication", "Social Skills",
        "Leadership", "Problem Solving"
    ],

    "Legal Assistant": [
        "Communication", "Research",
        "Writing", "Problem Solving"
    ],

    "Government Job Aspirant": [
        "Communication", "Mathematics",
        "Writing", "Problem Solving"
    ],

    "Banking Professional": [
        "Mathematics", "Accounting",
        "Communication", "Computer Skills"
    ],

    "Graphic Designer": [
        "Design", "Creativity",
        "Computer Skills", "Communication"
    ],

    "Entrepreneur": [
        "Leadership", "Communication",
        "Creativity", "Problem Solving"
    ],

    "Public Relations Executive": [
        "Communication", "Writing",
        "Social Skills", "Creativity"
    ]
}


def analyze_skill_gap(career, student_skills):

    required_skills = CAREER_SKILLS.get(career, [])

    available = []
    missing = []

    student_skills = [
        skill.lower() for skill in student_skills
    ]

    for skill in required_skills:

        if skill.lower() in student_skills:
            available.append(skill)
        else:
            missing.append(skill)

    return {
        "career": career,
        "available_skills": available,
        "missing_skills": missing,
        "total_required": len(required_skills)
    }
