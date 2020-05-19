from django.urls import path

from .views import LessonsView

urlpatterns = [
    path('', LessonsView.as_view())
]
