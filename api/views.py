from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serialziers import PersonSerializer
from .models import Person
from rest_framework import permissions
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def tutorial_list(request):
    queryset = Person.obejcts.all()
    serializer_class = PersonSerializer

    persons_serializer = PersonSerializer(queryset)
    return JsonResponse(persons_serializer, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
# class PersonView(viewsets.ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#     permission_classes = (permissions.IsAuthenticated,)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)