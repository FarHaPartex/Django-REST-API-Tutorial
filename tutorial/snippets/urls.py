from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns 
from .views import Snippet_List, Snipper_Details,UserList,UserDetail

urlpatterns = [
    path('snippets/', Snippet_List.as_view()),
    path('snippets/<int:pk>/', Snipper_Details.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)