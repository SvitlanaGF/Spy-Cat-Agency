from django.urls import path
from .views import *

app_name = 'missions'
urlpatterns = [
    path('create-mission/', CreateMission.as_view(), name='mission_create'),
    path('create-target/', CreateTarget.as_view(), name='target_create'),
    path('target-info/', TargetDetail.as_view(), name='target_info'),
    path('/<int:pk>/update-target/', UpdateTarget.as_view(), name='update-target'),
    path('', MissionList.as_view(), name='missions_list'),
    path('<int:pk>/', MissionDetail.as_view(), name='mission_detail'),


]