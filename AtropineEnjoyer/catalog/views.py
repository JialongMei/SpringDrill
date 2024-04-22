from django.shortcuts import render
from .models import CombatEngraving, ClassEngraving, AllClass, Archetype, Character
from django.views import generic
from .serializers import CharacterSerializer, CombatEngravingSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework import permissions, viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view


class IndexArchetypeCharacterList(generic.ListView):
    model = Archetype
    paginate_by = 6
    context_object_name = 'archetype_list'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            character_list = Character.objects.filter(owner=self.request.user.id)
        else:
            character_list = []

        context['character_list'] = character_list

        return context

    # def get(self, request, *args, **kwargs):
    #     return self.user_character_list(request, *args, **kwargs)
    #
    # def user_character_list(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         character_list = Character.objects.filter(owner=request.user.id)
    #         return render(request, 'index.html', context={'character_list': character_list})
    #     else:
    #         return 0


@api_view(['GET', 'POST'])
def character_list(request):
    if request.method == 'GET':
        character = Character.objects.filter(owner=request.user.id)
        serializer = CharacterSerializer(character, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def character_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        character = Character.objects.get(pk=pk)
    except Character.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CharacterSerializer(character)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CharacterSerializer(character, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        character.delete()
        return HttpResponse(status=204)


# replaced by IndexArchetypeCharacterList
# class ArchetypeListView(generic.ListView):
#     model = Archetype
#     paginate_by = 6
#     context_object_name = 'archetype_list'
#     template_name = 'index.html'


class ArchetypeDetailView(generic.DetailView):
    model = Archetype

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        archetype = context['object']

        if self.request.user.is_authenticated:
            character_list = Character.objects.filter(owner=self.request.user.id)
        else:
            character_list = []

        context['character_list'] = character_list
        context['archetype'] = archetype

        return context


class AllClassListView(generic.ListView):
    model = AllClass
    paginate_by = 10
    context_object_name = 'class_list'
    template_name = 'catalog/class_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            character_list = Character.objects.filter(owner=self.request.user.id)
        else:
            character_list = []

        context['character_list'] = character_list

        return context


class AllClassDetailView(generic.DetailView):
    model = AllClass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        allclass = context['object']

        if self.request.user.is_authenticated:
            character_list = Character.objects.filter(owner=self.request.user.id)
        else:
            character_list = []

        context['character_list'] = character_list
        context['class'] = allclass

        return context


class CombatEngravingListView(generic.ListView):
    model = CombatEngraving
    paginate_by = 10
    context_object_name = 'combat_engraving_list'
    template_name = 'catalog/combat_engraving.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            character_list = Character.objects.filter(owner=self.request.user.id)
        else:
            character_list = []

        context['character_list'] = character_list

        return context


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


class CombatEngravingViewSet(viewsets.ModelViewSet):
    queryset = CombatEngraving.objects.all().order_by('name')
    serializer_class = CombatEngravingSerializer
    permission_classes = [permissions.IsAuthenticated]
