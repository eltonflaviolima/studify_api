from rest_framework import serializers
from django.contrib.auth.models import User
from apps.flashcard.models import Card, Deck


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        
        
class DeckSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Deck
        fields = '__all__'
        
        def create(self, validated_data):
            request = self.context.get("request")
            user = request.user
            print(user)
            deck = Deck.objects.create(user=user, **validated_data)
            return deck
        

class DeckByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        exclude = ['user']
        

class CardSerializer(serializers.ModelSerializer):
    deck = serializers.ReadOnlyField(source='deck.title')
    class Meta:
        model = Card
        fields = '__all__'
        
        
class CardsByDeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        exclude = ['deck']