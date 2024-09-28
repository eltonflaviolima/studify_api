from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from apps.flashcard.models import Card, Deck
from apps.flashcard.serializers import (
    CardSerializer,
    DeckByUserSerializer,
    DeckSerializer,
    UserSerializer,
    CardsByDeckSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        user = serializer.save()
        return user


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get"]


class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DecksByUserViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Deck.objects.filter(user_id=self.kwargs["pk"])
        return queryset

    serializer_class = DeckByUserSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardsByDeckViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Card.objects.filter(deck_id=self.kwargs["pk"])
        return queryset

    serializer_class = CardsByDeckSerializer
