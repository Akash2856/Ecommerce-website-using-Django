from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import UserRegistrationForm
from .models import Product, Orders

# Create your views here.


def login_user(request):
    if request.method == "POST":
        #print(request.POST)
        username = request.POST.get('username')
        #print(username)
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        #print(user)
        if user is not None:
            #print(request.GET)
            login(request, user)
            # return HttpResponseRedirect(reverse('home'))
            # return redirect('home')
            return redirect('accounts:home')
        else:
            messages.error(request, 'wrong authentication')
    return render(request, 'accounts/login.html', {})


def logout_user(request):
    logout(request)
    # return HttpResponseRedirect(reverse('home'))
    return redirect('accounts:login')

@login_required
def home(request):
    allproduct = Product.objects.all()
    #print(allproduct)
    params = {'product': allproduct}
    return render(request, 'accounts/home.html', params)


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # print(request.POST)
            # print(form.cleaned_data)

            # comment these these thing because i don't want to create new user every time
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = User.objects.create_user(
                username=username, email=email, password=password)
            # print(user)
            messages.success(
                request, 'thanks for register {}'.format(user.username))
            # return HttpResponseRedirect(reverse('accounts:login'))
            return redirect('accounts:login')
            print("form is valid ")
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

@login_required
def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemjson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'accounts/checkout.html',{'thank':thank, 'id':id})
    return render(request, 'accounts/checkout.html')
