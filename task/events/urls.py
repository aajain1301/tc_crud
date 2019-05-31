from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('create/',views.EventCreate.as_view(),name='create'),
    path('detail/<int:pk>',views.EventDetail.as_view(),name='detail'),
    path('update/<int:pk>',views.EventUpdate.as_view(),name='update'),
    path('delete/<int:pk>',views.EventDelete.as_view(),name='delete'),
    path('list/',views.EventList.as_view(),name='list'),
]
