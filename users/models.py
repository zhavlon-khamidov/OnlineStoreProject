from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_profile(instance:User,created,**kwargs):
    print("create/update user")
    if created:
        print("created")
        Profile.objects.create(
            user=instance,name=instance.first_name,email=instance.email)
    else:
        instance.profile.name = instance.first_name
        instance.profile.email = instance.email
        instance.profile.save()


@receiver(post_save, sender=Profile)
def profile_created(instance,created,**kwargs):
    print("Profile created")
    if created:
        instance.name = instance.user.first_name
        instance.email = instance.user.email