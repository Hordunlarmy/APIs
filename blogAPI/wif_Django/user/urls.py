from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.SignUpView.as_view(), name="user-sign-up"),
]
