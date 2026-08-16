from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    food_name = serializers.ReadOnlyField(source="food.name")

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "food",
            "food_name",
            "quantity",
            "price",
        ]
        read_only_fields = [
            "id",
            "food_name",
            "price",
        ]

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError(
                "Quantity must be at least 1."
            )

        return value


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(
        many=True
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "total_price",
            "created_at",
            "items",
        ]
        read_only_fields = [
            "id",
            "total_price",
            "created_at",
        ]

    def validate(self, attrs):
        items = attrs.get("items")

        if not items:
            raise serializers.ValidationError(
                "Order must contain at least one item."
            )

        return attrs

    def create(self, validated_data):
        items_data = validated_data.pop("items")

        request = self.context["request"]

        order = Order.objects.create(
            user=request.user,
            total_price=0
        )

        total = 0

        for item_data in items_data:
            food = item_data["food"]
            quantity = item_data["quantity"]

            price = food.price
            subtotal = price * quantity

            OrderItem.objects.create(
                order=order,
                food=food,
                quantity=quantity,
                price=price
            )

            total += subtotal

        order.total_price = total
        order.save()

        return order