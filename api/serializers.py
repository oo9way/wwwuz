from rest_framework.serializers import ModelSerializer
from app.models import Website, Visitor, Data, Category
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)


class CategorySerializer(ModelSerializer): 
    class Meta:
        model = Category
        fields = '__all__'


class WebsiteSerializer(ModelSerializer):
    owner = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Website
        fields = '__all__'