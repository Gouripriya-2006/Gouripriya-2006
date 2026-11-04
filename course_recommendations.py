COURSES = {

    "Software Developer": [
        "Python or Java Programming",
        "Data Structures and Algorithms",
        "Web Development",
        "Database Management",
        "Git and GitHub"
    ],

    "Data Scientist": [
        "Python for Data Science",
        "Statistics and Mathematics",
        "Pandas and NumPy",
        "Data Visualization",
        "Machine Learning"
    ],

    "Cybersecurity Analyst": [
        "Computer Networking",
        "Linux Fundamentals",
        "Cybersecurity Basics",
        "Ethical Hacking Fundamentals",
        "Security Tools"
    ],

    "Research Assistant": [
        "Research Methodology",
        "Data Collection Techniques",
        "Data Analysis",
        "Academic Writing"
    ],

    "Laboratory Technician": [
        "Laboratory Safety",
        "Laboratory Techniques",
        "Scientific Equipment Handling",
        "Quality Control Basics"
    ],

    "Teacher": [
        "Teaching Methodology",
        "Classroom Management",
        "Communication Skills",
        "Educational Technology"
    ],

    "Content Writer": [
        "Creative Writing",
        "English Grammar",
        "Content Writing",
        "SEO Fundamentals"
    ],

    "Editor": [
        "Proofreading",
        "Editing Techniques",
        "Grammar and Language",
        "Publishing Basics"
    ],

    "Accountant": [
        "Financial Accounting",
        "Tally and Accounting Software",
        "GST Fundamentals",
        "Advanced Excel"
    ],

    "Financial Analyst": [
        "Financial Management",
        "Advanced Excel",
        "Financial Statement Analysis",
        "Data Analysis"
    ],

    "HR Executive": [
        "Human Resource Management",
        "Recruitment and Selection",
        "Communication Skills",
        "HR Analytics"
    ],

    "Marketing Executive": [
        "Marketing Fundamentals",
        "Digital Marketing",
        "Social Media Marketing",
        "Market Research"
    ],

    "Psychology Assistant": [
        "Introduction to Psychology",
        "Human Behaviour",
        "Research Methodology",
        "Psychological Assessment Fundamentals"
    ],

    "Social Worker": [
        "Social Work Fundamentals",
        "Community Development",
        "Counselling Skills",
        "Social Welfare Programmes"
    ],

    "Legal Assistant": [
        "Legal Research",
        "Legal Documentation",
        "Indian Constitution",
        "Basic Legal Procedures"
    ],

    "Government Job Aspirant": [
        "General Knowledge",
        "Indian Constitution",
        "Quantitative Aptitude",
        "Reasoning",
        "English Language"
    ],

    "Banking Professional": [
        "Banking Awareness",
        "Quantitative Aptitude",
        "Reasoning Ability",
        "Financial Awareness"
    ],

    "Graphic Designer": [
        "Design Fundamentals",
        "Typography and Colour Theory",
        "Graphic Design Software",
        "UI Design Basics"
    ],

    "Entrepreneur": [
        "Business Management",
        "Entrepreneurship Development",
        "Financial Planning",
        "Digital Marketing"
    ],

    "Public Relations Executive": [
        "Public Relations Fundamentals",
        "Media Communication",
        "Content Writing",
        "Public Speaking"
    ]
}


def get_courses(career):

    return COURSES.get(career, [
        "Career Fundamentals",
        "Communication Skills",
        "Computer Skills",
        "Practical Training"
    ])
