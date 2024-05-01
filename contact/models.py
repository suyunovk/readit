from django.db import models

class TeamStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Contact(TeamStamp):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.full_name

class ContactInfo(TeamStamp):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    website = models.URLField()


