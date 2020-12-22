from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PersonView

person_list = PersonView.as_view({
    'post': 'create',
    'get': 'list'
})
person_detail = PersonView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('persons/', person_list, name='person_list'),
    path('persons/<int:pk>/', person_detail, name='person_detail'),
])