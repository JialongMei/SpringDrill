from django.shortcuts import render
from .models import CombatEngraving, ClassEngraving, AllClass, Archetype
from django.views import generic
from django.shortcuts import HttpResponse, Http404

def index(request):

    return render(request, 'index.html')


class AllClassListView(generic.ListView):
    model = AllClass
    paginate_by = 5
    context_object_name = 'class_list'
    template_name = 'catalog/class_list.html'


class AllClassDetailView(generic.DetailView):
    model = AllClass

    def all_class_detail_view(request, primary_key):
        try:
            the_class = AllClass.objects.get(pk=primary_key)
        except AllClass.DoesNotExist:
            raise Http404('Class does not exist')

        return render(request, 'catalog/allclass_detail.html', context={'class': the_class})


class CombatEngravingListView(generic.ListView):
    model = CombatEngraving
    paginate_by = 10
    context_object_name = 'combat_engraving_list'
    template_name = 'catalog/combat-engraving.html'


class CombatEngravingDetailView(generic.DetailView):
    model = CombatEngraving

    def combat_engraving_detail_view(request, primary_key):
        try:
            combat_engraving = CombatEngraving.objects.get(pk=primary_key)
        except CombatEngraving.DoesNotExist:
            raise Http404('Combat Engraving does not exist')

        return render(request, 'catalog/combatengraving_detail.html', context={'combat_engraving': combat_engraving})
