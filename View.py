import os
from Controller import *
import Controller
from Models import *
from Dao import *

menu = """\033[94m
Sistema de Gerenciamento

[1] - Categoria | [2] - Produto | [3] - Funcionário | [4] - Cliente | [5] - Fornecedor | [6] - Venda | [0] - SAIR
Opção: \033[0m"""

sub_menu = """\033[91m      
      [1] - Novo | [2] - Editar | [3] - Excluir | [4] - Listar | [5] - MENU
Opção: \033[0m"""

sub_menu_venda = """\033[92m      
      [1] - Realizar Venda | [2] - Produto Mais Vendido | [3] - Venda por Periodo | [4] - MENU
Opção: \033[0m"""


if __name__ == "__main__":
    while True:
        op = int(input(menu))
        if op == 0:
            os.system("cls" if os.name == "nt" else "clear")
            break

        # CATEGORIA
        elif op == 1:
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                print("->> CATEGORIA")
                op_sub = int(input(sub_menu))

                os.system("cls" if os.name == "nt" else "clear")
                if op_sub == 1:
                    print("->> Novo")
                    cat = input("Nome: ")
                    Controller.CategoriaController().salvar(Categoria(nome=cat))
                elif op_sub == 2:
                    cat1 = input("Nome da categoria que deseja alterar: ")
                    cat2 = input("Nome da categoria para qual deseja alterar: ")
                    Controller.CategoriaController().editar(
                        Categoria(nome=cat1), Categoria(nome=cat2)
                    )
                elif op_sub == 3:
                    print("->> Excluir")
                    cat = input("Nome da categoria para excluir: ")
                    Controller.CategoriaController().excluir(Categoria(nome=cat))
                elif op_sub == 4:
                    print("->> Listar")
                    Controller.CategoriaController().mostrar()
                elif op_sub == 5:
                    break

        # PRODUTO
        elif op == 2:
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                print("->> PRODUTO")
                op_sub = int(input(sub_menu))

                os.system("cls" if os.name == "nt" else "clear")
                if op_sub == 1:
                    print("->> Novo")
                    nome = input("Nome: ")
                    preco = float(input("Preço: "))
                    estoque = float(input("Estoque: "))
                    categoria = input("Categoria: ")
                    fornecedor = input("Fornecedor: ")

                    p = Produto(
                        nome=nome,
                        preco=preco,
                        estoque=estoque,
                        categoria=Categoria(nome=categoria),
                        fornecedor=Fornecedor(nome=fornecedor)
                    )
                    Controller.ProdutoController().salvar(p)
                elif op_sub == 2:
                    nome1 = input("Nome do produto que deseja alterar: ")
                    nome2 = input("Nome do produto para qual deseja alterar: ")

                    x = ProdutoDao.ler()

                    p = list(filter(lambda x: x.nome == nome1, x))

                    Controller.ProdutoController().editar(
                        Produto(nome=nome1),
                        Produto(
                            nome=nome2,
                            preco=p[0].preco,
                            estoque=p[0].estoque,
                            categoria=Categoria(nome=p[0].categoria.nome),
                        ),
                    )
                elif op_sub == 3:
                    print("->> Excluir")
                    produto = input("Nome da categoria para excluir: ")
                    Controller.ProdutoController().excluir(
                        produto=Produto(nome=produto)
                    )
                elif op_sub == 4:
                    print("->> Listar")
                    Controller.ProdutoController().mostrar()
                elif op_sub == 5:
                    break

        # FUNCIONARIO
        elif op == 3:
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                print("->> FUNCIONARIO")
                op_sub = int(input(sub_menu))

                os.system("cls" if os.name == "nt" else "clear")
                if op_sub == 1:
                    print("->> Novo")
                    nome = input("Nome: ")
                    cnpj_cpf = input("CNPJ/CPF: ")
                    endereco = input("Endereço: ")
                    clt = input("CLT: ")

                    f = Funcionario(nome, cnpj_cpf, endereco, clt)
                    Controller.FuncionarioController().salvar(f)

                elif op_sub == 2:
                    nome1 = input("Nome do Funcionario que deseja alterar: ")
                    nome2 = input("Nome do Funcionario para qual deseja alterar: ")

                    x = FuncionarioDao.ler()

                    f = list(filter(lambda x: x.nome == nome1, x))

                    Controller.FuncionarioController().editar(
                        Funcionario(nome=nome1),
                        Funcionario(
                            nome=nome2,
                            cnpj_cpf=f[0].cnpj_cpf,
                            endereco=f[0].endereco,
                            clt=f[0].clt,
                        ),
                    )

                elif op_sub == 3:
                    print("->> Excluir")
                    funcionario = input("Nome da categoria para excluir: ")
                    Controller.FuncionarioController().excluir(
                        funcionario=Funcionario(nome=funcionario)
                    )
                elif op_sub == 4:
                    print("->> Listar")
                    Controller.FuncionarioController().mostrar()
                elif op_sub == 5:
                    break

        # CLIENTE
        elif op == 4:
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                print("->> CLIENTE")
                op_sub = int(input(sub_menu))

                os.system("cls" if os.name == "nt" else "clear")
                if op_sub == 1:
                    print("->> Novo")
                    nome = input("Nome: ")
                    cnpj_cpf = input("CNPJ/CPF: ")
                    endereco = input("Endereço: ")
                    cod_cliente = input("Nº CLIENTE: ")

                    f = Cliente(nome, cnpj_cpf, endereco, cod_cliente)
                    Controller.ClienteController().salvar(f)

                elif op_sub == 2:
                    nome1 = input("Nome do Cliente que deseja alterar: ")
                    nome2 = input("Nome do Cliente para qual deseja alterar: ")

                    x = ClienteDao.ler()

                    f = list(filter(lambda x: x.nome == nome1, x))

                    Controller.ClienteController().editar(
                        Cliente(nome=nome1),
                        Cliente(
                            nome=nome2,
                            cnpj_cpf=f[0].cnpj_cpf,
                            endereco=f[0].endereco,
                            cod_cliente=f[0].cod_cliente,
                        ),
                    )

                elif op_sub == 3:
                    print("->> Excluir")
                    cliente = input("Nome da categoria para excluir: ")
                    Controller.ClienteController().excluir(
                        cliente=Cliente(nome=cliente)
                    )
                elif op_sub == 4:
                    print("->> Listar")
                    Controller.ClienteController().mostrar()
                elif op_sub == 5:
                    break

        # FORNECEDOR
        elif op == 5:
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                print("->> FORNECEDOR")
                op_sub = int(input(sub_menu))

                os.system("cls" if os.name == "nt" else "clear")
                if op_sub == 1:
                    print("->> Novo")
                    nome = input("Nome: ")
                    cnpj_cpf = input("CNPJ/CPF: ")
                    endereco = input("Endereço: ")
                    obs = input("OBS: ")

                    f = Fornecedor(nome, cnpj_cpf, endereco, obs)
                    Controller.FornecedorController().salvar(f)

                elif op_sub == 2:
                    nome1 = input("Nome do Fornecedor que deseja alterar: ")
                    nome2 = input("Nome do Fornecedor para qual deseja alterar: ")

                    x = FornecedorDao.ler()

                    f = list(filter(lambda x: x.nome == nome1, x))

                    Controller.FornecedorController().editar(
                        Fornecedor(nome=nome1),
                        Fornecedor(
                            nome=nome2,
                            cnpj_cpf=f[0].cnpj_cpf,
                            endereco=f[0].endereco,
                            obs=f[0].obs,
                        ),
                    )

                elif op_sub == 3:
                    print("->> Excluir")
                    fornecedor = input("Nome da categoria para excluir: ")
                    Controller.FornecedorController().excluir(
                        fornecedor=Fornecedor(nome=fornecedor)
                    )
                elif op_sub == 4:
                    print("->> Listar")
                    Controller.FornecedorController().mostrar()
                elif op_sub == 5:
                    break

        # VENDA
        elif op == 6:
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                print("->> VENDA")
                op_sub = int(input(sub_menu_venda))

                os.system("cls" if os.name == "nt" else "clear")
                if op_sub == 1:
                    print("->> Novo")

                    ClienteController().mostrar_cliente_venda()
                    cliente = input("Nome do Cliente: ")

                    FuncionarioController().mostrar_funcionario_venda()
                    funcionario = input("Nome do Vendedor: ")

                    # listar os produtos para escolhar
                    ProdutoController().mostrar_produto_venda()

                    lista_itens = []

                    while True:
                        nome_produto = input(
                            "Qual nome do produto que deseja selecionar ou digite FIM para finallizar: "
                        )
                        if nome_produto == "FIM":
                            break
                        qtd_produto = float(input("Qtd: "))

                        x = ProdutoDao.ler()
                        lista_produto_selecionando = list(
                            filter(lambda x: x.nome == nome_produto, x)
                        )[0]

                        iV = ItensVenda(
                            produto=lista_produto_selecionando, qtd=qtd_produto
                        )
                        lista_itens.append(iV)

                    v = Venda(
                        cliente=Cliente(nome=cliente),
                        funcionario=Funcionario(nome=funcionario),
                        itensVenda=lista_itens,
                        data=datetime.now().strftime("%d/%m/%Y"),
                    )

                    VendaController().salvar(v)

                elif op_sub == 2:
                    VendaController().mostrar_produto_mais_vendido()
                elif op_sub == 3:

                    op = input(
                        "Por padrão, o sistema traz o último ano para consultar. Deseja modificar uma data específica? [S/N]"
                    )

                    if str(op).upper() == "S":
                        dt1 = input("Digite a data inicial.(DD/MM/AAAA)")
                        dt2 = input("Digite a data final.(DD/MM/AAAA)")
                        VendaController().mostrar_vendas(
                            data_inicial=dt1, data_final=dt2
                        )
                    else:
                        VendaController().mostrar_vendas()
                elif op_sub == 4:
                    break
