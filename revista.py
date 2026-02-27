from item_biblioteca import ItemBiblioteca

class Revista(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano, edicao, mes):
        super().__init__(codigo, titulo, ano)
        self.__edicao = edicao
        self.__mes = mes

    def get_edicao(self):
        return self.__edicao

    def get_mes(self):
        return self.__mes

    def exibir_detalhes(self):
        status = "Disponível" if self.get_disponivel() else "Emprestado"
        print(f"\n📰 Revista")
        print(f"Código: {self.get_codigo()}")
        print(f"Título: {self.get_titulo()}")
        print(f"Ano: {self.get_ano()}")
        print(f"Edição: {self.__edicao}")
        print(f"Mês: {self.__mes}")
        print(f"Status: {status}")