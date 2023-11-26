from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password") 
        print(username, password)       
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print("User Logged In")
            return redirect(reverse("home"))
        else:
            print("Invalid Credentials")
            return render(request, "login.html", {"error": "Invalid Credentials"})
    return render(request, "login.html")

def signupPage(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already exists"})
        if User.objects.filter(email=email).exists():
            return render(request, "signup.html", {"error": "Email already exists"})
        print(username, password, email)
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        print("User Created")
        login(request, user)
        return redirect(reverse("home"))
    return render(request, "signup.html")

def logoutPage(request):
    logout(request)
    return redirect(reverse("login"))

@login_required(login_url="/login")
def homePage(request):
    records = Record.objects.filter(user=request.user)
    return render(request, "dash.html", {
        "user": request.user,
        "records": records
        })

@login_required(login_url="/login")
def addExpense(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        description = request.POST.get("description")
        date = request.POST.get("date")
        user = request.user
        expense = Record.objects.create(amount=amount, category=category, date=date, user=user, description=description, type="Expense")
        expense.save()
        print("Expense Added")
        return redirect(reverse("home"))
    return render(request, "expense.html")

@login_required(login_url="/login")
def addIncome(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        description = request.POST.get("description")
        date = request.POST.get("date")
        user = request.user
        income = Record.objects.create(amount=amount, category=category, date=date, user=user, description=description, type="Income")
        income.save()
        print("Income Added")
        return redirect(reverse("home"))
    return render(request, "income.html")

@login_required(login_url="/login")
def filter(request):
    if request.method == "POST":
        date = request.POST.get("date")
        month = request.POST.get("month")
        type = request.POST.get("inex")
        category = request.POST.get("category")
        print(date)
        print(month)
        print(str(date), str(month), type, category)
        if not date is False:
            if type == "Income" and category == "All":
                records = Record.objects.filter(date=date, user=request.user, type=type)
            elif type == "Expense" and category == "All":
                records = Record.objects.filter(date=date, user=request.user, type=type)
            elif type == "Income" and category != "All":
                records = Record.objects.filter(date=date, user=request.user, type=type, category=category)
            elif type == "Expense" and category != "All":
                records = Record.objects.filter(date=date, user=request.user, type=type, category=category)
            elif type == "All" and category == "All":
                records = Record.objects.filter(date=date, user=request.user)
            elif type == "All" and category != "All":
                records = Record.objects.filter(date=date, user=request.user, category=category)
            else:
                records = Record.objects.filter(date=date, user=request.user)
        elif not month is False:
            if type == "Income" and category == "All":
                records = Record.objects.filter(date__month=month, user=request.user, type=type)
            elif type == "Expense" and category == "All":
                records = Record.objects.filter(date__month=month, user=request.user, type=type)
            elif type == "Income" and category != "All":
                records = Record.objects.filter(date__month=month, user=request.user, type=type, category=category)
            elif type == "Expense" and category != "All":
                records = Record.objects.filter(date__month=month, user=request.user, type=type, category=category)
            elif type == "All" and category == "All":
                records = Record.objects.filter(date__month=month, user=request.user)
            elif type == "All" and category != "All":
                records = Record.objects.filter(date__month=month, user=request.user, category=category)      
            else:
                records = Record.objects.filter(date__month=month, user=request.user)
        else: 
            if type == "Income" and category == "All":
                records = Record.objects.filter(user=request.user, type=type)
            elif type == "Expense" and category == "All":
                records = Record.objects.filter(user=request.user, type=type)
            elif type == "Income" and category != "All":
                records = Record.objects.filter(user=request.user, type=type, category=category)
            elif type == "Expense" and category != "All":
                records = Record.objects.filter(user=request.user, type=type, category=category)
            elif type == "All" and category == "All":
                records = Record.objects.filter(user=request.user)
            elif type == "All" and category != "All":
                records = Record.objects.filter(user=request.user, category=category)
            else:
                records = Record.objects.filter(user=request.user)
        return render(request, "dash.html", {"records": records})