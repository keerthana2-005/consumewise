from django.db import models
from django.contrib.auth.models import User
from modelapp import static


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    problemsInput = models.CharField(max_length=200)
    diabetes = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], default='No')
    blood_pressure = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], default='No')
    


    def __str__(self):
        return f'{self.user.username} Profile'