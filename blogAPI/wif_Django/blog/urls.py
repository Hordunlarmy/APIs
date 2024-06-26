from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from user import views

router = routers.DefaultRouter()
router.register(r'users', views.SignUpViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
