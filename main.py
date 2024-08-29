import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

chave = True
lista = [{"matricula": "1", "nome": "João", "data_inscricao": "01/01/2022", "status_curso": "nao", "aproveitamento": "medio"},
        {"matricula": "2", "nome": "Maria", "data_inscricao": "02/01/2022", "status_curso": "sim", "aproveitamento": "alto"},
        {"matricula": "3", "nome": "Pedro", "data_inscricao": "03/01/2022", "status_curso": "nao", "aproveitamento": "baixo"},
        {"matricula": "4", "nome": "Lucas", "data_inscricao": "04/01/2022", "status_curso": "sim", "aproveitamento": "medio"},
        {"matricula": "5", "nome": "Ana", "data_inscricao": "05/01/2022", "status_curso": "nao", "aproveitamento": "alto"},
        {"matricula": "6", "nome": "Mariana", "data_inscricao": "06/01/2022", "status_curso": "sim", "aproveitamento": "baixo"},
        {"matricula": "7", "nome": "Paulo", "data_inscricao": "07/01/2022", "status_curso": "nao", "aproveitamento": "alto"},
        {"matricula": "8", "nome": "Luiza", "data_inscricao": "08/01/2022", "status_curso": "sim", "aproveitamento": "medio"},
        {"matricula": "9", "nome": "Fernanda", "data_inscricao": "09/01/2022", "status_curso": "nao", "aproveitamento": "baixo"},
        {"matricula": "10", "nome": "Rafael", "data_inscricao": "10/01/2022", "status_curso": "sim", "aproveitamento": "alto"}]
while chave == True:
  print('---------------------------------------------------')
  print('Area de cadastro de alunos')
  print('[1] - Cadastrar aluno')
  print('[2] - Listar cadastros')
  print('[3] - Definir status do cadastro')
  print('[4] - Remover cadastro')
  print('[5] - Sair')
  print('---------------------------------------------------')
  escolha = int(input())
  clear_screen()

  if escolha == 1:
    while True:
      def adicionar():
        """
        Adiciona um novo aluno ao cadastro.

        Retorna:
        dict: Um dicionário representando os dados do aluno cadastrado.
        """
        cadastro = {}
        cadastro['matricula'] = input('Digite a matricula do aluno (ex: 1, 2, 3 ...): ')
        cadastro['nome'] = input('Digite o nome do aluno: ')
        cadastro['data_inscricao'] = input('Digite a data de       inscrição do aluno (dd/mm/aaaa): ')
        cadastro['status_curso'] = input('O aluno concluio o curso (sim/nao): ')
        cadastro['aproveitamento'] = input('Digite o nivel de aproveitamento (baixo, medio, alto): ')
        return cadastro
      print('--------------------------------------')
      print('Cadastro de alunos')
      print('[1] - Cadastrar aluno')
      print('[2] - Voltar ao menu')
      print('--------------------------------------')
      opcao = input()
      if opcao == '1':
        print('--------------------------------------')
        cadastro_do_aluno = adicionar()
        lista.append(cadastro_do_aluno)
        print('Aluno cadastrado com sucesso!')
      elif opcao == '2':
        print('--------------------------------------')
        print('Encerrando cadastro')
        print('--------------------------------------')
        break
      else:
        print('Opção inválida, tente novamente!!')

  elif escolha == 2:
    print('Listando Alunos')
    while True:
        def listar(lista):
          """
          Lista os alunos cadastrados em ordem crescente de matrícula.

          Parâmetros:
          lista (list): Uma lista de dicionários representando os alunos cadastrados.

          Retorna:
          list: A lista de alunos ordenada por matrícula.
          """
          lista = sorted(lista, key=lambda x: int(x['matricula']))

          return lista
        print('--------------------------------------')
        print('listar alunos')
        print('[1] - Lista de aluno')
        print('[2] - Voltar ao menu')
        print('--------------------------------------')
        opcao= input()
        if opcao == '1':
          print('--------------------------------------')
          print('Listando alunos cadastrados')
          resultado = listar(lista)
          for aluno in resultado:
            print(f"Matrícula: {aluno['matricula']},  Nome: {aluno['nome']}, Data de Inscrição: {aluno['data_inscricao']}, Status do Curso: {aluno['status_curso']}, Aproveitamento: {aluno['aproveitamento']}")
          print('--------------------------------------')
        elif opcao == '2':
          print('--------------------------------------')
          print('Encerrando listagem')
          print('--------------------------------------')
          break
        else:
          print('Opção inválida, tente novamente!!')

  elif escolha == 3:
    while True:
      def marcar(lista, matricula):
        """
        Marca o status do curso de um aluno como concluído.

        Parâmetros:
        lista (list): Uma lista de dicionários representando os alunos cadastrados.
        matricula (str): A matrícula do aluno a ser marcado como concluído.
        """
        for item in lista:
            if item.get("matricula") == matricula:
                item["status_curso"] = "sim"
                print(f"O curso do aluno com matrícula {matricula} foi alterado para 'sim'.")
                return
      print('--------------------------------------')
      print('Alterar status de conclusão do curso')
      print('[1] -Alterar status do aluno')
      print('[2] - Voltar ao menu')
      print('--------------------------------------')
      opcao= input()
      if opcao == '1':
        print('--------------------------------------')
        matricula = input('Digite a matricula do aluno a ser alterado: ')
        marcar(lista, matricula)
        print('--------------------------------------')
      elif opcao == '2':
        print('--------------------------------------')
        print('Encerrando Alteração')
        print('--------------------------------------')
        break
      else:
        print('Opção inválida, tente novamente!!') 

  elif escolha == 4:
    while True:
      def remover(lista, matricula):
        """
        Remove um aluno cadastrado da lista.

        Parâmetros:
        lista (list): Uma lista de dicionários representando os alunos cadastrados.
        matricula (str): A matrícula do aluno a ser removido.
        """
        for aluno in lista:
            if aluno["matricula"] == matricula:
                lista.remove(aluno)
                print(f"Aluno com matrícula {matricula} removido com sucesso.")
                return
      print('--------------------------------------')
      print('Alterar status de conclusão do curso')
      print('[1] - Remover aluno')
      print('[2] - Voltar ao menu')
      print('--------------------------------------')
      opcao= input()
      if opcao == '1':

        print('--------------------------------------')
        matricula = input('Digite a matricula do aluno que será removido: ')
        remover(lista, matricula)
        print('--------------------------------------')
      elif opcao == '2':
        print('--------------------------------------')
        print('Encerrando Alteração')
        print('--------------------------------------')
        break
      else:
        print('Opção inválida, tente novamente!!')

  elif escolha == 5:
    print('Saindo do programa')
    chave = False
clear_screen()