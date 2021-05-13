from django.shortcuts import render
from addntravel.models import Travel
from .forms import AddForm

def travel_index(request):
    travels = Travel.objects.all().order_by('-created_on')
    context = {
        "travels": travels,
    }
    return render(request, "travel_index.html", context)


def travel_detail(request):

    form = AddForm()
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            add = Travel(
                destination=form.cleaned_data["destination"],
                season=form.cleaned_data["season"],
                description=form.cleaned_data["description"]
            )
            add.save()


    context = {
        "form": form,
    }

    return render(request, "travel_detail.html", context)