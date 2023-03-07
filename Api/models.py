from django.db import models



class TaskModel(models.Model):
    text = models.CharField(max_length=200)
    list = models.ForeignKey('ListModel', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    def dict(self) -> dict:
        return {
            'id': self.id,
            'text': self.text,
            'is_completed': self.is_completed
        }



class ListModel(models.Model):
    name = models.CharField(max_length=100)
    def dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
        }