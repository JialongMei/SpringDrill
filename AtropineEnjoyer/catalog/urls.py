from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
# from armory.views import user_character_list


router = routers.DefaultRouter()
router.register(r'combat-engravings', views.CombatEngravingViewSet)


urlpatterns = [
    path('', views.IndexArchetypeCharacterList.as_view(), name='archetype'),
    # path('character/', user_character_list, name='user-character-list'), replaced by IndexArchetypeCharacterList
    path('archetype/<int:pk>', views.ArchetypeDetailView.as_view(), name='archetype-detail'),
    path('class/', views.AllClassListView.as_view(), name='class'),
    path('class/<int:pk>', views.AllClassDetailView.as_view(), name='class-detail'),
    path('combat-engraving/', views.CombatEngravingListView.as_view(), name='combat-engraving'),
    path('combat-engraving/<int:pk>', views.CombatEngravingDetailView.as_view(), name='combat-engraving-detail'),
    path('class-engraving/', views.ClassEngravingListView.as_view(), name='class-engraving'),
    path('class-engraving/<int:pk>', views.ClassEngravingDetailView.as_view(), name='class-engraving-detail'),
    path('character/', views.character_list),
    path('character/<int:pk>', views.character_detail),
    path('combat-engravings-rest/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
