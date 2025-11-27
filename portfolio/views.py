from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.mail import send_mail

# Create your views here.

def home(request):
    highlighted_skills = Skill.objects.filter(is_highlight=True)
    latest_projects = Project.objects.all()[:3]
    context = {
        'highlighted_skills': highlighted_skills,
        'latest_projects': latest_projects
    }
    return render(request, 'portfolio/home.html', context )

def project(request,id):
    projects = get_object_or_404(request, id=id)
    return render(request,'portfolio/project.html', {'project':projects})

def skill(request,id):
    skills = get_object_or_404(request, id=id)
    return render(request,'portfolio/skills.html', {'project':skills})

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        msg = request.POST.get("message")


        full_message = f"Message from: {name}\nEmail: {email}\n\nMessage:\n{msg}"


        send_mail(
            subject="New Contact Form Message",
            message=full_message,
            from_email=email,  
            recipient_list=['202301021.melwinmml@student.xavier.ac.in'],  
        )

        return redirect( "home")

    return render(request, "portfolio/contact.html")
