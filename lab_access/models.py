from django.db import models

# Create your models here.
class User (models.Model):
    user_types = [
        ('student', 'Student'),
        ('faculty', 'Faculty Member'),
        ('staff', 'Staff Member'),
        ('janitor', 'Janitor'),
    ]

    status_choices = [
        ('active', 'Active'),
        ('suspended', 'Suspended'),
    ]

    name = models.CharField(max_length = 100)
    student_id = models.CharField(max_length = 10, unique = True)
    user_type = models.CharField(choices = user_types, max_length = 10)
    status = models.CharField(choices = status_choices, max_length = 10, default = 'active')
    created_at = models.DateTimeField(auto_now_add = True)

class AccessLog(models.Model):
    action_choices = [('entry', 'Entry'), ('exit', 'Exit')]
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    action = models.CharField(choices = action_choices, max_length = 5)
    timestamp = models.DateTimeField(auto_now_add = True)
