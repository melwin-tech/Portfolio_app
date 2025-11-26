from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    description = models.TextField()  
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)
    

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend Development'),
        ('backend', 'Backend Development'),
        ('database', 'Database'),
        ('tools', 'Tools / DevOps'),
        ('soft', 'Soft Skills'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()                 
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='other'
    )
    years_experience = models.DecimalField(
        max_digits=4, 
        decimal_places=1,
        help_text="Years of experience (e.g., 1.5, 2.0)"
    )
    icon = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional: icon class (FontAwesome) or image URL"
    )
    description = models.TextField(
        blank=True,
        help_text="Short description about the skill"
    )
    is_highlight = models.BooleanField(
        default=False,
        help_text="Show this skill as highlighted on home page"
    )
    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"

