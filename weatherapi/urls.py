from django.urls import path, include
from . import views
from weatherapi.views import DateViewSet, ForecastViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('historical', views.DateViewSet)
router.register('forecast', views.ForecastViewSet)
urlpatterns = [
	path('', include(router.urls)),
]