usuarios = {}

def criar_usuario(): 
  CPF = input("CPF: ")
  if CPF in usuarios:
    print("Usuário já Existe")
  else:
      nome = str(input("Nome: "))
      idade = int(input("Idade: "))
      email = str(input("Email: "))
      usuarios[CPF] = nome, idade, email

      print("Cadastro Concluído")
      print()

def ler_usuario():
    CPF = input("CPF: ")
    if CPF in usuarios:
          usuario = usuarios[CPF]
          print(f"{usuario['nome']}, {usuario['idade']} anos, Contato:{usuario['email']}")
    else:
         print("Nenhum Usuário Cadastrado")
         print()

def atualizar_usuario():          
    CPF = input("CPF do Usuário: ")
    if CPF in usuarios:
      nome_novo = input("Digite o nome: ") ##caso errem o nome na hora do cadastro
      idade_nova = input("Digite a idade: ")
      email_novo = input("Digite o email: ")
      usuarios[CPF]['nome'] = nome_novo
      usuarios[CPF]['idade'] = idade_nova
      usuarios[CPF]['email'] = email_novo

      print("Usuário Atualizado com sucesso")
    else:
       print("Usuário não encontrado")
       print()

def deletar_usuario():
      CPF = input("CPF do Usuário: ")
      if CPF in usuarios:
         del usuarios[CPF]
         print("Usuário excluído")
      else:
         print("Usuário não encontrado")
         print()

while True:
   print(" MENU ".center(60, '#'))
   print()
   print(" OPERAÇÕES: ".center(60, '*'))
   print()
   print("[1]Criar Usuário | [2]Ver Usuários | [3]Atualizar Usuário | [4]Remover Usuário | [5]Sair \n")
   print("".center(60, '*'))
   print()
   operacao = int(input("Digite operação que você deseja: "))
   print()

   if operacao == 1:
      criar_usuario()
   elif operacao == 2:
      ler_usuario()
   elif operacao == 3:
      atualizar_usuario()
   elif operacao == 4: 
      deletar_usuario()
   elif operacao == 5:
      print("Saindo")
      break
   else:
      print("Opção Inválida")       

