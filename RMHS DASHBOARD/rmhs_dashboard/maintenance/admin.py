from django.contrib import admin
from .models import MaintenanceActivity, Spare

@admin.register(MaintenanceActivity)
class MaintenanceActivityAdmin(admin.ModelAdmin):
    list_display = ('date', 'shift', 'maintenance_type', 'maintenance_category', 
                    'area', 'equipment', 'duration_hours', 'is_completed')
    list_filter = ('date', 'shift', 'maintenance_type', 'maintenance_category', 
                   'area', 'equipment', 'is_completed', 'priority')
    search_fields = ('activity_description', 'spares_used', 'remarks', 'equipment_id')
    date_hierarchy = 'date'
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('date', 'shift', 'maintenance_type', 'maintenance_category', 'area', 'equipment', 'equipment_id')
        }),
        ('Activity Details', {
            'fields': ('activity_description', 'spares_used')
        }),
        ('Time Details', {
            'fields': ('start_time', 'end_time', 'duration_hours')
        }),
        ('Status and Priority', {
            'fields': ('priority', 'is_completed', 'completion_time')
        }),
        ('Additional Information', {
            'fields': ('remarks', 'created_by', 'created_at', 'updated_at')
        }),
    )

@admin.register(Spare)
class SpareAdmin(admin.ModelAdmin):
    list_display = ('name', 'part_number', 'quantity_available', 'minimum_stock_level', 
                    'unit_price', 'equipment_type', 'is_low_stock')
    list_filter = ('equipment_type', 'maintenance_type', 'last_restocked_date')
    search_fields = ('name', 'part_number', 'description')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'part_number', 'description')
        }),
        ('Inventory Details', {
            'fields': ('quantity_available', 'minimum_stock_level', 'unit_price', 'last_restocked_date')
        }),
        ('Categorization', {
            'fields': ('equipment_type', 'maintenance_type')
        }),
        ('System Fields', {
            'fields': ('created_at', 'updated_at')
        }),
    ) 