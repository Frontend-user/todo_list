from django.db import models



class TaskModel(models.Model):
    text = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    def dict(self) -> dict:
        return {
            'id': self.id,
            'text': self.text,
            'is_completed': self.is_completed,
        }