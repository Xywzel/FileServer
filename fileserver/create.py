
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
    p = Profile(user=user1, organization=org1)
    p.save()
    p = Profile(user=user2, organization=org2)
    p.save()
    p = Profile(user=user3, organization=org3)
    p.save()
    print(Profile.objects.all().values())
