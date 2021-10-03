from django.db import models


class Todolist(models.Model):
    todoitem = models.CharField(max_length=800)
    todoitem_fav = models.BooleanField()
    

    def __str__(self):
        return f"Todolist: {self.todoitem}"