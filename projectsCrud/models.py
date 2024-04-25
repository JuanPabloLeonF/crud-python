from django.db import models
import uuid


class Project(models.Model):
    
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4
    )
    
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    
    tecnology = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )
    
    description = models.TextField(
        blank=False,
        null=False
    )
    
    dateCreated = models.DateTimeField(
        auto_now_add=True
    )