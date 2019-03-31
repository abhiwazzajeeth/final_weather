from django.urls import path, include
from . import views
from weatherapi.views import DateViewSet, ForecastViewSet, DateListViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

date_list = DateListViewSet.as_view({'get':'list', 'post':'create'})

date_detail = DateViewSet.as_view(
	{
		'get':'retrieve',
		'put' : 'update',
		'patch' : 'partial_update',
		'delete' : 'destroy'
	})

router = DefaultRouter()
router.register(r'forecast', views.ForecastViewSet)

urlpatterns = [
	path('historical/', date_list, name='date-list'),
	path('historical/<int:pk>/', date_detail, name='date-detail'),
	path('', include(router.urls)),
	]