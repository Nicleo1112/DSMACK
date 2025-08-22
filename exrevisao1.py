class Restaurante:
    def __init__(self, nomerestaurante, tiporestaurante, avaliacaorestaurante, salariofuncionarios, quantidadefuncionarios):
        self.nomerestaurante = nomerestaurante
        self.tiporestaurante = tiporestaurante
        self.avaliacaorestaurante = avaliacaorestaurante
        self.__salariofuncionarios = salariofuncionarios
        self.__quantidadefuncionarios = quantidadefuncionarios

    def mostrar_informacoes_funcionarios(self):
        print("Salário dos funcionarios: " + self.__salariofuncionarios)
        print("Quantidade de funcionarios: " + self.__quantidadefuncionarios)


    def mostrar_informacoes_restaurantes(self):
        print("nome do Restaurente: " + self.nomerestaurante)
        print("tipo Restaurante: " + self.tiporestaurante)
        print("avaliação Restaurante: " + self.avaliacaorestaurante)

    def __str__(self):
        return (f"Nome do Restaurante: {self.nomerestaurante}\n"
            f"Tipo do Restaurante: {self.tiporestaurante}\n"
            f"Avaliação: {self.avaliacaorestaurante}\n"
            f"Salário dos Funcionários: {self.__salariofuncionarios}\n"
            f"Quantidade de Funcionários: {self.__quantidadefuncionarios}")

restaurante1 = Restaurante("outback","comida australiana","4.54 estrelas","joao - 2600, maria - 1860, cleber - 4000","3")
print(restaurante1)
