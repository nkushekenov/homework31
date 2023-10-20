from django.contrib import admin
from django.urls import include, path
from HW31.views import author_example, transaction_example

urlpatterns = [
    path('admin/', admin.site.urls),
    path('HW31/', include('HW31.urls')),
    path('', transaction_example, name='home'),
    path('author_example/', author_example, name='author_example')

]

