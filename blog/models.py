from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
STATUS = (
	(0,"Draft"),
	(1,"Publish")
)

class blog_article(models.Model):
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	content = models.TextField(null=2)
	updated_on = models.DateTimeField(auto_now= True)
	status = models.IntegerField(choices=STATUS, default=0)
	author = models.ForeignKey('Author',on_delete= models.CASCADE, related_name='articles',null= 1)
	
	def __str__(self):
		return self.title 


class author(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()

	def __str__(self):
		return self.name 
