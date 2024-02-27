from rest_framework import serializers

from app_edu.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super().__init__(*args, **kwargs)
        if remove_fields:
            for field_name in remove_fields:
                self.fields.pop(field_name)

    class Meta:
        model = Subscription
        fields = '__all__'
