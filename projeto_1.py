from acesso_cep import via_cep
#
# exemplo_de_cadastros = [
#     {'nome': 'julia', 'email': 'ju', 'senha': '123', 'bairro': 'Prado', 'modo': 'p', 'interesses': ['Cinema', 'Livros']},
#     {'nome': 'ewerton', 'email': 'ewe', 'senha': '123', 'bairro': 'Jurere', 'modo': 'm', 'interesses': ['Cinema']},
#     {'nome': 'ze', 'email': 'ze', 'senha': '123', 'bairro': 'madalena', 'modo': 'm', 'interesses': ['Cinema']},
#     {'nome': 'ingrid', 'email': 'ewesasd', 'senha': '123', 'bairro': 'Prado', 'modo': 'p', 'interesses': ['Cinema']},
# ]

cadastros = []

lista_interesses_disponiveis = [
  'Cinema',
  'Novela',
  'Negócios',
  'Video Games',
  'Livros',
  'Artes Plásticas',
  'Tecnologia',
  'Futebol'
  'Música',
  'Série',
]


while True:
  print('*** MENU PRINCIPAL ***')
  print('1 - Cadastro de Usuário')

  print('5 - Fazer login')
  print("** Digite 's' para sair **")

  opcao = input('>>> ')

  if opcao == 's':
    break
  else:
    if opcao == '1':
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
        interesses.append(interesse)

      usuario['interesses'] = interesses
      cadastros.append(usuario)

    elif opcao == '2':
      email = input('Digite seu email: ')
      senha = input('Digite sua senha: ')
      existe_usuario = False

      for usuario in cadastros:
        email_atual = usuario['email']
        senha_atual = usuario['senha']

        if email_atual == email and senha_atual == senha:
          usuario_encontrado = usuario
          existe_usuario = True

          break

      if not existe_usuario:
        print('USUÁRIO NÃO ENCONTRADO')
      else:
        if usuario_encontrado['modo'] == 'm':
            while True:
                print()
                print('SEJA BEM-VINDO {}'.format(email))
                print('1 - Ver perfil')
                print('2 - Ver passageiros disponíveis')
                print("** Digite 's' para sair **")
                opcao = input('>>> ')

                if opcao == 's':
                    break
                elif opcao == '1':
                    print(usuario)
                elif opcao == '2':
                    interesses_em_comum = []
                    for usuario_atual in cadastros:
                        if usuario_atual['modo'] == 'p':
                            if usuario_atual['bairro'] == usuario_encontrado['bairro']:
                                print('Nome: {}, Bairro: {}, Interesses: {}'.format(usuario_atual['nome'], usuario_atual['bairro'], usuario_atual['interesses']))

        if usuario_encontrado['modo'] == 'p':
            while True:
                print()
                print('SEJA BEM-VINDO {}'.format(email))
                print('1 - Ver perfil')
                print('2 - Ver motoristas disponíveis')
                print("** Digite 's' para sair **")
                opcao = input('>>> ')

                if opcao == 's':
                    break
                elif opcao == '1':
                    print(usuario)
                elif opcao == '2':
                    for usuario_atual in cadastros:
                        if usuario_atual['modo'] == 'm':
                            if usuario_atual['bairro'] == usuario_encontrado['bairro']:
                                print('Nome: {}, Bairro: {}, Interesses: {}'.format(usuario_atual['nome'], usuario_atual['bairro'], usuario_atual['interesses']))
