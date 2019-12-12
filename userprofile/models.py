from django.db import models

# Create your models here.
class userProfile(models.Model):
    """ This is User Profile acording to requirement """
    user_name = models.CharField(max_length=128, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True)
    skill = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user_name

class Resume(models.Model):
    """ This is resume model table resume and username """
    name = models.CharField(max_length = 100)
    pdf = models.FileField(upload_to='Resume/')

    def __str__(self):
        return self.name
