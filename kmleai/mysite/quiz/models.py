from django.db import models
from django.urls import reverse

class Quiz(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    contents = models.TextField()
    image_1 = models.ImageField(blank=True, upload_to='quiz/quiz/%Y/%m/%d')
    image_2 = models.ImageField(blank=True, upload_to='quiz/quiz/%Y/%m/%d')
    image_3 = models.ImageField(blank=True, upload_to='quiz/quiz/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('quiz:quiz_detail', args=[self.id])
