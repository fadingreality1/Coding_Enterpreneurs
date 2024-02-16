from rest_framework.routers import DefaultRouter

from api.viewsets import *

router = DefaultRouter()

router.register('Books-testing', BookViewSet, basename='books')

urlpatterns = router.urls