import io
from rest_framework import serializers
from .models import Post
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# class PostModel:
#     def __init__(self, title, content) -> None:
#         self.title = title
#         self.content = content






# class PostSerializers(serializers.Serializer):
    # title = serializers.CharField(max_length=255)
    # content = serializers.CharField()    
    # time_create = serializers.DateTimeField(read_only=True)
    # time_update = serializers.DateTimeField(read_only=True)
    # is_published = serializers.BooleanField(default=True)
    # category_id = serializers.IntegerField()
    
    
    # def create(self, validated_data):
    #     return Post.objects.create(**validated_data)
    
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.time_update = validated_data.get('time_update', instance.time_update)
    #     instance.is_published = validated_data.get('is_published', instance.is_published)
    #     instance.category_id = validated_data.get('category_id', instance.category_id)
        
    #     instance.save()
    #     return instance




class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields= ['title','content','category']
        fields = "__all__"
    
    
    
# def encode():
#     model = PostModel('Nasa starting to develop a new thing for about planet', 'wsjgifelrjegkrhgkearjhgkearughkhugkearuh')
#     models_sr = PostSerializers(model)
#     print(models_sr.data, type(models_sr.data),sep='\n')
    
#     json = JSONRenderer().render(models_sr.data)
#     print(json)
    
    
    
# def decode():
#     stream = io.BytesIO(b'{"title":"Nasa starting to develop a new thing for about planet","content":"wsjgifelrjegkrhgkearjhgkearughkhugkearuh"}')
#     data = JSONParser().parse(stream)
    
#     serializer =  PostSerializers(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
    
    
    