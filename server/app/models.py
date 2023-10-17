from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    income = models.IntegerField(default=0)
    phone = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.user.username

class Record(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=(("Income", "Income"), ("Expense", "Expense")))
    category = models.CharField(max_length=100, choices=(
        # income
        ("Salary", "Salary"),
        ("Business", "Business"),
        ("Loan", "Loan"),
        ("Others", "Others"),

        # expense
        ("Groceries", "Groceries"),
        ("Food", "Food"),
        ("Fuel", "Fuel"),
        ("Tax", "Tax"),
        ("Electricity", "Electricity"),
        ("Shopping", "Shopping"),
        ("Travel", "Travel"),
        ("Loan", "Loan"),
        ("Entertainment", "Entertainment"),
        ("Health", "Health"),
        ("Investment", "Investment"),
        ("Rent", "Rent"),
        ("Mobile Bills", "Mobile Bills"),
        ("TV & OTT", "TV & OTT"),
        ("EMI", "EMI"),
        ("Others", "Others")))

    def __str__(self):
        return self.title
