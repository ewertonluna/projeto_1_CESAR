import banco_de_dados
from time import sleep
from helper_functions import *

cadastros = banco_de_dados.usuarios
lista_interesses_disponiveis = banco_de_dados.interesses

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
        print('** Usuário cadastrado com sucesso! **')
        print()
      else:
          print("Só é possível cadastro de email '@cesar.school'. Tente novamente.")
          print()

    elif opcao == '2':
      email = input('Digite seu email: ')
      senha = input('Digite sua senha: ')

      usuario_encontrado = buscarUsuario(cadastros, email, senha)

      if not usuario_encontrado:
        print('USUÁRIO NÃO ENCONTRADO')
        print()
      else:
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
                  print('Buscando...')
                  sleep(1)
                  modo_oposto = getModoOposto(usuario_encontrado)
                  for usuario_atual in cadastros:
                      if usuario_atual['modo'] == modo_oposto:
                          if usuario_atual['bairro'] == usuario_encontrado['bairro']:
                              sleep(1)
                              print('Nome: {}, Bairro: {}, Interesses: {}'.format(usuario_atual['nome'], usuario_atual['bairro'], usuario_atual['interesses']))

              elif opcao == '3':
                modo_oposto = getModoOposto(usuario_encontrado)
                mudarModoUsuario(usuario_encontrado)
                print(f"Agora você está no modo '{modo_oposto}'!")