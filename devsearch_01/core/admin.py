from django.contrib import admin
from devsearch_01.core.models import Account, Skill, Tool, Image, Project


admin.site.register(Skill)
admin.site.register(Tool)


# the intermediate table generated for the many-to-many relationship between Project and Image.
class ImageInline(admin.TabularInline):
    model = Project.image_project.through 


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):     
    list_display = ('user', 'title', 'about', 'link', )
    # inlines = [ImageInline]
    
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):     
    list_display = ('user', 'name', 'title', 'about', 'profile_image', 'location', )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):     
    list_display = ('file', )
    
