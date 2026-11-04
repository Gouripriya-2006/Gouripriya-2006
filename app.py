from flask import Flask, render_template, request
from career_engine import recommend_careers
from skill_gap import analyze_skill_gap
from roadmap import get_roadmap
from course_recommendations import get_courses
from database import create_table, save_student, get_all_students

app = Flask(__name__)

# Create database table
create_table()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():

    students = get_all_students()

    return render_template(
        "dashboard.html",
        students=students
    )


@app.route("/assessment")
def assessment():
    return render_template("assessment.html")


@app.route("/assess", methods=["POST"])
def assess():

    name = request.form.get("name", "").strip()
    education = request.form.get("education", "")
    interest = request.form.get("interest", "")
    skills = request.form.getlist("skills")
    work_type = request.form.get("work_type", "")

    try:
        percentage = float(request.form.get("percentage", 0))
    except ValueError:
        return "Invalid percentage entered.", 400

    if not name or not education or not interest or not work_type:
        return "Please complete all required fields.", 400

    if not 0 <= percentage <= 100:
        return "Percentage must be between 0 and 100.", 400

    # Save student assessment
    save_student(
        name,
        education,
        interest,
        percentage,
        work_type,
        skills
    )

    # Generate career recommendations
    recommendations = recommend_careers(
        education,
        interest,
        skills,
        work_type
    )

    return render_template(
        "career_result.html",
        name=name,
        education=education,
        percentage=percentage,
        skills=skills,
        recommendations=recommendations
    )


@app.route("/skill-gap/<career>")
def skill_gap(career):

    skills = request.args.getlist("skills")

    result = analyze_skill_gap(career, skills)

    return render_template(
        "skill_gap.html",
        result=result
    )


@app.route("/roadmap/<career>")
def roadmap(career):

    career_roadmap = get_roadmap(career)

    return render_template(
        "roadmap.html",
        career=career,
        roadmap=career_roadmap
    )


@app.route("/courses/<career>")
def courses(career):

    recommended_courses = get_courses(career)

    return render_template(
        "courses.html",
        career=career,
        courses=recommended_courses
    )


if __name__ == "__main__":
    app.run(debug=True)

