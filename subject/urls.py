from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet
from django.urls import path,include

router = DefaultRouter()
router.register("", SubjectViewSet , basename='subject')

urlpatterns = [
    path('' , include(router.urls)),
]
