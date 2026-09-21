from django.urls import path,include
from .views import ClassBatchViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ClassBatchViewSet , basename = 'class')

urlpatterns = [
    path('', include(router.urls))
]
