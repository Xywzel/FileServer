
def create():
    print("Importing the models")
    from files.models import Profile, Organization, Upload, DownloadRecord
    from django.contrib.auth.models import User

    print("Creating some organizations")
    org1 = Organization.objects.create(name="Hosts")
    org2 = Organization.objects.create(name="TheClient")
    org3 = Organization.objects.create(name="OtherClient")
    print(Organization.objects.all().values())

    print("Creating some users")
    userS = User.objects.create(username="admin", is_superuser=True, is_staff=True)
    userS.set_password("password")
    userS.save()
    user1 = User.objects.create(username="Sami")
    user1.set_password("apina")
    user1.save()
    user2 = User.objects.create(username="Pena")
    user2.set_password("omena")
    user2.save()
    user3 = User.objects.create(username="Matti")
    user3.set_password("horse_stable_battery_correct")
    user3.save()
    print(User.objects.all().values())

    print("Creating some profiles")
    Profile.objects.create(user=userS, organization=org1)
    Profile.objects.create(user=user1, organization=org1)
    Profile.objects.create(user=user2, organization=org2)
    Profile.objects.create(user=user3, organization=org3)
    print(Profile.objects.all().values())
