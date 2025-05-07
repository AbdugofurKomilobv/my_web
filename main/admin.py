from django.contrib import admin

from main.models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'project_url','image')