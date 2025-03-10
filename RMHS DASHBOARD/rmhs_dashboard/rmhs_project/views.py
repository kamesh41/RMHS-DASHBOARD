from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

from operations.models import Area1Operation, Area23Operation
from delays.models import Delay
from rakes.models import Rake
from maintenance.models import MaintenanceActivity

@login_required
def dashboard(request):
    """Main dashboard view showing summary of all activities"""
    # Get filter parameters
    selected_date = request.GET.get('date', timezone.now().date())
    selected_shift = request.GET.get('shift', '')
    
    # Base filters
    date_filter = {'date': selected_date}
    if selected_shift:
        date_filter['shift'] = selected_shift
    
    # Get operations data
    area1_operations = Area1Operation.objects.filter(**date_filter)
    area23_operations = Area23Operation.objects.filter(**date_filter)
    
    # Calculate totals
    total_feeding = (
        area1_operations.aggregate(total=Sum('feeding_quantity'))['total'] or 0 +
        area23_operations.aggregate(total=Sum('feeding_quantity'))['total'] or 0
    )
    
    total_receiving = (
        area1_operations.aggregate(total=Sum('receiving_quantity'))['total'] or 0 +
        area23_operations.aggregate(total=Sum('receiving_quantity'))['total'] or 0
    )
    
    total_crushing = area23_operations.aggregate(total=Sum('crushing_quantity'))['total'] or 0
    
    total_reclaiming = area1_operations.aggregate(total=Sum('reclaiming_quantity'))['total'] or 0
    
    # Get delays data
    delays = Delay.objects.filter(**date_filter)
    mechanical_delays = delays.filter(delay_type='MECHANICAL').aggregate(total=Sum('duration_hours'))['total'] or 0
    electrical_delays = delays.filter(delay_type='ELECTRICAL').aggregate(total=Sum('duration_hours'))['total'] or 0
    operational_delays = delays.filter(delay_type='OPERATIONAL').aggregate(total=Sum('duration_hours'))['total'] or 0
    
    # Get rakes data
    rakes = Rake.objects.filter(**date_filter)
    total_rakes = rakes.count()
    completed_rakes = rakes.filter(status='COMPLETED').count()
    rake_percentage = (completed_rakes / total_rakes * 100) if total_rakes > 0 else 0
    
    # Get maintenance data
    maintenance_activities = MaintenanceActivity.objects.filter(**date_filter)
    maintenance_count = maintenance_activities.count()
    
    # Target values (these would typically come from a settings model)
    target_feeding = 5000  # Example target in MT
    target_receiving = 4000  # Example target in MT
    target_crushing = 3000  # Example target in MT
    target_reclaiming = 2500  # Example target in MT
    
    context = {
        'selected_date': selected_date,
        'selected_shift': selected_shift,
        
        # Operations data
        'total_feeding': total_feeding,
        'total_receiving': total_receiving,
        'total_crushing': total_crushing,
        'total_reclaiming': total_reclaiming,
        
        # Target values
        'target_feeding': target_feeding,
        'target_receiving': target_receiving,
        'target_crushing': target_crushing,
        'target_reclaiming': target_reclaiming,
        
        # Delays data
        'mechanical_delays': mechanical_delays,
        'electrical_delays': electrical_delays,
        'operational_delays': operational_delays,
        
        # Rakes data
        'total_rakes': total_rakes,
        'completed_rakes': completed_rakes,
        'rake_percentage': rake_percentage,
        
        # Maintenance data
        'maintenance_count': maintenance_count,
    }
    
    return render(request, 'dashboard/index.html', context) 