from django.contrib import admin
from devsearch_01.core.models import Account, Skill, Tool, Image, Project


admin.site.register(Skill)
admin.site.register(Tool)




@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):     
    list_display = ('user', 'title', 'about', 'link', )

    
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):     
    list_display = ('user', 'name', 'title', 'about', 'profile_image', 'location', )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):     
    list_display = ('project_author' , 'project_title' , 'file', )

    def project_title(self, obj):
        return obj.project.title

    def project_author(self, obj):
        return obj.project.user.username
    
    # Add description to the field
    project_title.description = "Project Title"
    project_author.description = "User"
    
