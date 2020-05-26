from helper_functions import *
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
  print('2 - Fazer login')
  print("** Digite 's' para sair **")

  opcao = input('>>> ')

  if opcao == 's':
    break
  else:
    if opcao == '1':
      usuario = criarUsuario(lista_interesses_disponiveis)
      cadastros.append(usuario)

    elif opcao == '2':
      email = input('Digite seu email: ')
      senha = input('Digite sua senha: ')

      usuario_encontrado = buscarUsuario(cadastros, email, senha)

      if not usuario_encontrado:
        print('USUÁRIO NÃO ENCONTRADO')
        print()
      else:
        if usuario_encontrado['modo'] == 'm':
            while True:
                print()
                print('SEJA BEM-VINDO {}'.format(email))
                print('1 - Ver perfil')
                print('2 - Ver passageiros disponíveis')
                print("** Digite 's' para voltar ao menu principal **")
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
