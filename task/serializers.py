from rest_framework import serializers

from . import models


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ['pk', 'name']

class