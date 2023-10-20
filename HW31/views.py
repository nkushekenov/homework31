from django.shortcuts import render
from .models import Author, TransactionExample

def transaction_example(request):
    TransactionExample.perform_transaction("John", 100)
    return render(request, 'HW31/transaction_example.html')



def author_example(request):
    female_authors = Author.objects.female_authors()
    return render(request, 'HW31/author_example.html', {'female_authors': female_authors})
