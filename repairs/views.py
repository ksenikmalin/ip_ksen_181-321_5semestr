from django.shortcuts import render
from django.views.generic.base import View

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ServicesListSerializer, ServicesDetailSerializer
from .models import Services

Services
class ServicesView(View):
    def get(self, request):
        services = Services.objects.all()
        return render(request, "service_list.html", {"service_list": services})


class ServicesListAPIView(APIView):
    def get(self, request):
        services = Services.objects.all()
        serializer = ServicesListSerializer(services, many=True)
        return Response(serializer.data)


class ServicesDetailView(View):
    def get(self, request, pk):
        service = Services.objects.get(id=pk)
        return render(request, "service_detail.html", {"service": service})


class ServicesDetailAPIView(APIView):
    def get(self, request, pk):
        service = Services.objects.get(id=pk)
        serializer = ServicesDetailSerializer(service)
        return Response(serializer.data)
