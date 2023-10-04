from django.shortcuts import render

from .shannon_fano_compression import shannon_fano_compression


def shannon_fano_view(request):
    """View para implementar o Shannon Fano."""
    string = request.GET.get("string", "")
    compressor = shannon_fano_compression()
    compressed_data = compressor.compress_data(string)

    context = {
        "compressed_data": compressed_data,
        "section_id": "shannon-fano",
        "string": string,
    }

    return render(
        request,
        "home/shannon_fano.html",
        context,
    )
