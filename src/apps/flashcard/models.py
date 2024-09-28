from django.db import models
from django.contrib.auth.models import User


class Deck(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    studied_at = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
LEVEL = (
    ('0', 'Não estudado'),
    ('1', 'Iniciante'),
    ('2', 'Intermediario'),
    ('3', 'Avançado'),
)


class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    level = models.CharField(max_length=1, choices=LEVEL, default='0')
    created_at = models.DateTimeField(auto_now=True)
    studied_at = models.DateField(blank=True, null=True)
    