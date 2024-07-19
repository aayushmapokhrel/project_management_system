from django.urls import path
from client.api.views import ClientAPIView, ClientUpdateAPIView

urlpatterns = [
    path("", ClientAPIView.as_view(), name="Client-view"),
    path("<int:pk>", ClientUpdateAPIView.as_view(), name="Client-update"),
]
