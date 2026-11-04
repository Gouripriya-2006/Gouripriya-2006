CAREERS = {

    "Software Developer": {
        "education": ["BCA", "BTech", "BE", "MCA", "MTech", "BSc", "MSc"],
        "interest": ["Technology"],
        "skills": ["Python", "Java", "C", "Problem Solving", "SQL"],
        "work": ["Technical"]
    },

    "Data Scientist": {
        "education": ["BSc", "BTech", "BE", "BCA", "MSc", "MCA", "MTech", "BA", "MA"],
        "interest": ["Data Science", "Artificial Intelligence"],
        "skills": ["Python", "SQL", "Data Analysis", "Machine Learning", "Mathematics"],
        "work": ["Analytical", "Research"]
    },

    "Cybersecurity Analyst": {
        "education": ["BCA", "BTech", "BE", "MCA", "MTech", "BSc", "MSc"],
        "interest": ["Technology"],
        "skills": ["Python", "SQL", "Problem Solving", "Computer Skills"],
        "work": ["Technical", "Analytical"]
    },

    "Research Assistant": {
        "education": ["BSc", "BA", "MSc", "MA", "BTech", "MTech"],
        "interest": ["Science and Research", "Healthcare and Biology"],
        "skills": ["Research", "Mathematics", "Problem Solving", "Communication"],
        "work": ["Research", "Analytical"]
    },

    "Laboratory Technician": {
        "education": ["Plus Two - Science", "BSc", "MSc", "Diploma"],
        "interest": ["Science and Research", "Healthcare and Biology"],
        "skills": ["Research", "Mathematics", "Computer Skills"],
        "work": ["Research"]
    },

    "Teacher": {
        "education": ["BA", "BSc", "BCom", "BEd", "MA", "MSc", "MCom"],
        "interest": ["Teaching and Education"],
        "skills": ["Teaching", "Communication", "Leadership", "Writing"],
        "work": ["Teaching", "Communication"]
    },

    "Content Writer": {
        "education": ["Plus Two - Science", "Plus Two - Commerce",
                      "Plus Two - Humanities", "BA", "BSc", "BCom",
                      "BBA", "BCA", "MA", "Other"],
        "interest": ["Arts and Literature", "Media and Communication"],
        "skills": ["Writing", "Creativity", "Communication"],
        "work": ["Creative", "Communication"]
    },

    "Editor": {
        "education": ["BA", "MA", "BSc", "BCom", "BBA"],
        "interest": ["Arts and Literature", "Media and Communication"],
        "skills": ["Writing", "Communication", "Creativity"],
        "work": ["Creative", "Communication"]
    },

    "Accountant": {
        "education": ["BCom", "MCom", "MBA", "BBA"],
        "interest": ["Commerce and Finance", "Business and Management"],
        "skills": ["Accounting", "Mathematics", "Computer Skills"],
        "work": ["Finance", "Analytical"]
    },

    "Financial Analyst": {
        "education": ["BCom", "MCom", "MBA", "BBA", "BSc", "MSc"],
        "interest": ["Commerce and Finance", "Business and Management"],
        "skills": ["Accounting", "Mathematics", "Data Analysis"],
        "work": ["Finance", "Analytical"]
    },

    "HR Executive": {
        "education": ["BBA", "MBA", "BA", "MA", "BCom", "MCom"],
        "interest": ["Business and Management", "Psychology"],
        "skills": ["Communication", "Leadership", "Social Skills"],
        "work": ["Management", "Communication"]
    },

    "Marketing Executive": {
        "education": ["BBA", "MBA", "BA", "BCom", "BSc", "BCA"],
        "interest": ["Business and Management", "Media and Communication"],
        "skills": ["Communication", "Creativity", "Leadership"],
        "work": ["Management", "Creative", "Communication"]
    },

    "Psychology Assistant": {
        "education": ["BA", "MA", "BSc", "MSc"],
        "interest": ["Psychology"],
        "skills": ["Communication", "Research", "Social Skills"],
        "work": ["Research", "Social Service"]
    },

    "Social Worker": {
        "education": ["BSW", "MSW", "BA", "MA"],
        "interest": ["Social Work", "Psychology"],
        "skills": ["Communication", "Social Skills", "Leadership"],
        "work": ["Social Service", "Communication"]
    },

    "Legal Assistant": {
        "education": ["LLB", "BA", "MA"],
        "interest": ["Law and Public Administration"],
        "skills": ["Communication", "Research", "Writing"],
        "work": ["Analytical", "Communication"]
    },

    "Government Job Aspirant": {
        "education": ["SSLC", "Plus Two - Science",
                      "Plus Two - Commerce", "Plus Two - Humanities",
                      "Diploma", "BA", "BSc", "BCom", "BBA",
                      "BCA", "BTech", "BE", "Other"],
        "interest": ["Government Jobs"],
        "skills": ["Communication", "Mathematics", "Writing"],
        "work": ["Government Service", "Analytical"]
    },

    "Banking Professional": {
        "education": ["BCom", "MCom", "BBA", "MBA", "BA", "BSc"],
        "interest": ["Banking", "Commerce and Finance"],
        "skills": ["Mathematics", "Accounting", "Communication"],
        "work": ["Finance", "Analytical"]
    },

    "Graphic Designer": {
        "education": ["Plus Two - Science", "Plus Two - Commerce",
                      "Plus Two - Humanities", "Diploma", "BA",
                      "BSc", "BCA", "BBA", "Other"],
        "interest": ["Design and Creativity"],
        "skills": ["Design", "Creativity", "Computer Skills"],
        "work": ["Creative"]
    },

    "Entrepreneur": {
        "education": ["SSLC", "Plus Two - Science",
                      "Plus Two - Commerce", "Plus Two - Humanities",
                      "Diploma", "BA", "BSc", "BCom", "BBA",
                      "BCA", "BTech", "BE", "MBA", "Other"],
        "interest": ["Entrepreneurship", "Business and Management"],
        "skills": ["Leadership", "Communication", "Creativity"],
        "work": ["Management", "Creative"]
    },

    "Public Relations Executive": {
        "education": ["BA", "MA", "BBA", "MBA", "BCom", "BSc"],
        "interest": ["Media and Communication"],
        "skills": ["Communication", "Writing", "Social Skills", "Creativity"],
        "work": ["Communication"]
    }
}


def recommend_careers(education, interest, skills, work_type):

    results = []

    for career, details in CAREERS.items():

        if education not in details["education"]:
            continue

        score = 0

        if interest in details["interest"]:
            score += 40

        if work_type in details["work"]:
            score += 20

        matching_skills = [
            skill for skill in skills
            if skill in details["skills"]
        ]

        score += len(matching_skills) * 10

        results.append({
            "career": career,
            "score": min(score, 100),
            "matching_skills": matching_skills
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:5]
