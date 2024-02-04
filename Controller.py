from Dao import *
from Models import *
from datetime import datetime


# CATEGORIA
class CategoriaController:
    def salvar(self, categoria: Categoria):
        existe = False

        x = CategoriaDao.ler()
        for c in x:
            if c.nome == categoria.nome:
                existe = True

        if not existe:
            CategoriaDao.salvar(categoria)
            print(f"Categoria  '{categoria.nome}' foi cadastrado com sucesso!")
        else:
            print(f"Categoria '{categoria.nome}' já existe!")

    def excluir(self, categoria: Categoria):
        x = CategoriaDao.ler()
        cat = list(filter(lambda x: x.nome == categoria.nome, x))

        y = ProdutoDao.ler()
        cat_pro = list(filter(lambda y: y.categoria.nome == categoria.nome, y))

        if len(cat) <= 0:
            print(f"Não existem a categoria '{categoria.nome}' para excluir.")

        elif len(cat) > 0 and len(cat_pro) > 0:
            print(
                f"A categoria {categoria.nome} não pode ser excluída, pois existe um relacionamento de produto cadastrado!"
            )
        elif len(cat) > 0 and len(cat_pro) <= 0:
            for i in range(len(x)):
                if x[i].nome == categoria.nome:
                    del x[i]
                    break
            print(f"A categoria '{categoria.nome}' foi excluir com sucesso!")

            with open("dados/categoria.txt", "w") as file:
                for c in x:
                    file.writelines(f"{c.nome}\n")

    def editar(self, categoria: Categoria, categoria_editado: Categoria):
        x = CategoriaDao.ler()

        cat = list(filter(lambda x: x.nome == categoria.nome, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.nome == categoria_editado.nome, x))
            if len(cat1) == 0:
                x = list(
                    map(
                        lambda x: (
                            categoria_editado if (x.nome == categoria.nome) else (x)
                        ),
                        x,
                    )
                )
                print(
                    f"A categoria '{categoria.nome}' foi alterado para '{categoria_editado.nome}' com sucesso!"
                )
            else:
                print(
                    f"A categoria '{categoria_editado.nome}' já existe, e não pode ser editado!"
                )
        else:
            print(f"A categoria '{categoria.nome}' não existe para alterar.")

        with open("dados/categoria.txt", "w") as file:
            for c in x:
                file.writelines(f"{c.nome}\n")

    def mostrar(self):
        x = CategoriaDao.ler()
        if len(x) == 0:
            print("Categoria vazia!")
        else:
            for c in x:
                print(f"{c.nome}")


# FUNCIONARIO
class FuncionarioController:
    def salvar(self, funcionario: Funcionario):
        x = FuncionarioDao.ler()

        lista_cnpj_cpf = list(filter(lambda x: x.cnpj_cpf == funcionario.cnpj_cpf, x))
        lista_nome = list(filter(lambda x: x.nome == funcionario.nome, x))

        if len(lista_cnpj_cpf) > 0:
            print(f"O CNPJ {funcionario.cnpj_cpf} já existe!")
        elif len(lista_nome) > 0:
            print(f"O nome {funcionario.nome} já existe!")
        else:
            if (
                len(funcionario.nome) > 5
                and len(funcionario.cnpj_cpf) == 14
                or len(funcionario.cnpj_cpf) == 11
            ):
                FuncionarioDao.salvar(funcionario)
                print(
                    f"O funcioanrio(a) '{funcionario.nome}' foi cadastrado com sucesso!"
                )
            else:
                print("Favor digitar CNPJ/CPF válidos e nome com mais de 5 caracteres!")

    def excluir(self, funcionario: Funcionario):
        x = FuncionarioDao.ler()

        lista_nome = list(filter(lambda x: x.nome == funcionario.nome, x))
        if len(lista_nome) <= 0:
            print(f"Não existem o funcionario '{funcionario.nome}' para excluir.")
        else:
            for i in range(len(x)):
                if x[i].nome == funcionario.nome:
                    del x[i]
                    break

            print(f"O funcionario '{funcionario.nome}' foi excluir com sucesso!")

            with open("dados/funcionario.txt", "w") as file:
                for f in x:
                    file.writelines(f"{f.nome};{f.cnpj_cpf};{f.endereco};{f.clt}\n")

    def editar(self, funcionario: Funcionario, funcionario_editado: Funcionario):
        x = FuncionarioDao.ler()

        lista_nome = list(filter(lambda x: x.nome == funcionario.nome, x))
        if len(lista_nome) > 0:
            lista = list(filter(lambda x: x.nome == funcionario_editado.nome, x))
            if len(lista) == 0:
                x = list(
                    map(
                        lambda x: (
                            funcionario_editado if (x.nome == funcionario.nome) else (x)
                        ),
                        x,
                    )
                )
                print(
                    f"O funcionario '{funcionario.nome}' foi alterado para '{funcionario_editado.nome}' com sucesso!"
                )

            else:
                print(
                    f"O funcionario '{funcionario_editado.nome}' já existe, e não pode ser editado!"
                )
        else:
            print(f"O funcionario '{funcionario.nome}' não existe para alterar.")

        with open("dados/funcionario.txt", "w") as file:
            for f in x:
                file.writelines(f"{f.nome};{f.cnpj_cpf};{f.endereco};{f.clt}\n")

    def mostrar(self):
        x = FuncionarioDao.ler()
        if len(x) == 0:
            print("Funcionario vazio!")
        else:
            print(f"-----------Funcionario--------------")
            for f in x:
                print(f"Nome: {f.nome}")
                print(f"CNPJ/CPF: {f.cnpj_cpf}")
                print(f"Endereço: {f.endereco}")
                print(f"CLT: {f.clt}")
                print(f"--------------------------\n")

    def mostrar_funcionario_venda(self):
        x = FuncionarioDao.ler()
        if len(x) == 0:
            print("Funcionario vazia para realizar uma venda!")
        else:
            print(f"============Funcionario para escolha================\n")
            for f in x:
                print(f"Nome: {f.nome} ")
                print(
                    f"================================================================"
                )


# FORNECEDOR
class FornecedorController:
    def salvar(self, fornecedor: Fornecedor):
        x = FornecedorDao.ler()

        lista_cnpj_cpf = list(filter(lambda x: x.cnpj_cpf == fornecedor.cnpj_cpf, x))
        lista_nome = list(filter(lambda x: x.nome == fornecedor.nome, x))

        if len(lista_cnpj_cpf) > 0:
            print(f"O CNPJ {fornecedor.cnpj_cpf} já existe!")
        elif len(lista_nome) > 0:
            print(f"O nome {fornecedor.nome} já existe!")
        else:
            if (
                len(fornecedor.nome) > 5
                and len(fornecedor.cnpj_cpf) == 14
                or len(fornecedor.cnpj_cpf) == 11
            ):
                FornecedorDao.salvar(fornecedor)
                print(
                    f"O funcioanrio(a) '{fornecedor.nome}' foi cadastrado com sucesso!"
                )
            else:
                print("Favor digitar CNPJ/CPF válidos e nome com mais de 5 caracteres!")

    def excluir(self, fornecedor: Fornecedor):
        x = FornecedorDao.ler()

        lista_nome = list(filter(lambda x: x.nome == fornecedor.nome, x))
        if len(lista_nome) <= 0:
            print(f"Não existem o fornecedor '{fornecedor.nome}' para excluir.")
        else:
            for i in range(len(x)):
                if x[i].nome == fornecedor.nome:
                    del x[i]
                    break

            print(f"O fornecedor '{fornecedor.nome}' foi excluir com sucesso!")

            with open("dados/fornecedor.txt", "w") as file:
                for f in x:
                    file.writelines(f"{f.nome};{f.cnpj_cpf};{f.endereco};{f.obs}\n")

    def editar(self, fornecedor: Fornecedor, fornecedor_editado: Fornecedor):
        x = FornecedorDao.ler()

        lista_nome = list(filter(lambda x: x.nome == fornecedor.nome, x))
        if len(lista_nome) > 0:
            lista = list(filter(lambda x: x.nome == fornecedor_editado.nome, x))
            if len(lista) == 0:
                x = list(
                    map(
                        lambda x: (
                            fornecedor_editado if (x.nome == fornecedor.nome) else (x)
                        ),
                        x,
                    )
                )
                print(
                    f"O fornecedor '{fornecedor.nome}' foi alterado para '{fornecedor_editado.nome}' com sucesso!"
                )

            else:
                print(
                    f"O fornecedor '{fornecedor_editado.nome}' já existe, e não pode ser editado!"
                )
        else:
            print(f"O fornecedor '{fornecedor.nome}' não existe para alterar.")

        with open("dados/fornecedor.txt", "w") as file:
            for f in x:
                file.writelines(f"{f.nome};{f.cnpj_cpf};{f.endereco};{f.obs}\n")

    def mostrar(self):
        x = FornecedorDao.ler()
        if len(x) == 0:
            print("Fornecedor vazio!")
        else:
            print(f"-----------Fornecedor--------------")
            for f in x:
                print(f"Nome: {f.nome}")
                print(f"CNPJ/CPF: {f.cnpj_cpf}")
                print(f"Endereço: {f.endereco}")
                print(f"OBS: {f.obs}")
                print(f"--------------------------\n")


# CLIENTE
class ClienteController:
    def salvar(self, cliente: Cliente):
        x = ClienteDao.ler()

        lista_cnpj_cpf = list(filter(lambda x: x.cnpj_cpf == cliente.cnpj_cpf, x))
        lista_nome = list(filter(lambda x: x.nome == cliente.nome, x))

        if len(lista_cnpj_cpf) > 0:
            print(f"O CNPJ {cliente.cnpj_cpf} já existe!")
        elif len(lista_nome) > 0:
            print(f"O nome {cliente.nome} já existe!")
        else:
            if (
                len(cliente.nome) > 5
                and len(cliente.cnpj_cpf) == 14
                or len(cliente.cnpj_cpf) == 11
            ):
                ClienteDao.salvar(cliente)
                print(f"O funcioanrio(a) '{cliente.nome}' foi cadastrado com sucesso!")
            else:
                print("Favor digitar CNPJ/CPF válidos e nome com mais de 5 caracteres!")

    def excluir(self, cliente: Cliente):
        x = ClienteDao.ler()

        lista_nome = list(filter(lambda x: x.nome == cliente.nome, x))
        if len(lista_nome) <= 0:
            print(f"Não existem o cliente '{cliente.nome}' para excluir.")
        else:
            for i in range(len(x)):
                if x[i].nome == cliente.nome:
                    del x[i]
                    break

            print(f"O cliente '{cliente.nome}' foi excluir com sucesso!")

            with open("dados/cliente.txt", "w") as file:
                for f in x:
                    file.writelines(
                        f"{f.nome};{f.cnpj_cpf};{f.endereco};{f.cod_cliente}\n"
                    )

    def editar(self, cliente: Cliente, cliente_editado: Cliente):
        x = ClienteDao.ler()

        lista_nome = list(filter(lambda x: x.nome == cliente.nome, x))
        if len(lista_nome) > 0:
            lista = list(filter(lambda x: x.nome == cliente_editado.nome, x))
            if len(lista) == 0:
                x = list(
                    map(
                        lambda x: cliente_editado if (x.nome == cliente.nome) else (x),
                        x,
                    )
                )
                print(
                    f"O cliente '{cliente.nome}' foi alterado para '{cliente_editado.nome}' com sucesso!"
                )

            else:
                print(
                    f"O cliente '{cliente_editado.nome}' já existe, e não pode ser editado!"
                )
        else:
            print(f"O cliente '{cliente.nome}' não existe para alterar.")

        with open("dados/cliente.txt", "w") as file:
            for f in x:
                file.writelines(f"{f.nome};{f.cnpj_cpf};{f.endereco};{f.cod_cliente}\n")

    def mostrar(self):
        x = ClienteDao.ler()
        if len(x) == 0:
            print("Cliente vazio!")
        else:
            print(f"-----------Cliente--------------")
            for f in x:
                print(f"Nome: {f.nome}")
                print(f"CNPJ/CPF: {f.cnpj_cpf}")
                print(f"Endereço: {f.endereco}")
                print(f"Nº cliente: {f.cod_cliente}")
                print(f"--------------------------\n")

    def mostrar_cliente_venda(self):
        x = ClienteDao.ler()
        if len(x) == 0:
            print("Cliente vazia para realizar uma venda!")
        else:
            print(f"============Cliente para escolha================\n")
            for c in x:
                print(f"Nome: {c.nome} ")
                print(
                    f"================================================================"
                )


# PRODUTO
class ProdutoController:
    def salvar(self, produto: Produto):
        existe_produto = False
        pro = ProdutoDao.ler()
        for p in pro:
            if p.nome == produto.nome:
                existe_produto = True

        existe_categoria = False
        cat = CategoriaDao.ler()
        for c in cat:
            if c.nome == produto.categoria.nome:
                existe_categoria = True

        if not existe_produto:
            if existe_categoria:
                ProdutoDao.salvar(produto)
                print(f"Produto  '{produto.nome}' foi cadastrado com sucesso!")
            else:
                print(f"Categoria '{produto.categoria.nome}' não existe!")
        else:
            print(f"Produto '{produto.nome}' já existe!")

    def excluir(self, produto: Produto):
        x = ProdutoDao.ler()

        pro = list(filter(lambda x: x.nome == produto.nome, x))
        if len(pro) <= 0:
            print(f"Não existem a produto '{produto.nome}' para excluir.")
        else:
            for i in range(len(x)):
                if x[i].nome == produto.nome:
                    del x[i]
                    break
            print(f"A produto '{produto.nome}' foi excluir com sucesso!")

            with open("dados/produto.txt", "w") as file:
                for p in x:
                    file.writelines(
                        f"{p.nome};{p.preco};{p.estoque};{p.categoria.nome}\n"
                    )

    def editar(self, produto: Produto, produto_editado: Produto):
        x = ProdutoDao.ler()

        cat = list(filter(lambda x: x.nome == produto.nome, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.nome == produto_editado.nome, x))
            if len(cat1) == 0:
                x = list(
                    map(
                        lambda x: produto_editado if (x.nome == produto.nome) else (x),
                        x,
                    )
                )
                print(
                    f"A categoria '{produto.nome}' foi alterado para '{produto_editado.nome}' com sucesso!"
                )
            else:
                print(
                    f"A categoria '{produto_editado.nome}' já existe, e não pode ser editado!"
                )
        else:
            print(f"A categoria '{produto.nome}' não existe para alterar.")

        with open("dados/produto.txt", "w") as file:
            for p in x:
                file.writelines(f"{p.nome};{p.preco};{p.estoque};{p.categoria.nome};{p.fornecedor.nome}\n")

    def mostrar(self):
        x = ProdutoDao.ler()
        if len(x) == 0:
            print("Produto vazia!")
        else:
            print(f"============Produtos================\n")
            for p in x:
                print(f"Nome: {p.nome}")
                print(f"Preço: {p.preco}")
                print(f"Estoque: {p.estoque}")
                print(f"Categoria: {p.categoria.nome}")
                print(f"Fornecedor: {p.fornecedor.nome}")
                print(f"================\n")

    def mostrar_produto_venda(self):
        x = ProdutoDao.ler()
        if len(x) == 0:
            print("Produto vazia para realizar uma venda!")
        else:
            print(f"============Produtos para escolha================\n")
            for p in x:
                if float(p.estoque) > 0:
                    print(
                        f"Nome: {p.nome} | Preço: {p.preco} | Estoque: {p.estoque} | Categoria: {p.categoria.nome} | Fornecedor: {p.fornecedor.nome}"
                    )
                    print(
                        f"================================================================"
                    )


class VendaController:
    def salvar(self, venda: Venda):
        existe_produto = False
        existe_estoque = False

        pro = ProdutoDao.ler()

        for p in pro:
            for i in venda.itensVenda:
                if p.nome == i.produto.nome:
                    existe_produto = True
                    if float(p.estoque) >= i.qtd:
                        existe_estoque = True

                        produtoAjustadoEstoque = p
                        produtoAjustadoEstoque.estoque = float(p.estoque) - i.qtd

                        pro = list(
                            map(
                                lambda pro: (
                                    produtoAjustadoEstoque
                                    if (pro.nome == produtoAjustadoEstoque.nome)
                                    else (pro)
                                ),
                                pro,
                            )
                        )

                        with open("dados/produto.txt", "w") as file:
                            for p in pro:
                                file.writelines(
                                    f"{p.nome};{p.preco};{p.estoque};{p.categoria.nome}\n"
                                )

                        break

        if existe_produto:
            if existe_estoque:
                valortotal = VendaDao.salvar(venda)
                print(f"Venda de R$ {valortotal} realizada com sucesso!")
            else:
                for i in venda.itensVenda:
                    print(
                        f"O produto '{i.produto.nome}' nao tem estoque suficiente para venda.[{i.produto.estoque}|{i.qtd}]"
                    )

        else:
            for i in venda.itensVenda:
                print(f"O produto '{i.produto.nome}' não existe!")

    def mostrar_produto_mais_vendido(self):
        x = VendaDao.ler()

        produtos_dist = {}

        for v in x:
            for i in v.itensVenda:
                nome = i.produto.nome
                qtd = i.qtd

                if not nome in produtos_dist.keys():
                    produtos_dist[nome] = qtd
                else:
                    pegar_qtd = produtos_dist[nome] + qtd
                    produtos_dist[nome] = pegar_qtd

        lista = list(produtos_dist.items())
        ordem = sorted(lista, key=lambda x: x[1], reverse=True)

        print("==========PRODUTOS MAIS VENDIDOS==========")
        for p in ordem:
            print(f"{p[0]} = {p[1]} ")
        print("==========================================")

    def mostrar_vendas(self, data_inicial="01/01/2023", data_final="31/12/2024"):
        vendas = VendaDao.ler()

        data_inicial1 = datetime.strptime(data_inicial, "%d/%m/%Y")
        data_final1 = datetime.strptime(data_final, "%d/%m/%Y")

        venda_selecionada = list(
            filter(
                lambda x: datetime.strptime(x.data, "%d/%m/%Y") >= data_inicial1
                and datetime.strptime(x.data, "%d/%m/%Y") <= data_final1,
                vendas,
            )
        )
        print("==========RELATORIO DE VENDA==========")
        print(f"Data inicial:{data_inicial} / Data final:{data_final}")
        for i in venda_selecionada:
            print(f"Data: {i.data}")
            print(f"Cliente: {i.cliente.nome}")
            print(f"Vendendor(Funcionário): {i.funcionario.nome}")
            for itens in i.itensVenda:
                print(f"Produto: {itens.produto.nome}")
                print(f"Qtd: {itens.qtd}")
                print(f"Estoque(Atual): {itens.produto.estoque}")
                print("-----------------------")

            print(f"Total: R$ {i.valor_total}")
            print("==================================\n")
