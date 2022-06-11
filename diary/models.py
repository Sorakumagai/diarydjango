from django.db import models


class Note(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=200)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name