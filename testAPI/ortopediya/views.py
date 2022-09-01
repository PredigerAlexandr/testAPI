from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


# Create your views here.

class OrtopediyaApiView(APIView):
    def get(self, request):
        products = Product.objects.all().values()
        return Response({'products': ProductSerializer(products, many=True).data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            Response({"error":"Method put not allowed"})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            Response({"error":"Objects does not exists"})

        serializer = ProductSerializer(data=request.data,instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            Response({"error": "Method put not allowed"})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            Response({"error": "Objects does not exists"})

        instance.delete()
        return Response({"post": "delete product: " + str(pk)})

# class OrtopediyaApiView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
