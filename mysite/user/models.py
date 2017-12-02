from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=40)
    date = models.DateField(auto_now_add=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Comment(models.Model):
    contain = models.CharField(max_length=500)
    article = models.ForeignKey('articles.Articles')
    user = models.ForeignKey("UserInfo")
    date = models.DateField(auto_now_add=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.contain