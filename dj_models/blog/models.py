from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from django.utils.timesince import timesince
from django.utils.text import slugify
from django.db.models.signals import pre_save,post_save,pre_delete, post_delete
import datetime
from datetime import timedelta
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField(null=True)


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status='published')

    def featured(self):
        return self.filter(featured=True)

    def starts_with(self, start):
        return self.filter(title__istartswith=start)

    def time_frame(self, start_date=datetime.datetime(2015,1,1), end_date=datetime.datetime(2017,11,10)):
        # inclusive
        # start_date = datetime.datetime.combine(start_date, datetime.time.min, tzinfo=timezone.utc)
        # end_date = datetime.datetime.combine(end_date, datetime.time.max, tzinfo=timezone.utc)

        # exclusive
        start_date = datetime.datetime(2015, 1, 1, tzinfo=timezone.utc)
        end_date = datetime.datetime(2017,11,10, tzinfo=timezone.utc)
        return self.filter(publish_date__range=(start_date, end_date))
        # return self.filter(publish_date__gte=start_date, publish_date__lt=end_date)

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)
        # return super().get_queryset().filter(status='published')

    def all(self):
        return self.get_queryset()


class Post(models.Model):

    # objects = models.Manager()
    objects = PostManager()
    statuses = (
        ('draft','Draft'),
        ('published','Published'),
        ('active','Active')
    )

    id = models.BigAutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=250,unique=True, error_messages={
        "unique": "The post with this title already exists, pick another",
        "required": "You have to fill this field"
    }, help_text="Must be unique value")

    slug = models.CharField(max_length=250,null=True,blank=True)
    featured = models.BooleanField(default=True)
    status = models.CharField(max_length=10,choices=statuses,default=statuses[1])
    body = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    author_email = models.CharField(editable=False, max_length=240, null=True,blank=True, validators=[])
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return smart_text(self.title)

    @property
    def age(self):
        # now = datetime.now(timezone.utc)   #  works in django and without it
        now = timezone.now()  # works only in django

        difference = now - self.publish_date
        if difference <= timedelta(minutes=1):
            return "just now"
        return "{} ago".format(timesince(self.publish_date))


def before_save(sender, instance, *args,**kwargs):
    print("before save")
    if not instance.slug:
        instance.slug = slugify(instance.title)

def after_save(sender, instance, created, *args,**kwargs):
    print("after save")
    print(instance.slug)
    # if not instance.slug:
    #     instance.slug = slugify(instance.title)
    #     instance.save()



# events

pre_save.connect(before_save,sender=Post)
post_save.connect(after_save,sender=Post)