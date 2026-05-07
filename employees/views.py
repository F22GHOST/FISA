from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Employee, Division, Rank

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/employees/')
        else:
            return render(request, 'employees/login.html', {'error': True})
    if request.user.is_authenticated:
        return redirect('/employees/')
    return render(request, 'employees/login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def employee_list(request):
    employees = Employee.objects.all()
    active_count = Employee.objects.filter(user__is_active=True).count()
    hrt_count = Employee.objects.filter(is_hrt=True).count()
    division_count = Division.objects.count()
    return render(request, 'employees/employee_list.html', {
        'employees': employees,
        'active_count': active_count,
        'hrt_count': hrt_count,
        'division_count': division_count,
    })

@login_required(login_url='/login/')
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_detail.html', {
        'employee': employee,
    })