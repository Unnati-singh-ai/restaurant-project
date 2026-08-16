from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import MethodNotAllowed

from .models import Order
from .serializers import OrderSerializer
from menu.permissions import IsStaffUser


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()

        return Order.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "partial_update"]:
            return [IsStaffUser()]

        if self.action == "destroy":
            return [IsStaffUser()]

        return [IsAuthenticated()]

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE")