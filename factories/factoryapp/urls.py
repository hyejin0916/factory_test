
from django.urls import path

from .views import FactoryAPIView,FactorySelectAPIView


urlpatterns = [
    path('factories/',FactoryAPIView.as_view()),
    path('factories-select/<int:pk>', FactorySelectAPIView.as_view()),
]