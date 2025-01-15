from django.db import models

class Idea(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='idea_images/')
    content = models.TextField()
    interest = models.PositiveIntegerField(default=0)
    devtools = models.ManyToManyField('devtool.DevTool', related_name='ideas') 

    def __str__(self):
        return self.title

class IdeaStar(models.Model):
    idea = models.OneToOneField(Idea, on_delete=models.CASCADE, related_name='star')
    is_starred = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.idea.title} - {'Starred' if self.is_starred else 'Not Starred'}"