from .models import Character


def get_context_data(request):
    if request.user.is_authenticated:
        return{
            "character_list": Character.objects.filter(owner=request.user.id)
        }
    else:
        return {} ##return empty dic
