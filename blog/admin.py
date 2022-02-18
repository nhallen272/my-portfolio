from django.contrib import admin
from blog.models import Category, Project, Subscriber
# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Subscriber, SubscriberAdmin)