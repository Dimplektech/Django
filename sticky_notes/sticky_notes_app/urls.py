
from django.urls import path
from .import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('note/<int:id>/', views.note_details, name='note_detail'),
    path('note/new/', views.note_new, name='note_new'),
    path('note/,<int:id>/edit/', views.note_edit, name='note_edit'),
    path('note/<int:id>/delete/', views.note_delete, name='note_delete'),

]
