from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(to='Category', on_delete=models.PROTECT, null=True)
    
    
    
    
    def __str__(self) -> str:
        return self.title
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    
    
    
    def __str__(self) -> str:
        return self.name
    
    
    
    
    