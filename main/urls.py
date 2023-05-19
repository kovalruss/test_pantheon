from django.urls import path

from main.views import MadlibAPIView

urlpatterns = [
    path(
        "madlib",
        MadlibAPIView.as_view(),
        name="madlib",
    ),
]
