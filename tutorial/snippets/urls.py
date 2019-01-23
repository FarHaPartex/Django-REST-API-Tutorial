from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns 
from .views import snipper_list, snipper_details

urlpatterns = [
    path('snippets/', snipper_list),
    path('snippets/<int:pk>/', snipper_details),
]


urlpatterns = format_suffix_patterns(urlpatterns)