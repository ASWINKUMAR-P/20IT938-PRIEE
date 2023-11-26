from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

income_types = ["All","Salary", "Business", "Gifts", "Interest", "Rental", "Other"]
expense_types = ["All","Groceries","Food","Fuel","Tax","Electricity","Shopping","Travel","Loan","Entertainment","Health","Investment","Rent","Mobile Bills","TV & OTT","EMI"]
types = ["All","Income","Expense"]

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
            is_invalid = True
            return render(request, "login.html", {"is_invalid": is_invalid})
    return render(request, "login.html")

def signupPage(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        if User.objects.filter(username=username).exists():
            username_exist = True
            return render(request, "signup.html", {"username_exist": username_exist})
        if User.objects.filter(email=email).exists():
            email_exist = True
            return render(request, "signup.html", {"email_exist": email_exist})
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
        "records": records,
        "categories": set(income_types+expense_types),
        "types": types
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
    date = request.POST.get("date")
    month = request.POST.get("month")
    type = request.POST.get("inex")
    category = request.POST.get("category")
    records = Record.objects.filter(user=request.user)
    if date:
        records = records.filter(date=date)
    elif month:
        mm = month.split("-")[1]
        yy = month.split("-")[0]
        mm = int(mm)
        yy = int(yy)
        print(mm, yy)
        records = records.filter(date__month=mm , date__year=yy)
    if type != "All":
        records = records.filter(type=type)
    if category != "All":
        records = records.filter(category=category)
    return render(request, "dash.html", {
        "records": records,
        "date": date,
        "month": month,
        "type": type,
        "category": category,
        "categories": set(income_types+expense_types),
        "types": types,
        })

@login_required(login_url="/login")
def edit(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = request.user
        if password != "":
            user.set_password(password)
        user.username = username
        user.email = email
        user.save()
        print("User Updated")
        return render(request, "dash.html",{"user": request.user})
    return render(request, "edit.html", {"user": request.user})