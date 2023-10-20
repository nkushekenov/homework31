from django.urls import path
from . import views

urlpatterns = [
    path('transaction_example/', views.transaction_example, name='transaction_example'),
    path('author_example/', views.author_example, name='author_example'),
]


