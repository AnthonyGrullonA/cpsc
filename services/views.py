from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def Service_Order_View(request):
    return render(request, 'pages/client_control/service_order.html')


