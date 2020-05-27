from helper_functions import *

cadastros = [
    {'nome': 'Zé', 'email': 'ju', 'senha': '123', 'bairro': 'Prado', 'modo': 'p', 'interesses': ['Cinema', 'Livros']},
    {'nome': 'Júlia', 'email': 'ju', 'senha': '123', 'bairro': 'Madalena', 'modo': 'p', 'interesses': ['Cinema', 'Livros']},
]

lista_interesses_disponiveis = [
  'Cinema',
  'Novela',
  'Negócios',
  'Video Games',
  'Livros',
  'Artes Plásticas',
  'Tecnologia',
  'Futebol',
  'Música',
  'Série',
]

while True:
  mostrarMenuPrincipal()
  opcao = input('>>> ')

  if opcao == 's':
    break
  else:

    if opcao == '1':
      usuario = criarUsuario(lista_interesses_disponiveis)
      if usuario:
        cadastros.append(usuario)
        print('**Usuário criado com sucesso!**')
      else:
          print("Só é possível cadastro de email '@cesar.school'")

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
                mostrarMenuUsuario(usuario_encontrado)
                opcao = input('>>> ')

                if opcao == 's':
                    break
                elif opcao == '1':
                    perfilUsuario = getPerfilUsuario(usuario_encontrado)
                    print(perfilUsuario)
                elif opcao == '2':
                    for usuario_atual in cadastros:
                        if usuario_atual['modo'] == 'p':
                            if usuario_atual['bairro'] == usuario_encontrado['bairro']:
                                print('Nome: {}, Bairro: {}, Interesses: {}'.format(usuario_atual['nome'], usuario_atual['bairro'], usuario_atual['interesses']))

        if usuario_encontrado['modo'] == 'p':
            while True:
                print()
                mostrarMenuUsuario(usuario_encontrado)
                opcao = input('>>> ')

                if opcao == 's':
                    break
                elif opcao == '1':
                    perfilUsuario = getPerfilUsuario(usuario_encontrado)
                    print(perfilUsuario)
                elif opcao == '2':
                    for usuario_atual in cadastros:
                        if usuario_atual['modo'] == 'm':
                            if usuario_atual['bairro'] == usuario_encontrado['bairro']:
                                print('Nome: {}, Bairro: {}, Interesses: {}'.format(usuario_atual['nome'], usuario_atual['bairro'], usuario_atual['interesses']))
