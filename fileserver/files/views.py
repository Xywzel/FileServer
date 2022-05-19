from django.shortcuts import render
from django.template import loader
from django.http import FileResponse

from rest_framework import viewsets, permissions, status

from files.models import Profile, Organization, Upload, DownloadRecord
from files.serializers import ProfileSerializer, OrganizationSerializer, UploadSerializer, DownloadRecordSerializer

def download(request, filepath):
    # Get the file requested
    file = Upload.objects.get(data=filepath)
    # Get the active user
    user = request.user
    # Superuser doesn't have profile, so this might fail
    profile = Profile.objects.get(user=user)
    org = profile.organization
    # Make a record of this download
    DownloadRecord.objects.create(upload=file, profile=profile, organization=org)
    file.download_count +=1
    file.save()
    org.download_count += 1
    org.save()
    # Count loads in different places
    response = FileResponse(open(filepath, 'rb'))
    return response

def upload(request):
    return None

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
    permission_classes = [permissions.IsAuthenticated]

class DownloadRecordViewSet(viewsets.ModelViewSet):
    queryset = DownloadRecord.objects.all()
    serializer_class = DownloadRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

# Query users
#@api_view
#def users(request):
#    return Responce(None, status=status.HTTP_200_OK)

# Other needed codes
# HTTP_201_CREATED
# HTTP_204_NO_CONTENT
# HTTP_400_BAD_REQUEST
# HTTP_401_UNAUTHORIZED
# HTTP_403_FORBIDDEN
# HTTP_404_NOT_FOUND
