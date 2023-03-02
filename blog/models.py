from django.db import models


print(" i am model")
class Todo(models.Model):
    task = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.task}"



class checker(models.Model):
    box = models.BooleanField()
    
    def __str__(self):
        return f"{self.box}"
    