from rest_framework import serializers
from products.models import Products,Tag,Review
from users.models import Profile


class ReviewSerializer(serializers.ModelSerializer):
    class  Meta:
        model=Review
        fields='__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class  Meta:
        model=Profile
        fields='__all__'


class TagSerializer(serializers.ModelSerializer):
    class  Meta:
        model=Tag
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    owner=ProfileSerializer(many=False)
    tags=TagSerializer(many=True)
    reviews=serializers.SerializerMethodField()

    class  Meta:
     model= Products
     fields='__all__'

    def get_reviews(self,obj):
        reviews=obj.review_set.all()
        serializer=ReviewSerializer(reviews,many=True)
        return serializer.data
