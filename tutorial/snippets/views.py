from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer,UserSerializer
from rest_framework import status , mixins, generics,permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User




class Snippet_List(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self,serializer_class):
        serializer_class.save(owner=self.request.user)



class Snipper_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class Snippet_List(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
    
#     def get(self,request,*args,**kargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self,request,*args,**kargs):
#         return self.create(request, *args, **kwargs)
    


# class Snipper_Details(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,
#                 generics.GenericAPIView):

#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

    # def get_object(self,pk):
    #     try:
    #         snippet = Snippet.objects.get(pk=pk)
    #     except snippet.DoesNotExit:
    #         return Response(status=status.HTTP_400_NOT_FOUND)

    # def get(self,request,pk,format=None):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet)
    #     return Response(serializer.data)
    
    # def put(self,request,pk,format=None):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet,data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self,request,pk,format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
