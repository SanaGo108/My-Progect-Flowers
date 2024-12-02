from django.shortcuts import render

def analytics_home(request):
    return render(request, 'analytics/analytics.html')

