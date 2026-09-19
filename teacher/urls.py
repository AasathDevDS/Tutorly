from django.urls import path,include
from .views import TeacherViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("" , TeacherViewSet ,  basename="teacher")

urlpatterns = [
    path("" , include(router.urls)),
]

