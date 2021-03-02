from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    completed = models.BooleanField(default=False)
    time_completed = models.DateTimeField(blank=True, null=True)
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, completed: {'yes' if self.completed else 'no'}"
