from acesso_cep import via_cep

def mostrarMenuPrincipal():
    print('*** MENU PRINCIPAL ***')
    print('1 - Cadastro de Usuário')
    print('2 - Fazer login')
    print("** Digite 's' para encerrar o programa **")

def mostrarMenuUsuario(usuario):
    modo = usuario['modo']
    if modo == 'm':
        modo_oposto = 'passageiros'
    elif modo == 'p':
        modo_oposto = 'motoristas'
    print('SEJA BEM-VINDO {}'.format(usuario['nome'].upper()))
    print('1 - Ver perfil')
    print('2 - Ver {} disponíveis'.format(modo_oposto))
    print("** Digite 's' para voltar ao menu principal **")

def criar_interesses_do_usuario(lista_interesses_disponiveis):
    interesses = []

    while True:
        print('*** MENU DE INTERESSES ***')
        for index, interesse in enumerate(lista_interesses_disponiveis, 1):
          print('{} - {}'.format(index, interesse))
        print("** Digite 'ok' para concluir **")

        opcao_interesse = input('>>> ')

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

def getPerfilUsuario(usuario):
    nome = usuario['nome']
    email = usuario['email']
    bairro = usuario['bairro']
    interesses = usuario['interesses']
    return f'Nome: {nome}, Email: {email}, Bairro: {bairro}, Interesses: {interesses}'


def criarUsuario(lista_interesses_disponiveis):
      usuario = {}
      email = input('Email: ')
      if '@cesar.school' not in email:
          return {}
      else:
          nome = input("Nome: ")
          senha = input('Senha: ')
          cep = input('CEP: ')
          while True:
              modo = input("Motorista (Digite 'm') ou passageiro (Digite 'p')? ")
              if modo.lower() == 'm' or modo.lower() == 'p':
                  break
              print('Input inválido. Tente novamente')
          bairro = via_cep(cep)
          usuario['nome'] = nome
          usuario['email'] = email
          usuario['senha'] = senha
          usuario['bairro'] = bairro
          usuario['modo'] = modo

          interesses = criar_interesses_do_usuario(lista_interesses_disponiveis)
          usuario['interesses'] = interesses

      return usuario
