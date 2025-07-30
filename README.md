# 📚 CRUD de Usuários em Python (Terminal)

Este projeto é um **CRUD simples no terminal**, criado em Python, usando somente estruturas básicas como **listas, dicionários e laços de repetição**.  

O objetivo principal é **simular um sistema de cadastro de usuários via terminal**, ótimo para praticar lógica de programação, input de dados e manipulação de dicionários.

---

## ⚙️ Funcionalidades

- 🟢 **Criar usuário** (com CPF, nome, idade e e-mail)
- 🔍 **Consultar usuário** pelo CPF
- ✏️ **Atualizar dados** de um usuário existente
- ❌ **Excluir** usuário do sistema
- 📋 **Menu interativo** para facilitar a navegação

---

## ▶️ Como rodar o projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/ka-rodrigues/interface-CRUD
   cd interface-CRUD
   ```

2. Rode o script principal:
   ```bash
   python main.py
   ```

3. Siga o menu exibido no terminal para navegar entre as opções.

---

## 📁 Estrutura do Código

Tudo está contido em um único arquivo, e o menu roda em loop até que o usuário escolha sair.

- `usuarios = {}` → Dicionário que armazena os cadastros usando o CPF como chave
- Funções separadas para cada operação: criar, ler, atualizar e excluir
- Sistema de menu com `while True` e `input()`

---

## ⚠️ Observações

- O cadastro impede CPFs duplicados
- Os dados são **armazenados apenas em memória** (não persistem após encerrar o programa)
- A função `ler_usuario()` possui um pequeno erro de acesso ao dicionário (está acessando como se fosse um dicionário aninhado, mas os valores estão como tupla)

💡 Isso pode ser corrigido trocando a estrutura de `usuarios[CPF] = nome, idade, email` para um dicionário, como:
```python
usuarios[CPF] = {"nome": nome, "idade": idade, "email": email}
```

---

## 🎯 O que dá pra fazer depois?

- Salvar os dados em um arquivo `.json`
- Separar as funções em arquivos diferentes para melhorar a organização
- Criar uma versão com orientação a objetos
- Desenvolver uma interface gráfica com Tkinter ou uma API com Flask

---

## 🧠 Aprendizados

Esse projeto é excelente para:

- Entender como funciona um CRUD na prática
- Trabalhar com dicionários e estrutura de repetição
- Criar menus simples de interação com o usuário
- Refletir sobre organização de código e boas práticas
