from Models import *


# CATEGORIA
class CategoriaDao:
    @classmethod
    def salvar(cls, categoria: Categoria):
        with open("dados/categoria.txt", "a") as file:
            file.writelines(f"{categoria.nome}\n")

    @classmethod
    def ler(cls):
        with open("dados/categoria.txt", "r") as file:
            cls.categoria = file.readlines()
            cls.categoria = [i.replace("\n", "") for i in cls.categoria]

        cat = []
        for c in cls.categoria:
            cat.append(Categoria(c))

        return cat


# PRODUTO
class ProdutoDao:
    @classmethod
    def salvar(cls, produto: Produto):
        with open("dados/produto.txt", "a") as file:
            file.writelines(
                f"{produto.nome};{produto.preco};{produto.estoque};{produto.categoria.nome};{produto.fornecedor.nome}\n"
            )

    @classmethod
    def ler(cls):
        with open("dados/produto.txt", "r") as file:
            cls.produto = file.readlines()
            cls.produto = [i.replace("\n", "") for i in cls.produto]

        pro = []
        for p in cls.produto:
            pp = p.split(";")

            produto = Produto(
                nome=pp[0],
                preco=pp[1],
                estoque=pp[2],
                categoria=Categoria(pp[3]),
                fornecedor=Fornecedor(pp[4]),
            )

            pro.append(produto)

        return pro


# FORNECEDOR
class FornecedorDao:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open("dados/fornecedor.txt", "a") as file:
            file.writelines(
                f"{fornecedor.nome};{fornecedor.cnpj_cpf};{fornecedor.endereco};{fornecedor.obs}\n"
            )

    @classmethod
    def ler(cls):
        with open("dados/fornecedor.txt", "r") as file:
            cls.fornecedor = file.readlines()
            cls.fornecedor = [i.replace("\n", "") for i in cls.fornecedor]

        cli = []
        for c in cls.fornecedor:
            cc = c.split(";")

            if c:
                fornecedor = Fornecedor(
                    cc[0],
                    cc[1],
                    cc[2],
                    cc[3],
                )

                cli.append(fornecedor)

        return cli


# FUNCIONARIO
class FuncionarioDao:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open("dados/funcionario.txt", "a") as file:
            file.writelines(
                f"{funcionario.nome};{funcionario.cnpj_cpf};{funcionario.endereco};{funcionario.clt}\n"
            )

    @classmethod
    def ler(cls):
        with open("dados/funcionario.txt", "r") as file:
            cls.funcionario = file.readlines()
            cls.funcionario = [i.replace("\n", "") for i in cls.funcionario]

            cli = []
            for c in cls.funcionario:
                cc = c.split(";")

                funcionario = Funcionario(
                    nome=cc[0],
                    cnpj_cpf=cc[1],
                    endereco=cc[2],
                    clt=cc[3],
                )

                cli.append(funcionario)

        return cli


# CLIENTE
class ClienteDao:
    @classmethod
    def salvar(cls, cliente: Cliente):
        with open("dados/cliente.txt", "a") as file:
            file.writelines(
                f"{cliente.nome};{cliente.cnpj_cpf};{cliente.endereco};{cliente.cod_cliente}\n"
            )

    @classmethod
    def ler(cls):
        with open("dados/cliente.txt", "r") as file:
            cls.cliente = file.readlines()
            cls.cliente = [i.replace("\n", "") for i in cls.cliente]

        cli = []
        for c in cls.cliente:
            cc = c.split(";")

            if c:
                cliente = Cliente(
                    cc[0],
                    cc[1],
                    cc[2],
                    cc[3],
                )

                cli.append(cliente)

        return cli


# VENDA
class VendaDao:
    @classmethod
    def salvar(cls, venda: Venda):
        with open("dados/venda.txt", "a") as file:
            file.writelines(
                f"Venda:{venda.cliente.nome};{venda.funcionario.nome};{venda.data}\n"
            )
            valortotal = []
            for i in venda.itensVenda:
                file.writelines(
                    f"Itens: {i.produto.nome};{i.produto.preco};{float(i.produto.estoque) - i.qtd};{i.qtd}\n"
                )
                valortotal.append(float(i.produto.preco) * i.qtd)

            file.writelines(f"Total:{sum(valortotal)}\n")
            return sum(valortotal)

    @classmethod
    def ler(cls):
        with open("dados/venda.txt", "r") as file:
            cls.venda = file.readlines()
            cls.venda = [i.replace("\n", "") for i in cls.venda]

        ven = []
        for v in cls.venda:
            if v.startswith("Venda:"):
                vv = v.replace("Venda:", "").split(";")
                venda_atual = Venda(
                    cliente=Cliente(vv[0], "", "", ""),
                    funcionario=Funcionario(vv[1], "", "", ""),
                    data=vv[2],
                    itensVenda=[],
                    valor_total=None,
                )

            elif v.startswith("Itens:"):
                vv = v.replace("Itens:", "").split(";")
                produto = Produto(
                    nome=vv[0],
                    preco=float(vv[1]),
                    estoque=float(vv[2]),
                    categoria=Categoria(""),
                )
                qtd = float(vv[3])
                venda_atual.itensVenda.append(ItensVenda(produto=produto, qtd=qtd))
            else:
                venda_atual.valor_total = v.replace("Total:", "")
                ven.append(venda_atual)

        return ven
