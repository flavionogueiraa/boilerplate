class HuffmanCompression(object):
    def __init__(self, left=None, right=None):
        """Método para executarmos ações ao iniciar a classe."""
        self.left = left
        self.right = right

    def children(self):
        """Método para retornar os filhos do nó."""
        return (self.left, self.right)

    def nodes(self):
        """Método para retornar os nós da árvore."""
        return (self.left, self.right)

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return "%s_%s" % (self.left, self.right)

    def huffman_code_tree(self, node, left=True, binString=""):
        """Método para retornar a árvore de huffman."""
        if type(node) is str:
            return {node: binString}
        (l, r) = node.children()
        d = dict()
        d.update(self.huffman_code_tree(l, True, binString + "0"))
        d.update(self.huffman_code_tree(r, False, binString + "1"))
        return d

    def calculate_frequency(self, string):
        """Método para calcular a frequência de cada caractere."""
        freq = {}
        for c in string:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return freq

    def huffman_code(self, string):
        """Método para retornar a codificação de huffman."""
        if not string:
            return []

        freq = self.calculate_frequency(string)

        nodes = freq

        while len(nodes) > 1:
            (key1, c1) = nodes[-1]
            (key2, c2) = nodes[-2]
            nodes = nodes[:-2]
            node = HuffmanCompression(key1, key2)
            nodes.append((node, c1 + c2))

            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

        huffmanCode = HuffmanCompression().huffman_code_tree(nodes[0][0])

        return [
            {
                "char": char,
                "code": huffmanCode[char],
                "frequency": frequency,
            }
            for char, frequency in freq
        ]
