from typing import Type
from django.shortcuts import render

from typescards.models import Types
from .forms import TypesForm
# Create your views here.
def card_new(request):
    if request.method == "POST":
        form = TypesForm(request.POST)
        if form.is_valid():
            Types = form.save(commit=False)
            Types.save()
    else:
        form = TypesForm()
    return render(request, 'typescards/card_new.html', {'form': form})
