# language: pt
Funcionalidade: Gerenciar clientes

    Cenário: Cadastro de cliente
        Quando acesso a página inicial
        E clico em "Novo cliente"
        E preencho o formulário do cliente com as seguintes informações:
            | NOME  | EMAIL         | DT. NASC.  |
            | João  | joao@joao.com | 25/01/1990 |
        E clico no botão "Salvar"
        Então verei a mensagem "Cliente cadastrado com sucesso."
        E verei a seguinte lista dos clientes:
            | NOME | EMAIL         | DT. NASC.   |
            | João | joao@joao.com | 25/01/1990  |

    Cenário: Lista apresenta os clientes ativos
        Dado que existem 2 clientes ativos previamente cadastrado
        E que existem 2 clientes inativos previamente cadastrado
        Quando acesso a página inicial
        Então verei a seguinte lista dos clientes:
            | NOME      | EMAIL               | DT. NASC.   |
            | Client #0 | client0@example.com | 15/06/1990  |
            | Client #1 | client1@example.com | 15/06/1990  |

    Cenário: Possibilidade de visualizar clientes inativos
        Dado que existem 2 clientes ativos previamente cadastrado
        E que existem 2 clientes inativos previamente cadastrado
        Quando acesso a página inicial
        E clico em "Visualizar clientes inativos"
        Então verei a seguinte lista dos clientes:
            | NOME      | EMAIL               | DT. NASC.   |
            | Client #2 | client2@example.com | 15/06/1990  |
            | Client #3 | client3@example.com | 15/06/1990  |
