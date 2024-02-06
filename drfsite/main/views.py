from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response



from .serializers import PostSerializers
from .models import Post



# class PostAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers



class PostAPIList(generics.ListCreateAPIView):
    pass


class PostAPIView(APIView):
    def get(self,request):
        lst = Post.objects.all()
        return Response({'posts': PostSerializers(lst, many=True).data})
    
    
    def post(self,request):
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response({'post': serializer.data})
    
    
    def put(self,request,*args, **kwargs):
        pk = kwargs.get('pk', None)
        
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        
        
        try:
            instance = Post.objects.get(pk=pk)
        
        except:
            return Response({'error': 'Object does not exists'})
        
        serializer = PostSerializers(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'post': serializer.data})
    
    
    
    def delete(self,request,*args, **kwargs):
        pk = kwargs.get('pk', None)
        
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})
        
        
        post = Post.objects.get(pk=pk)
        post.delete()
        
        return Response({'post': f'delete post {str(pk)}'})
