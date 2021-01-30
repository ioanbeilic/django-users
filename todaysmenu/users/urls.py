from django.urls import path
from users.views import UserAPIView, UserDetailAPIView


urlpatterns = [
    path('', UserAPIView.as_view(), name="users"),
    path('<int:pk>/', UserDetailAPIView.as_view(), name="user"),
]
