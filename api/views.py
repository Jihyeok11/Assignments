from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import PersonSerializer,GenderSerializer
from .models import Person,Gender
from api import serializers

from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @action(methods=['GET'], detail=True, url_path="genders")
    def person_gender(self, request, *args,**kwargs):
        person = self.get_object()
        serializer_class = serializers.GenderSerializer

        person_gender = Gender.objects.filter(person=person)

        serializer = serializer_class(person_gender)
        return Response(serializer.data)

 
# class PersonView(viewsets.ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#     permission_classes = (permissions.IsAuthenticated,)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)