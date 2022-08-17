from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from user_operation.models import UserFav


class UserFavSerializers(serializers.ModelSerializer):

    user = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserFav
        fields = "__all__"

        validators = [
            UniqueTogetherValidator(queryset=UserFav.objects.all(), fields=("user","goods"), message="已经收藏")
        ]
