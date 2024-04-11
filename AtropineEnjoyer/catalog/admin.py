from django.contrib import admin
from .models import CombatEngraving, Archetype, AllClass, ClassEngraving

admin.site.register(CombatEngraving)
admin.site.register(ClassEngraving)
admin.site.register(Archetype)
admin.site.register(AllClass)


class AllClassInline(admin.TabularInline):
    model =AllClass

