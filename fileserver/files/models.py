from django.db import models
from django.contrib.auth.models import User

# As the default group model is practically only for permission
# handling, so better make a different model for the organizations
class Organization(models.Model):
    name = models.CharField(max_length=255)
    download_count = models.IntegerField(default=0)

# For base user needs we use the build-in user model,
# https://docs.djangoproject.com/en/4.0/ref/contrib/auth/
# This extension allows us to add the organizatio
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

# This handles the actual files
class Upload(models.Model):
    name = models.CharField(max_length=255)
    # User that uploaded this file
    profile = models.ForeignKey(Profile, models.CASCADE)
    # Organization that the uploading user belonged to at the time
    organization = models.ForeignKey(Organization, models.CASCADE)
    # Total download count of the file
    download_count = models.IntegerField(default=0)
    # The actual file
    data = models.FileField(upload_to='uploads/%Y-%m-%d/', null=True)

# A way of keeping track of the downloads, while total download counts
# can be stored in the file/user/org models, we can't do per file in
# user or org as that would require database entry column for each file.
class DownloadRecord(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    upload = models.ForeignKey(Upload, models.CASCADE)
    organization = models.ForeignKey(Organization, models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
