from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Articles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    title = models.TextField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.date}"

    class Meta:
        verbose_name_plural = 'Articles'
        ordering = ['date', 'time']
