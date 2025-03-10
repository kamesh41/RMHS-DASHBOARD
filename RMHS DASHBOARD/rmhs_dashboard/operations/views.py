from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .models import Area1Operation, Area23Operation

@login_required
def area1_list(request):
    """List view for Area-1 operations"""
    # Get filter parameters
    selected_date = request.GET.get('date', timezone.now().date())
    selected_shift = request.GET.get('shift', '')
    
    # Base filters
    filters = {'date': selected_date}
    if selected_shift:
        filters['shift'] = selected_shift
    
    # Get operations data
    operations = Area1Operation.objects.filter(**filters).order_by('-date', '-created_at')
    
    context = {
        'operations': operations,
        'selected_date': selected_date,
        'selected_shift': selected_shift,
    }
    
    return render(request, 'operations/area1_list.html', context)

@login_required
def area1_create(request):
    """Create view for Area-1 operations"""
    # This would be implemented with a form
    return render(request, 'operations/area1_form.html')

@login_required
def area1_detail(request, pk):
    """Detail view for Area-1 operations"""
    operation = get_object_or_404(Area1Operation, pk=pk)
    return render(request, 'operations/area1_detail.html', {'operation': operation})

@login_required
def area1_update(request, pk):
    """Update view for Area-1 operations"""
    # This would be implemented with a form
    operation = get_object_or_404(Area1Operation, pk=pk)
    return render(request, 'operations/area1_form.html', {'operation': operation})

@login_required
def area1_delete(request, pk):
    """Delete view for Area-1 operations"""
    operation = get_object_or_404(Area1Operation, pk=pk)
    if request.method == 'POST':
        operation.delete()
        messages.success(request, 'Area-1 operation deleted successfully.')
        return redirect('operations:area1_list')
    return render(request, 'operations/area1_confirm_delete.html', {'operation': operation})

@login_required
def area23_list(request):
    """List view for Area-2 & 3 operations"""
    # Get filter parameters
    selected_date = request.GET.get('date', timezone.now().date())
    selected_shift = request.GET.get('shift', '')
    
    # Base filters
    filters = {'date': selected_date}
    if selected_shift:
        filters['shift'] = selected_shift
    
    # Get operations data
    operations = Area23Operation.objects.filter(**filters).order_by('-date', '-created_at')
    
    context = {
        'operations': operations,
        'selected_date': selected_date,
        'selected_shift': selected_shift,
    }
    
    return render(request, 'operations/area23_list.html', context)

@login_required
def area23_create(request):
    """Create view for Area-2 & 3 operations"""
    # This would be implemented with a form
    return render(request, 'operations/area23_form.html')

@login_required
def area23_detail(request, pk):
    """Detail view for Area-2 & 3 operations"""
    operation = get_object_or_404(Area23Operation, pk=pk)
    return render(request, 'operations/area23_detail.html', {'operation': operation})

@login_required
def area23_update(request, pk):
    """Update view for Area-2 & 3 operations"""
    # This would be implemented with a form
    operation = get_object_or_404(Area23Operation, pk=pk)
    return render(request, 'operations/area23_form.html', {'operation': operation})

@login_required
def area23_delete(request, pk):
    """Delete view for Area-2 & 3 operations"""
    operation = get_object_or_404(Area23Operation, pk=pk)
    if request.method == 'POST':
        operation.delete()
        messages.success(request, 'Area-2 & 3 operation deleted successfully.')
        return redirect('operations:area23_list')
    return render(request, 'operations/area23_confirm_delete.html', {'operation': operation}) 