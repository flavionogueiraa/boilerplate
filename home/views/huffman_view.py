from django.shortcuts import render

from .huffman_compression import HuffmanCompression


def huffman_view(request):
    """Docstring here."""
    string = request.GET.get("string", "")
    compressor = HuffmanCompression()
    compressed_data = compressor.huffman_code(string)

    context = {
        "compressed_data": compressed_data,
        "section_id": "huffman",
        "string": string,
    }

    return render(
        request,
        "home/huffman.html",
        context,
    )
