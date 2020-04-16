from rest_framework import serializers
from .models import blog_article

class BlogSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return blog_article.objects.create(**validated_data)

    def update(self, instance, validated_data):
    	
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance

    class Meta:
        fields = ('id', 'title', 'content','author_id', 'created_on','status','updated_on')
        model = blog_article

    