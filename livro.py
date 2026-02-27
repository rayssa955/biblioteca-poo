from item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano, autor, num_paginas):
        super().__init__(codigo, titulo, ano)
        self.__autor = autor
        self.__num_paginas = num_paginas

    def get_autor(self):
        return self.__autor

    def get_num_paginas(self):
        return self.__num_paginas

    def exibir_detalhes(self):
        status = "Disponível" if self.get_disponivel() else "Emprestado"
        print(f"\n📚 Livro")
        print(f"Código: {self.get_codigo()}")
        print(f"Título: {self.get_titulo()}")
        print(f"Ano: {self.get_ano()}")
        print(f"Autor: {self.__autor}")
        print(f"Páginas: {self.__num_paginas}")
        print(f"Status: {status}")