from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .forms import UserForm, ActivityForm
from .models import Activity_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Check if user already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, f'User {username} already exists.')
                return redirect('registration')

            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            auth_login(request, user)
            messages.success(request, f'User {username} registered successfully')
            return redirect('login')
        else:
            messages.error(request, 'Form submission failed. Please correct the errors below.')
    else:
        form = UserForm()
    return render(request, 'registration.html', {'form': form})

def login(request):
    if request.method == "POST":
    	username = request.POST.get('user')
    	password = request.POST.get('pas')
    	user = authenticate(request, username=username, password=password)
    	if user is not None:
    		auth_login(request, user)
    		return redirect('welcome')
    	else:
    		messages.error(request, 'Username or password is incorrect.')
    return render(request, 'login.html')

def welcome(request):
    user = request.user
    data = Activity_model.objects.filter(user=user).order_by('-id')
    form = ActivityForm()

    page_number = request.GET.get('page',1)
    paginator = Paginator(data, 3)

    try:
        employees = paginator.get_page(page_number)


    except PageNotAnInteger:
        employees = paginator.page(1)

    except EmptyPage:
        employees = paginator.page(paginator.num_pages)

    return render(request, 'welcome.html', {'data': data, 'form': form,'employees': employees })


def insertData(request):
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
        	Activity_name=form.cleaned_data["Activity_name"]
        	Activity=form.cleaned_data["Activity"]
        	file=form.cleaned_data["file"]

        	user = request.user

        	query=Activity_model(user=user,Activity_name=Activity_name,Activity=Activity,file=file)
        	query.save()
        	messages.info(request, "Data inserted successfully.")
        	return redirect('welcome')
        else:
            messages.error(request, "There was an error with the form submission.")
    else:
        form = ActivityForm()
    return render(request, 'welcome.html', {'form': form})

def updateData(request,id):
    if request.method=="POST":
        Activity_name=request.POST.get('Activity_name')
        Activity=request.POST.get('Activity')
        file = request.FILES.get('file')

        edit=Activity_model.objects.get(id=id)
        edit.Activity_name=Activity_name
        edit.Activity=Activity
        edit.file=file
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect('welcome')

    d=Activity_model.objects.get(id=id) 
    return render(request,"update.html",{"dd":d})

def deleteData(request,id):
    d=Activity_model.objects.get(id=id)
    d.delete()
    messages.warning(request,'Data deleted Successfully')
    return redirect("welcome")

def logout(request):
    auth.logout(request)
    return render(request,'login.html')
