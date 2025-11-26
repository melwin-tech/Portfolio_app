import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Portfolio_app.settings")
django.setup()

from portfolio.models import Skill

# Sample skills data
skills_data = [
    # Frontend
    {"name": "HTML5", "proficiency": 95, "category": "frontend", "years_experience": 4, "icon": "fab fa-html5", "description": "Semantic markup, accessibility", "is_highlight": True},
    {"name": "CSS3", "proficiency": 90, "category": "frontend", "years_experience": 4, "icon": "fab fa-css3-alt", "description": "Responsive design, Flexbox, Grid", "is_highlight": True},
    {"name": "JavaScript", "proficiency": 85, "category": "frontend", "years_experience": 3, "icon": "fab fa-js", "description": "DOM manipulation, ES6+, AJAX", "is_highlight": True},
    {"name": "React", "proficiency": 80, "category": "frontend", "years_experience": 2, "icon": "fab fa-react", "description": "SPA development, component-based", "is_highlight": False},

    # Backend
    {"name": "Python", "proficiency": 95, "category": "backend", "years_experience": 4, "icon": "fab fa-python", "description": "Django, Flask, scripting", "is_highlight": True},
    {"name": "Django", "proficiency": 90, "category": "backend", "years_experience": 3, "icon": "fas fa-leaf", "description": "Web frameworks, ORM, templates", "is_highlight": True},
    {"name": "REST API", "proficiency": 85, "category": "backend", "years_experience": 2, "icon": "fas fa-network-wired", "description": "API development, JSON responses", "is_highlight": False},

    # Database
    {"name": "MySQL", "proficiency": 85, "category": "database", "years_experience": 3, "icon": "fas fa-database", "description": "Relational databases, queries", "is_highlight": True},
    {"name": "PostgreSQL", "proficiency": 80, "category": "database", "years_experience": 2, "icon": "fas fa-database", "description": "Advanced queries, indexing", "is_highlight": False},
    {"name": "MongoDB", "proficiency": 70, "category": "database", "years_experience": 2, "icon": "fas fa-leaf", "description": "NoSQL database, JSON storage", "is_highlight": False},

    # Tools / DevOps
    {"name": "Git", "proficiency": 95, "category": "tools", "years_experience": 4, "icon": "fab fa-git-alt", "description": "Version control, branching", "is_highlight": True},
    {"name": "GitHub", "proficiency": 90, "category": "tools", "years_experience": 4, "icon": "fab fa-github", "description": "Repository hosting, collaboration", "is_highlight": True},
    {"name": "Docker", "proficiency": 80, "category": "tools", "years_experience": 2, "icon": "fab fa-docker", "description": "Containerization, dev environments", "is_highlight": False},
    {"name": "VS Code", "proficiency": 90, "category": "tools", "years_experience": 4, "icon": "fas fa-code", "description": "IDE for coding, debugging", "is_highlight": False},

    # Soft Skills
    {"name": "Communication", "proficiency": 90, "category": "soft", "years_experience": 4, "icon": "fas fa-comments", "description": "Team collaboration, presentations", "is_highlight": True},
    {"name": "Problem Solving", "proficiency": 95, "category": "soft", "years_experience": 4, "icon": "fas fa-lightbulb", "description": "Analytical thinking, debugging", "is_highlight": True},
    {"name": "Time Management", "proficiency": 85, "category": "soft", "years_experience": 4, "icon": "fas fa-clock", "description": "Meeting deadlines efficiently", "is_highlight": False},
]

# Insert into database
for skill in skills_data:
    obj, created = Skill.objects.get_or_create(
        name=skill["name"],
        defaults={
            "proficiency": skill["proficiency"],
            "category": skill["category"],
            "years_experience": skill["years_experience"],
            "icon": skill["icon"],
            "description": skill["description"],
            "is_highlight": skill["is_highlight"]
        }
    )
    if created:
        print(f"Added skill: {obj.name}")
    else:
        print(f"Skill already exists: {obj.name}")

print("All skills injected successfully!")
