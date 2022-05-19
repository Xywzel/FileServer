from django.contrib.auth.models import User
from rest_framework import serializers
from files.models import Profile, Organization, Upload, DownloadRecord

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['url', 'user', 'organization', 'uploads', 'records']

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ['url', 'name', 'download_count', 'members', 'org_uploads', 'records']

class UploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'

class DownloadRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DownloadRecord
        fields = '__all__'

