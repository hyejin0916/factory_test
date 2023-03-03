
from django.urls import path

from .views import SecondFactoryAPIView,SecondFactorySelectAPIView


urlpatterns = [
    path('second-factories/',SecondFactoryAPIView.as_view()),
    path('second-factories-select/<int:pk>', SecondFactorySelectAPIView.as_view()),
]