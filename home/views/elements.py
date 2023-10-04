from django.shortcuts import render


def elements(request):
    """Docstring here."""
    context = {}

    return render(
        request,
        "elements.html",
        context,
    )
