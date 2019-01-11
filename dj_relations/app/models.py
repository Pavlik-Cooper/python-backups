from django.db import models
from django.db.models import Q
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your models here.

# django.contrib.auth.models.User

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Only one profile with a particular user. The user can be changed
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


def set_delete_user(*args,**kwargs):
    User = get_user_model()
    return User.objects.get_or_create(username="unknown", is_staff=True)[0]


class Article(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.SET(set_delete_user),
        limit_choices_to={"is_staff": True}
    )
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        if self.author.username.endswith("s"):
            return f"{self.author.username}' article"
        return f"{self.author.username}'s article"


# paul = User.objects.get(username__iexact="paul")
# articles = paul.article_set.all()

def limit_drivers():
    return Q(username__startswith="p") | Q(username__startswith="j") | Q(username__startswith="r")


class Car(models.Model):
    drivers = models.ManyToManyField(User, limit_choices_to=limit_drivers)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="updated_car_set", null=True, blank=True)
    # paul = User.objects.get(username="paul")
    # paul_cars = paul.updated_car_set.all()

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# paul = User.objects.get(username="paul")
# paul_cars = paul.updated_car_set.all()

# paul_cars = Car.objects.filter(updated_by__username="paul")

# jane = User.objects.get(username__iexact="jane")
# jane_cars = jane.car_set.all()  # or jane_cars = Car.objects.filter(drivers=jane)
#
# ferrari = jane_cars.get(name__iexact="ferrari")
# ferrari_drivers = ferrari.drivers.all()
#
# another_cars_of_ferrari_drivers = Car.objects.filter(drivers__in=ferrari_drivers).distinct()
