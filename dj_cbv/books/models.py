from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse

def get_unique_slug(model_instance, slugable_field_name, slug_field_name):
    """
    Takes a model instance, sluggable field name (such as 'title') of that
    model as string, slug field name (such as 'slug') of the model as string;
    returns a unique slug as string.
    """
    slug = slugify(getattr(model_instance, slugable_field_name))
    unique_slug = slug
    extension = 1
    ModelClass = model_instance.__class__

    while ModelClass._default_manager.filter(
        **{slug_field_name: unique_slug}
    ).exists():
        unique_slug = '{}-{}'.format(slug, extension)
        extension += 1

    return unique_slug


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50,blank=True, null=True)
    city = models.CharField(max_length=60,blank=True, null=True)
    state_province = models.CharField(max_length=30,blank=True, null=True)
    country = models.CharField(max_length=50,blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.CASCADE, related_name="book_add")
    title = models.CharField(max_length=240)
    description = models.TextField()
    slug = models.SlugField(blank=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False,auto_now=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,null=True,blank=True)

    def save(self,*args,**kwargs):
        print("save")
        if not self.slug:
            print("not self slug")
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail",kwargs={'slug':self.slug})

    class Meta:
        ordering = ["created_at"]

def before_save(sender,instance,*args,**kwargs):
    print("before")

def after_save(sender,instance,created,*args,**kwargs):
    print("after")


pre_save.connect(before_save,sender=Book)
post_save.connect(after_save,sender=Book)