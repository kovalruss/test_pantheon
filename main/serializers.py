from rest_framework import serializers


# noinspection PyAbstractClass
class MadlibRetrieveResponseSerializer(serializers.Serializer):
    sentence = serializers.CharField(required=True)
