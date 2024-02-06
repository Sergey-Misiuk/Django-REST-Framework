from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action


from .serializers import PostSerializers
from .models import Post, Category



# class PostAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers



class PostViewSet(viewsets.ModelViewSet):
    # queryset = Post.objects.all()
    serializer_class = PostSerializers


    def get_queryset(self):
        pk = self.kwargs.get('pk')
        
        if not pk:
            return Post.objects.all()[:4]
        else:
            return Post.objects.filter(pk=pk)


    @action(methods=['get'], detail=False)
    def category(self,request):
        cats = Category.objects.all()
        return Response({'category': [c.name for c in cats]})


# class PostViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

# class PostAPIList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers


# class PostAPIUpdate(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
    
    
# class PostAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers





# class PostAPIView(APIView):
#     def get(self,request):
#         lst = Post.objects.all()
#         return Response({'posts': PostSerializers(lst, many=True).data})
    
    
#     def post(self,request):
#         serializer = PostSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
        
#         serializer.save()
        
#         return Response({'post': serializer.data})
    
    
#     def put(self,request,*args, **kwargs):
#         pk = kwargs.get('pk', None)
        
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
        
        
#         try:
#             instance = Post.objects.get(pk=pk)
        
#         except:
#             return Response({'error': 'Object does not exists'})
        
#         serializer = PostSerializers(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         return Response({'post': serializer.data})
    
    
    
#     def delete(self,request,*args, **kwargs):
#         pk = kwargs.get('pk', None)
        
#         if not pk:
#             return Response({'error': 'Method DELETE not allowed'})
        
        
#         post = Post.objects.get(pk=pk)
#         post.delete()
        
#         return Response({'post': f'delete post {str(pk)}'})
