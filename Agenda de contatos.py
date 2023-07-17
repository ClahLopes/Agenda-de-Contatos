agenda = [] #Criando uma lista vazia

#Cria um novo contato na agenda
def novo():
    global agenda #definindo variavél como global
    nome = p_nome()
    celular = input("Celular:")
    email = input("E-mail:")
    agenda.append([nome, celular, email]) #adicionando dados na agenda
    print("Registro gravado com Sucesso!")

def p_nome():
    return(input("Nome:"))

#lista um registro
def listar_dados(nome, celular, email):
    print("""Nome: %s
Celular: %s
Email: %s""" % (nome, celular, email))
    print("----------------------------------")

#lista todos os registros da matriz
def listar():
    print("CONTATOS DA AGENDA #########")
    for e in agenda:
        listar_dados(e[0], e[1], e[2])
    print("FIM DA AGENDA #########")

#pesquisa um contato pelo nome
def pesquisa(nome):
    name = nome.lower()
    for d, e in enumerate(agenda): #percorre toda a matriz
        if e[0].lower() == name: #procura o nome desejado
            return d #retorna o índice do nome encontrado
        return None #se não encontrar

#exibe o registro ou mensagem de insucesso
def pesquisar():
    p = pesquisa(p_nome())
    if p != None:
        print("Registro encontrado!")
        #atualiza as variáveis se encontrou
        nome = agenda[p][0]
        celular = agenda[p][1]
        email = agenda[p][2]
        listar_dados(nome, celular, email)
    else:
        print("Nome não encontrado!")

#apagar um contato
def apagar():
    global agenda
    nome = p_nome()
    p = pesquisa(nome)
    if p != None:
        del agenda[p]
        print("Registro APAGADO com Sucesso!")
        print("----------------------------------")
    else:
        print("Nome não encontrado.")

#editar um contato
def editar():
    p = pesquisa(p_nome())
    if p != None:
        #mostra o nome e pede adição celular e email
        nome = agenda[p][0]
        print("Nome:", nome)
        celular = input("Celular:")
        email = input("E-mail:")
        agenda[p] = [nome, celular, email] #armazenar novos dados
        print("Registro EDITADO com Sucesso!")
    else:
        print("Nome não encontrado")

#retorna o item do menu ou 0 para invalido
def menu():
    print("""
   1 - Adicionar novo contato
   2 - Editar um contato
   3 - Pesquisar contato
   4 - Lista de contatos
   5 - Apagar um contato
   6 - Sair
""")
    return validar("Escolha uma opção: ", 1, 6)

#valida se o item digitado foi valido
def validar(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return (valor)
            else:
                return (0)
        except ValueError:
            print("Valor inválido, favor digitar entre %d e d% " % (inicio, fim))

#criando menu de opções
while True:  # Criando um loop infinito.
    opcao = menu()
    if opcao == 0:
        print("Opcao Inválida!")
    elif opcao == 6:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        editar()
    elif opcao == 3:
        pesquisar()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        apagar()