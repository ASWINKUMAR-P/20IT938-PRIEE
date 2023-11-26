from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()
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
        return self.description
