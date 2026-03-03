from django.contrib import admin
from .models import ProjectCategory, Project

class ProjectInline(admin.TabularInline):
    model = Project

class ProjectCategoryAdmin(admin.ModelAdmin):
    model = ProjectCategory
    inlines = [ProjectInline]

class ProjectAdmin(admin.ModelAdmin):
    model = Project

admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(ProjectAdmin, ProjectAdmin)