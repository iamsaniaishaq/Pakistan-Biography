from django.db import models

class PrimeMinisters(models.Model):
    name = models.CharField(max_length=255)
    english_bio = models.CharField(max_length=500, blank=True)
    urdu_bio = models.CharField(max_length=500, blank=True, default='')
    english_achievements = models.CharField(max_length=500, blank=True, default='')
    urdu_achievements = models.CharField(max_length=500, blank=True, default='')
    youtube_link = models.CharField(max_length=500, blank=True, default='')
    background_color = models.CharField(max_length=7)
    term = models.CharField(max_length=100)
    image = models.ImageField(upload_to='prime_ministers_images/', blank=True, null=True)
    def __str__(self):
        return self.name