from datetime import datetime, date


class Categoria:
    def __init__(self, nome):
        self.nome = nome


#
class Pessoa:
    def __init__(self, nome, cnpj_cpf=None, endereco=None):
        self.nome = nome
        self.cnpj_cpf = cnpj_cpf
        self.endereco = endereco


class Cliente(Pessoa):
    def __init__(self, nome, cnpj_cpf=None, endereco=None, cod_cliente=None):
        super().__init__(nome, cnpj_cpf, endereco)
        self.cod_cliente = cod_cliente


class Funcionario(Pessoa):
    def __init__(self, nome, cnpj_cpf=None, endereco=None, clt=None):
        super().__init__(nome, cnpj_cpf, endereco)
        self.clt = clt


class Fornecedor(Pessoa):
    def __init__(self, nome, cnpj_cpf=None, endereco=None, obs=None):
        super().__init__(nome, cnpj_cpf, endereco)
        self.obs = obs


#


class Produto:
    def __init__(
        self,
        nome,
        categoria: Categoria = None,
        fornecedor: Fornecedor = None,
        preco=None,
        estoque=0,
    ):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.categoria = categoria
        self.fornecedor = fornecedor


#


class ItensVenda:
    def __init__(self, produto: Produto, qtd):
        self.produto = produto
        self.qtd = qtd


class Venda:
    def __init__(
        self,
        cliente: Cliente,
        funcionario: Funcionario,
        itensVenda: list[ItensVenda],
        data=datetime.now().strftime("%d/%m/%Y"),
        valor_total=None,
    ):
        self.valor_total = valor_total
        self.cliente = cliente
        self.funcionario = funcionario
        self.itensVenda = itensVenda
        self.data = data
