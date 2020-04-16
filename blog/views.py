from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import generic
from .models import blog_article
from .serializers import BlogSerializer 

# Create your views here.
class ArticleListView(generic.ListView):
	
	model = blog_article
	template_name = 'index.html'

class ArticleDetailView(generic.DetailView):
	model = blog_article
	template_name = 'detail.html'


class BlogApiView(APIView):
	def get(self,request,pk):
		articles = blog_article.objects.all()
		serializer = BlogSerializer(articles, many=True)
		return Response({"articles":serializer.data})

	def post(self,request):
		article = request.data.get('articles')
		serializer = BlogSerializer(data = article)
		if serializer.is_valid(raise_exception=True):
			article_saved = serializer.save()
		return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

	def put(self, request, pk):
		
		snippet = blog_article.objects.get(id=pk)
		serializer = BlogSerializer(instance=snippet, data= request.data.get('articles'))
		
		if serializer.is_valid(raise_exception=True):
			article_saved = serializer.save()
		
		return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})

	def delete(self, request, pk):
	# Get object with this pk
		snippet = blog_article.objects.get(id=pk)
		serializer = BlogSerializer(instance=snippet, data= request.data.get('articles'))
		
		snippet.delete()
		return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)

