from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('class/', views.AllClassListView.as_view(), name='class'),
    path('class/<int:pk>', views.AllClassDetailView.as_view(), name='class-detail'),
    path('combat-engraving/', views.CombatEngravingListView.as_view(), name='combat-engraving'),
    path('combat-engraving/<int:pk>', views.CombatEngravingDetailView.as_view(), name='combat-engraving-detail'),
]
