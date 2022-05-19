from django.contrib.auth.models import User
from rest_framework import serializers
from files.models import Profile, Organization, Upload, DownloadRecord

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'organization']

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class UploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'

class DownloadRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DownloadRecord
        fields = '__all__'

