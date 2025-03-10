from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .models import Rake

@login_required
def rake_list(request):
    """List view for rakes"""
    # Get filter parameters
    selected_date = request.GET.get('date', timezone.now().date())
    selected_shift = request.GET.get('shift', '')
    selected_material = request.GET.get('material', '')
    selected_status = request.GET.get('status', '')
    
    # Base filters
    filters = {'date': selected_date}
    if selected_shift:
        filters['shift'] = selected_shift
    if selected_material:
        filters['material_type'] = selected_material
    if selected_status:
        filters['status'] = selected_status
    
    # Get rakes data
    rakes = Rake.objects.filter(**filters).order_by('-date', '-created_at')
    
    context = {
        'rakes': rakes,
        'selected_date': selected_date,
        'selected_shift': selected_shift,
        'selected_material': selected_material,
        'selected_status': selected_status,
    }
    
    return render(request, 'rakes/rake_list.html', context)

@login_required
def rake_create(request):
    """Create view for rakes"""
    # This would be implemented with a form
    return render(request, 'rakes/rake_form.html')

@login_required
def rake_detail(request, pk):
    """Detail view for rakes"""
    rake = get_object_or_404(Rake, pk=pk)
    return render(request, 'rakes/rake_detail.html', {'rake': rake})

@login_required
def rake_update(request, pk):
    """Update view for rakes"""
    # This would be implemented with a form
    rake = get_object_or_404(Rake, pk=pk)
    return render(request, 'rakes/rake_form.html', {'rake': rake})

@login_required
def rake_delete(request, pk):
    """Delete view for rakes"""
    rake = get_object_or_404(Rake, pk=pk)
    if request.method == 'POST':
        rake.delete()
        messages.success(request, 'Rake report deleted successfully.')
        return redirect('rakes:list')
    return render(request, 'rakes/rake_confirm_delete.html', {'rake': rake})

@login_required
def rake_complete(request, pk):
    """Mark a rake as completed"""
    rake = get_object_or_404(Rake, pk=pk)
    if request.method == 'POST':
        rake.status = 'COMPLETED'
        rake.unloading_end_time = timezone.now()
        rake.save()
        messages.success(request, 'Rake marked as completed.')
        return redirect('rakes:detail', pk=rake.pk)
    return render(request, 'rakes/rake_complete.html', {'rake': rake}) 