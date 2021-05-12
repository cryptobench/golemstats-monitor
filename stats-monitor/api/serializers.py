from rest_framework import serializers
from collector.models import ResponseLog


class ResponseLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResponseLog
        fields = ['Url', 'ResponseTime', 'ResponseCode', 'queried_at', ]
