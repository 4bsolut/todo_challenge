from django.db import models

class Todo(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    status=models.BooleanField(default=False)
