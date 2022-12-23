from django.urls import path
from . import views

urlpatterns = [
#    path('<int:danes_id>', views.detail,name='detail'),
    path('<int:dane_id>', views.detail,name='detail'),

    path('create/', views.createdanes,name='createdanes'),
#    path('<int:danes_id/create', views.createdanes,name='createdanes'),
    path('update/<int:dane_id>', views.updatedanes,name='updatedanes'),
    path('delete/<int:dane_id>', views.deletedanes,name='deletedanes'),
]