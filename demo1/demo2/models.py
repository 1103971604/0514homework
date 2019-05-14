from django.db import models

# Create your models here.
class Bookinfo(models.Model):
    title=models.CharField(max_length=20)
    data=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Heroinfo(models.Model):
    name =models.CharField(max_length=20)
    age=models.IntegerField()
    skill=models.CharField(max_length=20,null=True)
    book=models.ForeignKey(Bookinfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
