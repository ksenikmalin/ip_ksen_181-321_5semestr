from rest_framework import serializers

from .models import Services


class ServicesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ("naimenovaniye", "id_repair_type", "id_object", "id_duration")


class ServicesDetailSerializer(serializers.ModelSerializer):
    id_repair_type = serializers.SlugRelatedField(slug_field="naimenovaniye", read_only=True)

    class Meta:
        model = Services
        exclude = ("")
