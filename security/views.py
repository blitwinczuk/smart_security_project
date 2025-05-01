from django.shortcuts import render, redirect, get_object_or_404
from .models import MotionAlert

def home(request):
    return render(request, 'index.html')

def features(request):
    return render(request, 'features.html')

def team(request):
    members = [
        {"name": "Alice", "role": "Backend"},
        {"name": "Bob", "role": "Frontend"},
        {"name": "Charlie", "role": "Hardware"},
        {"name": "Dina", "role": "PM"},
    ]
    return render(request, 'team.html', {"members": members})


def demo(request):
    return render(request, 'demo.html')

def homeowner_dashboard(request):
    alerts = MotionAlert.objects.all().order_by('-timestamp')
    return render(request, 'homeowner_dashboard.html', {'alerts': alerts})

def admin_dashboard(request):
    alerts = MotionAlert.objects.all().order_by('-timestamp')
    return render(request, 'admin_dashboard.html', {'alerts': alerts})

def resolve_alert(request, alert_id):
    alert = get_object_or_404(MotionAlert, id=alert_id)
    alert.status = 'Resolved'
    alert.save()
    return redirect('homeowner_dashboard')

def admin_update_status(request, alert_id):
    alert = get_object_or_404(MotionAlert, id=alert_id)
    if alert.status == 'Unresolved':
        alert.status = 'Pending'
    elif alert.status == 'Pending':
        alert.status = 'Resolved'
    alert.save()
    return redirect('admin_dashboard')
