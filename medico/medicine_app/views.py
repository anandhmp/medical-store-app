from django.shortcuts import render,redirect,get_object_or_404
from .forms import MedicineForm
from .models import Medicine
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q





def home_page(request):
    return render(request,'index.html')



def list_medicine(request):
    query = request.GET.get('q', '')
    medicines = Medicine.objects.all()

    if query:
        medicines = medicines.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'list_medicine.html', {'medicines': medicines, 'query': query})




def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicinelist')  # Redirect to the medicine list page
    else:
        form = MedicineForm()
    return render(request, 'add_medicine.html', {'form': form})



def edit_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, pk=medicine_id)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicinelist')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'edit_medicine.html', {'form': form, 'medicine': medicine})


def delete_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, pk=medicine_id)
    if request.method == 'POST':
        medicine.delete()
        return redirect('medicinelist')
    return render(request, 'delete_medicine.html', {'medicine': medicine})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('medicinelist')  # Redirect to your desired page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('medicinelist')  # Redirect to your desired page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('medicinelist')  # Redirect to your desired page after logout
