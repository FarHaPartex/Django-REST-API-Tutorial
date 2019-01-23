from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns 
from .views import Snippet_List, Snipper_Details

urlpatterns = [
    path('snippets/', Snippet_List.as_view()),
    path('snippets/<int:pk>/', Snipper_Details.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)