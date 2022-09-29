from django.db import models

class Task(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    # on_delete CASCADE agar ketika user terhapus maka task ikut terhapus
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
