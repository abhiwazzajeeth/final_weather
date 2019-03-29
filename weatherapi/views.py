from weatherapi.models import WeatherAPI
from weatherapi.serializers import WeatherSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets, permissions
from datetime import timedelta, datetime
import random
class DateViewSet(viewsets.ModelViewSet):
	queryset = WeatherAPI.objects.all()
	serializer_class = WeatherSerializer
	permission_classes = [
	permissions.AllowAny
	]

class ForecastViewSet(viewsets.GenericViewSet):
	queryset = WeatherAPI.objects.all()
	serializer_class = WeatherSerializer
	def retrieve(self, request, pk=None):
		startDate = datetime(int(pk[:4]), int(pk[4:6]), int(pk[6:]))
		response = []
		newdata = {}
		for i in range(7):
			currDate = (startDate + timedelta(days = i)).strftime("%Y%m%d")
			serializer = self.get_serializer(WeatherAPI.objects.all().filter(DATE = currDate), many = True)
			if len(serializer.data)==0:
				TMAX = round(random.uniform(50, 100), 2)
				TMIN = round(random.uniform(2, 50), 2)
				newdata ={"DATE" : currDate, "TMAX" : TMAX, "TMIN" : TMIN} 
				response.append(newdata)
			else:
				newdata = serializer.data
				response.append(newdata[0])	
		return Response(response)