from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .models import Delay

@login_required
def delay_list(request):
    """List view for delays"""
    # Get filter parameters
    selected_date = request.GET.get('date', timezone.now().date())
    selected_shift = request.GET.get('shift', '')
    selected_type = request.GET.get('type', '')
    
    # Base filters
    filters = {'date': selected_date}
    if selected_shift:
        filters['shift'] = selected_shift
    if selected_type:
        filters['delay_type'] = selected_type
    
    # Get delays data
    delays = Delay.objects.filter(**filters).order_by('-date', '-created_at')
    
    context = {
        'delays': delays,
        'selected_date': selected_date,
        'selected_shift': selected_shift,
        'selected_type': selected_type,
    }
    
    return render(request, 'delays/delay_list.html', context)

@login_required
def delay_create(request):
    """Create view for delays"""
    # This would be implemented with a form
    return render(request, 'delays/delay_form.html')

@login_required
def delay_detail(request, pk):
    """Detail view for delays"""
    delay = get_object_or_404(Delay, pk=pk)
    return render(request, 'delays/delay_detail.html', {'delay': delay})

@login_required
def delay_update(request, pk):
    """Update view for delays"""
    # This would be implemented with a form
    delay = get_object_or_404(Delay, pk=pk)
    return render(request, 'delays/delay_form.html', {'delay': delay})

@login_required
def delay_delete(request, pk):
    """Delete view for delays"""
    delay = get_object_or_404(Delay, pk=pk)
    if request.method == 'POST':
        delay.delete()
        messages.success(request, 'Delay report deleted successfully.')
        return redirect('delays:list')
    return render(request, 'delays/delay_confirm_delete.html', {'delay': delay})

@login_required
def delay_resolve(request, pk):
    """Resolve a delay"""
    delay = get_object_or_404(Delay, pk=pk)
    if request.method == 'POST':
        delay.is_resolved = True
        delay.resolution_time = timezone.now()
        delay.save()
        messages.success(request, 'Delay marked as resolved.')
        return redirect('delays:detail', pk=delay.pk)
    return render(request, 'delays/delay_resolve.html', {'delay': delay}) 