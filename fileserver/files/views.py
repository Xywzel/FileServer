from django import forms
from django.http import FileResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status

from files.models import Profile, Organization, Upload, DownloadRecord
from files.serializers import ProfileSerializer, OrganizationSerializer, UploadSerializer, DownloadRecordSerializer, UserSerializer

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

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILE)
        if form.is_valid():
            pass
            # Get profile for the user
            # Get organization for the user
            # Get the file from the form
            # Upload.objects.create(profile=profile, organization=organization, data=file)
    else:
        form = UploadFileForm()
    return None

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

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

# class 
