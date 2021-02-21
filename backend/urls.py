from django.urls import path
from django.conf import settings
from backend.djangoapps.main.views import UserViewSet
urlpatterns = [
    path("v1/user", UserViewSet.as_view({"get": "list", "post": "add"}), name="user"),
    # path("v1/music/<int:music_num>", UserViewSet.as_view({"get": "list"}), name="music"),
]