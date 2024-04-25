from rest_framework import viewsets, permissions
from projectsCrud import models, serializers

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = serializers.ProjectSerializer