from rest_framework import routers
from projectsCrud import api

router = routers.DefaultRouter()  

router.register(r'projects', api.ProjectViewSet, "projects")

urlpatterns = router.urls