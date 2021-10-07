from django.db import models


class Todolist(models.Model):
    todoitem = models.CharField(max_length=800)
    todoitem_fav = models.BooleanField()
    todoitem_done = models.BooleanField()
    
    def item_class(self):
        classes = []
        if self.todoitem_fav :
            classes.append("list-group-item-success")
        if self.todoitem_done:
            classes.append("list-group-item-strikethrough")
        if not classes:
            classes.append("list-group-item-light") 
        return " ".join(classes)
    

    def btn_done_class(self):
        classes = []
        if self.todoitem_done:
            classes.append("btn-success") 
        else:
            classes.append("btn-outline-success")
        return " ".join(classes)



    def __str__(self):
        # return f"Todolist ID>>> {self.id}, Todoitem>>> {self.todoitem}"
        return f"Todolist: {self.id} | {self.todoitem} | {self.todoitem_fav} | {self.todoitem_done}"