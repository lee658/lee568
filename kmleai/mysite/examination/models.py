from django.db import models
from django.urls import reverse

class Examination(models.Model):
    tensorflowImg = models.ImageField(blank=True, upload_to='tensorflow')
    
    def get_absolute_url(self):
        return reverse('examination:examination_detail', args=[self.id])
