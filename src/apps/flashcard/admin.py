from django.contrib import admin
from .models import Deck, Card


@admin.register(Deck)
class DecksAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('question', 'deck', 'level')
    
