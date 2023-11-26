from django.urls import path
from .views import *

urlpatterns=[
    path('login/',loginPage,name="login"),
    path('signup/',signupPage,name="signup"),
    path('logout/',logoutPage,name="logout"),
    path('home/',homePage,name="home"),
    path('addexpense/',addExpense,name="expense"),
    path('addincome/',addIncome,name="income"),
    path('filter/',filter,name="filter"),
]