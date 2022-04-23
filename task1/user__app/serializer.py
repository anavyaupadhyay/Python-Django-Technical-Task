from rest_framework import serializers
from user__app.models import user_model, customer_model

class user_serializers(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = ['id', 'first_name', 'last_name', 'email', 'mob_no']


class customer_serializers(serializers.ModelSerializer):
    class Meta:
        model = customer_model
        fields = ['id', 'profile_no']