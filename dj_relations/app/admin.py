from django.contrib import admin

# Register your models here.
from .models import Car, Profile, Article


class CarAdmin(admin.ModelAdmin):
    search_fields = ['drivers__username','drivers__email','drivers__id']
    # raw_id_fields = ['drivers']
    readonly_fields = ['updated_by']

    class Meta:
        model = Car

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        obj.save()

    # def get_queryset(self, request):
    #     super().get_queryset(request)



admin.site.register(Car,CarAdmin)
admin.site.register(Profile)
admin.site.register(Article)
