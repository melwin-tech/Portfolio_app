import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Portfolio_app.settings")
django.setup()

from portfolio.models import Project
from django.core.files import File

# Sample project data
projects_data = [
    {
        "title": "Portfolio Website",
        "domain": "Web Development",
        "description": "A personal portfolio website built with Django and Bootstrap showcasing skills and projects.",
        "image_path": "media/projects/portfolio.jpg",
        "url": "https://example.com/portfolio"
    },
    {
        "title": "E-commerce Platform",
        "domain": "Web Development",
        "description": "Full-featured e-commerce platform with product catalog, cart, checkout, and admin panel.",
        "image_path": "media/projects/ecommerce.jpg",
        "url": "https://example.com/ecommerce"
    },
    {
        "title": "Blog Application",
        "domain": "Web Development",
        "description": "Blog app with user authentication, post creation, editing, and comments functionality.",
        "image_path": "media/projects/blog.jpg",
        "url": "https://example.com/blog"
    },
    {
        "title": "Finance Tracker",
        "domain": "Web Application",
        "description": "Personal finance tracker to manage monthly income and expenses with charts and reports.",
        "image_path": "media/projects/finance.jpg",
        "url": ""
    },
    {
        "title": "Task Management App",
        "domain": "Productivity",
        "description": "Todo/Task management app with deadlines, priorities, and status tracking built in Django.",
        "image_path": "media/projects/todo.jpg",
        "url": ""
    },
]

# Insert into database
for project in projects_data:
    # Check if project already exists
    obj, created = Project.objects.get_or_create(
        title=project["title"],
        defaults={
            "domain": project["domain"],
            "description": project["description"],
            "url": project["url"],
        }
    )
    
    # Add image if file exists
    if created:
        image_path = project["image_path"]
        if os.path.exists(image_path):
            with open(image_path, "rb") as f:
                obj.image.save(os.path.basename(image_path), File(f), save=True)
        print(f"Added project: {obj.title}")
    else:
        print(f"Project already exists: {obj.title}")

print("All projects injected successfully!")
