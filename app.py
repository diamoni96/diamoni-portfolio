from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

PROFILE = {
    "name": "Dia Moni",
    "role": "AI/ML Enthusiast | Python Developer",
    "location": "Dhaka, Bangladesh",
    "email": "diamoni7096@gmail.com",
    "linkedin": "https://linkedin.com/in/dia-moni",
    "github": "https://github.com/diamoni96",
    "resume_file": "Dia_Moni_CV.txt",
    "summary": (
        "Aspiring AI/ML Engineer, Python Developer, and CSE student focused on "
        "building intelligent, reliable, and practical software systems. Dia is "
        "interested in machine learning, backend development, automation, and "
        "real-world problem solving through scalable technology."
    ),
}

EDUCATION = [
    {
        "institution": "Southeast University",
        "period": "11/2023 - Present",
        "location": "Dhaka, Bangladesh",
        "description": (
            "Computer Science and Engineering student developing a strong base "
            "in programming, algorithms, backend systems, AI/ML fundamentals, "
            "and practical software development."
        ),
    }
]

SKILL_GROUPS = [
    {
        "title": "Programming Languages",
        "skills": ["Python", "C++", "Java"],
    },
    {
        "title": "Backend & Software Development",
        "skills": [
            "FastAPI",
            "REST API Development",
            "Backend Development",
            "Software Design and Development",
        ],
    },
    {
        "title": "Core CS Concepts",
        "skills": [
            "OOP",
            "Data Structures and Algorithms",
            "Problem Solving",
            "Database Fundamentals",
        ],
    },
    {
        "title": "AI / Data / Analysis",
        "skills": [
            "Machine Learning Fundamentals",
            "Text Analysis",
            "Complaint and Ticket Analysis",
            "Rule-Based Classification",
            "Data Analysis",
        ],
    },
    {
        "title": "Tools / Platforms",
        "skills": [
            "Git",
            "GitHub",
            "PostgreSQL",
            "Jupyter Notebook",
            "Google Colab",
            "VS Code",
        ],
    },
    {
        "title": "Cybersecurity",
        "skills": [
            "Penetration Testing Basics",
            "Security Assessment Fundamentals",
        ],
    },
    {
        "title": "Soft Skills",
        "skills": [
            "Teamwork",
            "Communication",
            "Event Coordination",
            "Time Management",
            "Adaptability",
        ],
    },
]

PROJECTS = [
    {
        "title": "QueueStorm - Ticket Classification API",
        "type": "Backend / AI-adjacent API",
        "description": (
            "Python-based ticket classification and complaint investigation API "
            "designed for digital finance support operations."
        ),
        "features": [
            "Analyzes customer complaints and cross-references transaction history.",
            "Classifies case types and routes issues to the appropriate department.",
            "Generates structured support responses using rule-based logic.",
            "Highlights backend engineering, workflow automation, and structured problem solving.",
        ],
        "stack": ["Python", "FastAPI", "REST API", "Rule-Based Logic"],
    },
    {
        "title": "Student Management System",
        "type": "C++ Systems Project",
        "description": (
            "Console-based student management system with file handling, "
            "persistent storage, and structured record operations."
        ),
        "features": [
            "Adds, views, searches, edits, and deletes student records.",
            "Stores records persistently with file handling.",
            "Implements Merge Sort for roll, CGPA, name, and department sorting.",
            "Supports ascending and descending order for record organization.",
        ],
        "stack": ["C++", "File Handling", "Data Structures", "Merge Sort"],
    },
    {
        "title": "University Complaint Analyzer",
        "type": "Analysis Project",
        "description": (
            "Complaint analysis project focused on understanding university-related "
            "feedback and organizing issues for clearer review."
        ),
        "features": [
            "Applies text analysis and structured complaint review concepts.",
            "Connects AI/data interests with real-world institutional problem solving.",
            "Public implementation details are limited in the current CV source.",
        ],
        "stack": ["Text Analysis", "Data Analysis", "Classification Concepts"],
    },
]

EXPERIENCE = [
    {
        "role": "Volunteer",
        "organization": "IEEE Computer Society Southeast University Student Branch Chapter",
        "period": "05/2026",
        "description": (
            "Supported student-focused technical activities, event coordination, "
            "and community-driven learning environments."
        ),
    }
]

ACHIEVEMENTS = [
    {
        "title": "SUST CSE Carnival 2026 Hackathon Finalist",
        "detail": "Reached the final round among top 50 teams from 700+ participants.",
    },
    {
        "title": "DUET CSE Carnival 2026 ICT Olympiad Participant",
        "detail": "Participated in a competitive ICT-focused university carnival event.",
    },
]

CERTIFICATES = [
    "Structuring Machine Learning Projects",
    "Maximize Productivity With AI Tools",
    "C)PTE: Certified Penetration Testing Engineer",
]

NAV_ITEMS = [
    ("About", "about"),
    ("Education", "education"),
    ("Skills", "skills"),
    ("Projects", "projects"),
    ("Leadership", "leadership"),
    ("Achievements", "achievements"),
    ("Contact", "contact"),
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        education=EDUCATION,
        skill_groups=SKILL_GROUPS,
        projects=PROJECTS,
        experience=EXPERIENCE,
        achievements=ACHIEVEMENTS,
        certificates=CERTIFICATES,
        nav_items=NAV_ITEMS,
    )


@app.route("/resume")
def resume():
    return send_from_directory(
        "static/files",
        PROFILE["resume_file"],
        as_attachment=False,
        download_name=PROFILE["resume_file"],
    )


@app.route("/download-cv")
def download_cv():
    return send_from_directory(
        "static/files",
        PROFILE["resume_file"],
        as_attachment=True,
        download_name=PROFILE["resume_file"],
    )


if __name__ == "__main__":
    app.run(debug=True)
