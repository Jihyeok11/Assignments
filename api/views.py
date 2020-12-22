from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serialziers import PersonSerializer
from .models import Person
from rest_framework import permissions
from rest_framework.decorators import api_view
# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def ge
 
# class PersonView(viewsets.ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#     permission_classes = (permissions.IsAuthenticated,)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)