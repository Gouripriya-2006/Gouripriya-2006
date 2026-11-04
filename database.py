import sqlite3


DATABASE = "career_ai.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():

    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            education TEXT NOT NULL,
            interest TEXT NOT NULL,
            percentage REAL,
            work_type TEXT,
            skills TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_student(name, education, interest,
                 percentage, work_type, skills):

    connection = get_connection()

    connection.execute("""
        INSERT INTO students
        (name, education, interest, percentage, work_type, skills)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name,
        education,
        interest,
        percentage,
        work_type,
        ", ".join(skills)
    ))

    connection.commit()
    connection.close()


def get_all_students():

    connection = get_connection()

    students = connection.execute("""
        SELECT * FROM students
        ORDER BY created_at DESC
    """).fetchall()

    connection.close()

    return students
