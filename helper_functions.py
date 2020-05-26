from acesso_cep import via_cep

def mostrarMenuPrincipal():
    print('*** MENU PRINCIPAL ***')
    print('1 - Cadastro de Usuário')
    print('2 - Fazer login')
    print("** Digite 's' para sair **")

def criar_interesses_do_usuario(lista_interesses_disponiveis):
    interesses = []

    while True:
        print('*** MENU DE INTERESSES ***')
        for index, interesse in enumerate(lista_interesses_disponiveis, 1):
          print('{} - {}'.format(index, interesse))
        print("** Digite 'ok' para concluir **")

        opcao_interesse = input('>>> ') # '1'

        if opcao_interesse.lower() == 'ok':
          break

        interesse = lista_interesses_disponiveis[int(opcao_interesse) - 1]

        if interesse not in interesses:
          interesses.append(interesse)

    return interesses

def buscarUsuario(cadastros, email, senha):
    for usuario in cadastros:
        email_atual = usuario['email']
        senha_atual = usuario['senha']

        if email_atual == email and senha_atual == senha:
            return usuario

    return None

def criarUsuario(lista_interesses_disponiveis):
      usuario = {}
      nome = input("Nome: ")
      email = input('Email: ')
      senha = input('Senha: ')
      cep = input('CEP: ')
      modo = input("Motorista (Digite 'm') ou passageiro (Digite 'p')?")
      bairro = via_cep(cep)
      usuario['nome'] = nome
      usuario['email'] = email
      usuario['senha'] = senha
      usuario['bairro'] = bairro
      usuario['modo'] = modo

      interesses = criar_interesses_do_usuario(lista_interesses_disponiveis)
      usuario['interesses'] = interesses

      return usuario
