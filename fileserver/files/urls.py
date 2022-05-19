from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'profile', views.ProfileViewSet)
router.register(r'organization', views.OrganizationViewSet)
router.register(r'upload', views.UploadViewSet)
router.register(r'record', views.DownloadRecordViewSet)

urlpatterns = [
    path('files/', include(router.urls)),
    path('download/<path:filepath>', views.download),
    path('upload/', views.upload),
    path('api/', include('rest_framework.urls', namespace="rest_framework")),
]
