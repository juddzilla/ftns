from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid

class Exercise(models.Model):
    # Enum choices based on your provided data
    CATEGORY_CHOICES = [
        ('strength', 'Strength'),
        ('stretching', 'Stretching'),
        ('plyometrics', 'Plyometrics'),
        ('strongman', 'Strongman'),
        ('powerlifting', 'Powerlifting'),
        ('cardio', 'Cardio'),
        ('olympic weightlifting', 'Olympic Weightlifting'),
    ]
    EQUIPMENT_CHOICES = [
        ('body only', 'Body Only'),
        ('machine', 'Machine'),
        ('other', 'Other'),
        ('foam roll', 'Foam Roll'),
        ('kettlebells', 'Kettlebells'),
        ('dumbbell', 'Dumbbell'),
        ('cable', 'Cable'),
        ('barbell', 'Barbell'),
        ('bands', 'Bands'),
        ('medicine ball', 'Medicine Ball'),
        ('exercise ball', 'Exercise Ball'),
        ('e-z curl bar', 'E-Z Curl Bar'),
    ]
    FORCE_CHOICES = [
        ('pull', 'Pull'),
        ('push', 'Push'),
        ('static', 'Static'),
    ]
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert'),
    ]
    MECHANIC_CHOICES = [
        ('compound', 'Compound'),
        ('isolation', 'Isolation'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(unique=True, null=False)
    aliases = ArrayField(models.TextField(), blank=True, null=True)
    primary_muscles = ArrayField(models.TextField(), blank=True, null=True)  # Assuming muscle is a text field
    secondary_muscles = ArrayField(models.TextField(), blank=True, null=True)  # Assuming muscle is a text field
    force = models.CharField(max_length=50, choices=FORCE_CHOICES, blank=True, null=True)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, null=False)
    mechanic = models.CharField(max_length=50, choices=MECHANIC_CHOICES, blank=True, null=True)
    equipment = models.CharField(max_length=50, choices=EQUIPMENT_CHOICES, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=False)
    instructions = ArrayField(models.TextField(), blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tips = ArrayField(models.TextField(), blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'exercises'
