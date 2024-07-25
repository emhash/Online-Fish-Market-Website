from django.db import models

class ContactUsMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f" {self.name} Contact about: {self.subject}"