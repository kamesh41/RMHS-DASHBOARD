from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .models import MaintenanceActivity, Spare

@login_required
def maintenance_list(request):
    """List view for maintenance activities"""
    # Get filter parameters
    selected_date = request.GET.get('date', timezone.now().date())
    selected_shift = request.GET.get('shift', '')
    selected_type = request.GET.get('type', '')
    selected_category = request.GET.get('category', '')
    
    # Base filters
    filters = {'date': selected_date}
    if selected_shift:
        filters['shift'] = selected_shift
    if selected_type:
        filters['maintenance_type'] = selected_type
    if selected_category:
        filters['maintenance_category'] = selected_category
    
    # Get maintenance data
    activities = MaintenanceActivity.objects.filter(**filters).order_by('-date', '-created_at')
    
    context = {
        'activities': activities,
        'selected_date': selected_date,
        'selected_shift': selected_shift,
        'selected_type': selected_type,
        'selected_category': selected_category,
    }
    
    return render(request, 'maintenance/maintenance_list.html', context)

@login_required
def maintenance_create(request):
    """Create view for maintenance activities"""
    # This would be implemented with a form
    return render(request, 'maintenance/maintenance_form.html')

@login_required
def maintenance_detail(request, pk):
    """Detail view for maintenance activities"""
    activity = get_object_or_404(MaintenanceActivity, pk=pk)
    return render(request, 'maintenance/maintenance_detail.html', {'activity': activity})

@login_required
def maintenance_update(request, pk):
    """Update view for maintenance activities"""
    # This would be implemented with a form
    activity = get_object_or_404(MaintenanceActivity, pk=pk)
    return render(request, 'maintenance/maintenance_form.html', {'activity': activity})

@login_required
def maintenance_delete(request, pk):
    """Delete view for maintenance activities"""
    activity = get_object_or_404(MaintenanceActivity, pk=pk)
    if request.method == 'POST':
        activity.delete()
        messages.success(request, 'Maintenance activity deleted successfully.')
        return redirect('maintenance:list')
    return render(request, 'maintenance/maintenance_confirm_delete.html', {'activity': activity})

@login_required
def maintenance_complete(request, pk):
    """Mark a maintenance activity as completed"""
    activity = get_object_or_404(MaintenanceActivity, pk=pk)
    if request.method == 'POST':
        activity.is_completed = True
        activity.completion_time = timezone.now()
        activity.save()
        messages.success(request, 'Maintenance activity marked as completed.')
        return redirect('maintenance:detail', pk=activity.pk)
    return render(request, 'maintenance/maintenance_complete.html', {'activity': activity})

@login_required
def spare_list(request):
    """List view for spare parts"""
    # Get filter parameters
    selected_equipment = request.GET.get('equipment', '')
    selected_maintenance_type = request.GET.get('maintenance_type', '')
    low_stock_only = request.GET.get('low_stock', False)
    
    # Base filters
    filters = {}
    if selected_equipment:
        filters['equipment_type'] = selected_equipment
    if selected_maintenance_type:
        filters['maintenance_type'] = selected_maintenance_type
    
    # Get spares data
    spares = Spare.objects.filter(**filters).order_by('name')
    
    # Filter for low stock if requested
    if low_stock_only:
        spares = [spare for spare in spares if spare.is_low_stock]
    
    context = {
        'spares': spares,
        'selected_equipment': selected_equipment,
        'selected_maintenance_type': selected_maintenance_type,
        'low_stock_only': low_stock_only,
    }
    
    return render(request, 'maintenance/spare_list.html', context)

@login_required
def spare_create(request):
    """Create view for spare parts"""
    # This would be implemented with a form
    return render(request, 'maintenance/spare_form.html')

@login_required
def spare_detail(request, pk):
    """Detail view for spare parts"""
    spare = get_object_or_404(Spare, pk=pk)
    return render(request, 'maintenance/spare_detail.html', {'spare': spare})

@login_required
def spare_update(request, pk):
    """Update view for spare parts"""
    # This would be implemented with a form
    spare = get_object_or_404(Spare, pk=pk)
    return render(request, 'maintenance/spare_form.html', {'spare': spare})

@login_required
def spare_delete(request, pk):
    """Delete view for spare parts"""
    spare = get_object_or_404(Spare, pk=pk)
    if request.method == 'POST':
        spare.delete()
        messages.success(request, 'Spare part deleted successfully.')
        return redirect('maintenance:spare_list')
    return render(request, 'maintenance/spare_confirm_delete.html', {'spare': spare}) 