from .models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    #model serializer
    class Meta:
        model = Article
        fields = '__all__'

    

    """
    #normal serializer
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=20)
    date = models.DateTimeField(auto_now_add = True)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)
      
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author_name = validated_data.get('author_name', instance.author_name)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

    """


       


