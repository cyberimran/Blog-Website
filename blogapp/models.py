from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField(max_length=70, default="No Description")
    category = models.ForeignKey(Category, null=True, blank=False, on_delete=models.SET_NULL,)
    slug = models.CharField(unique=True, null=False, blank=False, max_length=150)
    dateandtime = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    premium = models.BooleanField(default=False)
    content = RichTextField()

    def __str__(self):
        return self.title
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.image)
