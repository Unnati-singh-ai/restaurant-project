from rest_framework import serializers
from .models import Category, Food


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class FoodSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    class Meta:
        model = Food
        fields = [
            "id",
            "name",
            "description",
            "price",
            "image",
            "category",
            "category_name",
            "is_available",
            "created_at",
            "updated_at",
        ]