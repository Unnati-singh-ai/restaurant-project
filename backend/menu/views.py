from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Category, Food
from .permissions import IsStaffUser
from .serializers import CategorySerializer, FoodSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]

        return [IsStaffUser()]
