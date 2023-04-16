from django.db import models
from django.conf import settings

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.text

class FavouriteQuote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'quote')
