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
    path('edit/',edit,name="edit"),
    path('analytics/',analytics,name="analytics"),
    path('analytics-date/',analyticsByDate,name="analytics-date"),
    path('analytics-month/',analyticsByMonth,name="analytics-month")
]