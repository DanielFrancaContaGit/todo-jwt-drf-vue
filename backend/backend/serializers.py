from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            is_staff=validated_data["is_staff"],
            email=validated_data["email"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user

    class Meta:
        model = User
        fields = ["password", "email", "username", "is_staff", "id"]
