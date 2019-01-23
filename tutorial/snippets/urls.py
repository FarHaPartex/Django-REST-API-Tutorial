from django.urls import path,include
from .views import snipper_list, snipper_details

urlpatterns = [
    path('snippets/', snipper_list),
    path('snippets/<int:pk>/', snipper_details),
]