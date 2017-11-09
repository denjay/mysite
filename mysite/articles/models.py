from django.db import models
from tinymce.models import HTMLField


class Classification(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = HTMLField()
    classification = models.ForeignKey('Classification')
    date = models.DateTimeField(auto_now_add=True)
    click = models.IntegerField(default=0)
    top = models.IntegerField(default=0)
    isDelete = models.BooleanField()
    cover = models.ImageField(upload_to='articles')

    def __str__(self):
        return self.title

