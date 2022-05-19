# FileServer

Recruitment task of file sharing REST API using Django

The assignment was as follows:

'''
Please write a web application that provides a REST API for logged-in users
to upload and download any kind of files.

The users must be able to login and logout (use either token or session
authentication). There is no need to implement CRUD endpoints for users or
organizations, those can be created by running a script.

Each user and file must belong to an organization. Once uploaded, the file must
belong to the same organization as the user who uploaded it.

Users should see and be able to download any of the uploaded files from any
organization. Write an endpoint for listing all the files that belong to one
organization, and an endpoint for listing all the file downloads done by one
user. Include timestamps when the file was uploaded and when the user downloaded
a file.

Keep track of how many times each file has been downloaded, and also how many
total file downloads each organization has (number of all file downloads from
that organization). Include the number of downloads when listing files and
organizations.

Use Django and Django REST Framework (https://www.django-rest-framework.org/).
You can use a database of your choice.

No need to implement the UI, writing the API endpoints is enough.
'''

## Scripts

- *setup.sh* makes initial setup of the environment
- *clean.sh* removes existing databases and migrations, allowing starting
  testing from clean slate. It also runs *create.py* that initializes some
  organizations and users with their profiles
- *start.sh* runs the development server in its virtual environment

## Implementation

- */files/* is root for the API
- Users are handled with django auth User model, extended with Profile model.
  Profiles can be queried through */files/profile/*.
- Organizations can be queried trough */files/organization/*.
  Organizations track their total download count.
- Files can be queried trough *files/upload/*, the serialised format include a
  download link for the file in data field. Name is upload, because file is too
  overloaded word in python and django context. Uploads track their total
  download count.
- DownloadRecords allow for more granular tracking of downloads, each recording,
  user, organization, file upload and time of download. With filtering these,
  each of the required views should be possible to display. They can be accessed
  trough */record/*
- The rest API uses hyperlinked references, so other models are referenced by
  a link that fetches information about that model.
- Currently there is no proper way to upload files, way to do it trough form was
  left unfinished and I did have time to find a way to do it trough the
  serialised API. Files can be added trough admin interface *admin/files/upload/add/*.
- There is no consideration of security or privacy currently in the system as
  all information that is visible is so for all logged in users and can likely
  also be edited trough POSTs to the API.

## About the workload

- This took about two work days (~16h) split around 3 days.
- Most of this time was spend reading django and REST framework documentation
  and tutorials.
- Trying to get the database play nicely also took quite a while, and is the
  reason, why my clean up script takes quite drastic measures.

