
# CRUD de Usuários em Python (Terminal)

Este é um programa de CRUD (Criar, Ler, Atualizar e Deletar) desenvolvido em **Python**, com uma interface via **terminal**, que permite ao usuário gerenciar um cadastro simples de usuários. O projeto demonstra conceitos fundamentais de **entrada/saída de dados**, **laços de repetição**, **condicionais** e **manipulação de dicionários**.

---

## Funcionalidades

O programa oferece um menu interativo com as seguintes operações:

- `[1] Criar Usuário`: Cadastra um novo usuário com CPF, nome, idade e e-mail.
- `[2] Ver Usuários`: Exibe os dados de um usuário já cadastrado, com base no CPF.
- `[3] Atualizar Usuário`: Permite alterar os dados (nome, idade e e-mail) de um usuário existente.
- `[4] Remover Usuário`: Exclui um usuário do sistema usando o CPF.
- `[5] Sair`: Encerra o programa.

O sistema inclui verificações básicas, como impedir o cadastro de CPFs duplicados ou tentar alterar/excluir usuários inexistentes.

---

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação principal utilizada para todo o código.

---

## Estrutura do Código

- O código é estruturado com um `while True` que mantém o menu interativo até que o usuário escolha a opção de sair.
- As operações são realizadas por funções separadas: `criar_usuario`, `ler_usuario`, `atualizar_usuario` e `deletar_usuario`.
- Um dicionário (`usuarios`) é usado para armazenar os dados, com o CPF como chave e os demais dados como valor.

**Observação**: Para um funcionamento completo da atualização e leitura, o ideal é que os dados dos usuários sejam armazenados como dicionários aninhados, e não como tuplas.

---

## Próximos Passos e Melhorias

Este projeto pode ser expandido e melhorado com:

- **Validação de dados**: Garantir que os campos sejam inseridos corretamente (por exemplo, idade numérica, e-mail com formato válido).
- **Tratamento de exceções**: Adicionar `try/except` para prevenir erros com entradas incorretas.
- **Persistência de dados**: Salvar os cadastros em arquivos `.json` ou `.csv` para não perder os dados após fechar o programa.
- **Refatoração com POO**: Organizar o projeto com classes e métodos, como uma classe `Usuario` ou `SistemaCRUD`.
- **Interface Gráfica (GUI)**: Criar uma interface visual utilizando Tkinter, PySimpleGUI ou outro framework leve.
- **Versão Web ou API**: Expandir o projeto para um backend simples com Flask ou FastAPI.

---

## Aprendizados

Este projeto é uma ótima forma de praticar:

- Lógica de programação
- Criação de menus interativos
- Organização de código em funções
- Manipulação de dicionários
- Pensamento em modularização e melhorias futuras
