from rest_framework import serializers
from projectsCrud import models

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ("id", "title", "tecnology", "description", "dateCreated")
        read_only_fields = ("id", "dateCreated")
