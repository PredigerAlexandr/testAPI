from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.IntegerField()
    image = serializers.CharField()
    art = serializers.CharField(max_length=50, default=0)
    subcategory_id = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.image = validated_data.get("image", instance.price)
        instance.art = validated_data.get("art", instance.art)
        instance.subcategory_id = validated_data.get("subcategory_id", instance.subcategory_id)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return "Product delet: ", str(instance.pk)

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields=('name', 'description')