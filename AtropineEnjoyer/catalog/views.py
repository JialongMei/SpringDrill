from django.shortcuts import render
from .models import CombatEngraving, ClassEngraving, AllClass, Archetype, Character
from django.views import generic
from .serializers import CharacterSerializer
from django.http import JsonResponse

class IndexArchetypeCharacterList(generic.ListView):
    model = Archetype
    paginate_by = 6
    context_object_name = 'archetype_list'
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return self.user_character_list(request, *args, **kwargs)

    def user_character_list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            character_list = Character.objects.filter(owner=request.user.id)
            return render(request, 'index.html', context={'character_list': character_list})
        else:
            return 0


def character_list(request):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True)
    return JsonResponse(serializer.data, safe=False)

#replaced by IndexArchetypeCharacterList
# class ArchetypeListView(generic.ListView):
#     model = Archetype
#     paginate_by = 6
#     context_object_name = 'archetype_list'
#     template_name = 'index.html'


class ArchetypeDetailView(generic.DetailView):
    model = Archetype

    def get(self, request, *args, **kwargs):
        return self.all_archetype_detail_view(request, *args, **kwargs)

    def all_archetype_detail_view(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return render(request, 'catalog/archetype_detail.html', context={'archetype': context['object']})


class AllClassListView(generic.ListView):
    model = AllClass
    paginate_by = 10
    context_object_name = 'class_list'
    template_name = 'catalog/class_list.html'


class AllClassDetailView(generic.DetailView):
    model = AllClass

    def get(self, request, *args, **kwargs):
        return self.all_class_detail_view(request, *args, **kwargs)

    def all_class_detail_view(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return render(request, 'catalog/allclass_detail.html', context={'class': context['object']})


class CombatEngravingListView(generic.ListView):
    model = CombatEngraving
    paginate_by = 10
    context_object_name = 'combat_engraving_list'
    template_name = 'catalog/combat_engraving.html'


class CombatEngravingDetailView(generic.DetailView):
    model = CombatEngraving

    def get(self, request, *args, **kwargs):
        return self.combat_engraving_detail_view(request, *args, **kwargs)

    def combat_engraving_detail_view(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return render(request, 'catalog/combatengraving_detail.html', context={'combat_engraving': context['object']})


class ClassEngravingListView(generic.ListView):
    model = ClassEngraving
    paginate_by = 10
    context_object_name = 'class_engraving_list'
    template_name = 'catalog/class_engraving.html'


class ClassEngravingDetailView(generic.DetailView):
    model = ClassEngraving

    def get(self, request, *args, **kwargs):
        return self.class_engraving_detail_view(request, *args, **kwargs)

    def class_engraving_detail_view(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return render(request, 'catalog/classengraving_detail.html', context={'class_engraving': context['object']})
