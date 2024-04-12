from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ArchetypeListView.as_view(), name='archetype'),
    path('archetype/<int:pk>', views.ArchetypeDetailView.as_view(), name='archetype-detail'),
    path('class/', views.AllClassListView.as_view(), name='class'),
    path('class/<int:pk>', views.AllClassDetailView.as_view(), name='class-detail'),
    path('combat-engraving/', views.CombatEngravingListView.as_view(), name='combat-engraving'),
    path('combat-engraving/<int:pk>', views.CombatEngravingDetailView.as_view(), name='combat-engraving-detail'),
    path('class-engraving/', views.ClassEngravingListView.as_view(), name='class-engraving'),
    path('class-engraving/<int:pk>', views.ClassEngravingDetailView.as_view(), name='class-engraving-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
