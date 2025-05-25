from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import token_obtain_pair 
from apps.flashcard.views import (
    CardViewSet,
    CardsByDeckViewSet,
    DeckViewSet,
    DecksByUserViewSet,
    RegisterView,
    UserViewSet,
)

router = routers.DefaultRouter()
router.register("decks", DeckViewSet)
router.register("cards", CardViewSet)
router.register("users", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/login/", token_obtain_pair, name="api_token_auth"),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path("api/", include(router.urls)),
    path("api/users/<int:pk>/decks/", DecksByUserViewSet.as_view()),
    path("api/decks/<int:pk>/cards/", CardsByDeckViewSet.as_view()),
]
