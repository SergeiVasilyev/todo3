from django.db import models


class TodoCat(models.Model):
    name = models.CharField(max_length=400, unique=True, blank=False)
    selected = models.BooleanField(default=0)

    def item_class(self):
        classes = []
        if self.selected :
            classes.append("selected")
        return " ".join(classes)

    def __str__(self):
        return self.name

    # def __str__(self):
    #     return f"Todocat: {self.id} | {self.name}"

class Todolist(models.Model):
    todoitem = models.CharField(max_length=800)
    todoitem_fav = models.BooleanField()
    todoitem_done = models.BooleanField()
    todo_description = models.CharField(max_length=1000, default=None, blank=True, null=True)
    category = models.ForeignKey(TodoCat, on_delete=models.CASCADE, blank=True, null=True) #SET_DEFAULT , to_field='name'
    
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
        return f"Todolist: {self.id} | {self.category} | {self.todoitem} | {self.todoitem_fav} | {self.todoitem_done} | {self.todo_description}"



