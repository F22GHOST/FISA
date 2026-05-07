from django.contrib import admin
from .models import Employee, Rank, Division

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['roleplay_name', 'callsign', 'rank', 'is_hrt']
    list_filter = ['rank', 'divisions', 'is_hrt']
    search_fields = ['roleplay_name', 'callsign', 'roblox_username', 'discord_username']

@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ['name', 'level']
    ordering = ['-level']

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name']