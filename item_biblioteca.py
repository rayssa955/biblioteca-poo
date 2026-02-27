class ItemBiblioteca:
    def __init__(self, codigo, titulo, ano):
        self.__codigo = codigo
        self.set_titulo(titulo)
        self.set_ano(ano)
        self.__disponivel = True

    # GETTERS
    def get_codigo(self):
        return self.__codigo

    def get_titulo(self):
        return self.__titulo

    def get_ano(self):
        return self.__ano

    def get_disponivel(self):
        return self.__disponivel

    # SETTERS com validação
    def set_titulo(self, titulo):
        if titulo.strip() == "":
            print("Título não pode ser vazio.")
        else:
            self.__titulo = titulo

    def set_ano(self, ano):
        if ano > 0:
            self.__ano = ano
        else:
            print("Ano inválido.")

    # Métodos principais
    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"Item '{self.__titulo}' emprestado com sucesso!")
        else:
            print(f"Item '{self.__titulo}' já está emprestado.")

    def devolver(self):
        self.__disponivel = True
        print(f"Item '{self.__titulo}' devolvido com sucesso!")

    def exibir_detalhes(self):
        print("Item genérico da biblioteca.")