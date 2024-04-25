from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CombatEngraving, ClassEngraving, AllClass, Archetype, Character
from django.views import generic
from .serializers import CharacterSerializer, CombatEngravingSerializer
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework import permissions, viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class IndexArchetypeList(generic.ListView):
    model = Archetype
    paginate_by = 6
    context_object_name = 'archetype_list'
    template_name = 'index.html'


class CharacterList(APIView):
    permission_classes = [IsAuthenticated]
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CharacterList, self).dispatch(request, *args, **kwargs)


    def get(self, request, format=None):
        character = Character.objects.filter(owner=request.user.id)
        serializer = CharacterSerializer(character, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CharacterSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CharacterDetail(APIView):
    permission_classes = [IsAuthenticated]
    model = Character

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CharacterDetail, self).dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        try:
            return Character.objects.get(pk=pk)
        except Character.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        character = self.get_object(pk)
        serializer = CharacterSerializer(character)
        return Response(serializer.data,template_name='catalog/character_detail.html')

    def put(self, request, pk, format=None):
        character = self.get_object(pk)
        serializer = CharacterSerializer(character, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        character = self.get_object(pk)
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# replaced by IndexArchetypeList
# class ArchetypeListView(generic.ListView):
#     model = Archetype
#     paginate_by = 6
#     context_object_name = 'archetype_list'
#     template_name = 'index.html'


class ArchetypeDetailView(generic.DetailView):
    model = Archetype


class AllClassListView(generic.ListView):
    model = AllClass
    paginate_by = 10
    context_object_name = 'class_list'
    template_name = 'catalog/class_list.html'


class AllClassDetailView(generic.DetailView):
    model = AllClass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        allclass = context['object']
        context['class'] = allclass

        return context


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


class CombatEngravingViewSet(viewsets.ModelViewSet):
    queryset = CombatEngraving.objects.all().order_by('name')
    serializer_class = CombatEngravingSerializer
    permission_classes = [permissions.IsAuthenticated]
