from django.urls import path
from .views import SpyCatCreate, SpyCatUpdate, SpyCatDelete, SpyCatListView, SpyCatDetailView

app_name = 'spy_cats'
urlpatterns = [
    path('create/', SpyCatCreate.as_view(), name='spy_cat_create'),
    path('<int:pk>/update/', SpyCatUpdate.as_view(), name='spy_cat_update'),
    path('<int:pk>/delete/', SpyCatDelete.as_view(), name='spy_cat_delete'),
    path('', SpyCatListView.as_view(), name='spy_cat_list'),
    path('<int:pk>/', SpyCatDetailView.as_view(), name='spy_cat_detail'),


]