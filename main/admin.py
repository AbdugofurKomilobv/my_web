from django.contrib import admin

from main.models import Portfolio,ContactMe


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'project_url','image')

@admin.register(ContactMe)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('u_name','email','subject','phone','message','created_at','updated_at')