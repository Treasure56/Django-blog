from django.db import models

class BlogPost(models.Model):
    reporter = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/%y/%n/%d/')
    popular = models.BooleanField(default=False)
    blog_date = models.DateTimeField()

    def _str__(self):
        return self.title
