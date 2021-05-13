from django.shortcuts import render
from recepies.models import Recepies


def recepies_list(request):
    recepies = Recepies.objects.all().order_by('-created_on')
    context = {
        "recepies": recepies,
    }
    return render(request, "recepies_index.html", context)

def recepies_category(request, category):
    recepies = Recepies.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "recepies": recepies,
    }
    return render(request, "recepies_category.html", context)
