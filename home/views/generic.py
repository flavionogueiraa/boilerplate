from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def generic(request):
    """Docstring here."""
    context = {}

    return render(
        request,
        "generic.html",
        context,
    )
