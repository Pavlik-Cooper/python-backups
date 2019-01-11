from django.contrib import admin
# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'body',
        'author',
        'status',
        'featured',
        'age',
        'publish_date',
        'custom_field',
        'created_at',
        'updated_at'
    ]
    readonly_fields = [
        'created_at',
        'updated_at',
        'custom_field',
        'age'
    ]
    def custom_field(self,obj,*args,**kwargs):
        return obj.title

    def age(self,obj,*args,**kwargs):
        return obj.age


# admin.site.register(Post)
admin.site.register(Post, PostAdmin)