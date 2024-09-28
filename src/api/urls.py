from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

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
    path("api/auth/login/", obtain_auth_token, name="api_token_auth"),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path("api/", include(router.urls)),
    path("api/users/<int:pk>/decks/", DecksByUserViewSet.as_view()),
    path("api/decks/<int:pk>/cards/", CardsByDeckViewSet.as_view()),
]
