# Sistema de Gestão Hospitalar em Python

## 1. Descrição do Projeto
Este projeto consiste no desenvolvimento de um Sistema de Gestão Hospitalar básico utilizando a linguagem de programação Python.

O sistema é dividido em três áreas principais:
- **Ambulatório**: Controle de pacientes para consultas de rotina.
- **Pronto Atendimento**: Gerenciamento de atendimentos de emergência.
- **Central de Agendamento**: Sistema para agendar consultas médicas.

O programa funciona através do terminal (linha de comando), utilizando menus interativos e conceitos fundamentais de programação como:
- Estruturas de decisão (`if`, `elif`, `else`)
- Laços de repetição (`while`, `for`)
- Manipulação de listas e strings
- Modularização de código com funções

---

## 2. Objetivos do Projeto
- Aplicar conceitos básicos de Python em um cenário prático.
- Demonstrar a utilização de menus e navegação baseada em escolhas do usuário.
- Organizar o código de forma clara, simples e objetiva.
- Simular o funcionamento de áreas administrativas de um hospital.

---

## 3. Funcionalidades Implementadas

| Área                 | Funcionalidades                     |
|-----------------------|-------------------------------------|
| **Ambulatório**        | - Listar pacientes<br>- Adicionar novos pacientes |
| **Pronto Atendimento** | - Listar pacientes<br>- Adicionar novos pacientes |
| **Central de Agendamento** | - Agendar novas consultas<br>- Listar agendamentos realizados |

---

## 4. Estrutura do Código
- **Menu Principal**: Escolha entre Ambulatório, Pronto Atendimento, Agendamento ou Sair.
- **Menus Secundários**: Cada área possui seu próprio conjunto de opções.
- **Funções Modulares**: Cada funcionalidade é separada em funções específicas.
- **Armazenamento em Listas**: Dados de pacientes e agendamentos são mantidos em memória temporária.

---

## 5. Tecnologias Utilizadas
- Python
- GitHub

---

## 6. Código Fonte
O código completo pode ser encontrado neste repositório:  
**[([https://github.com/luccaPRL/Sprint3_Python/tree/main](https://github.com/luccaPRL/Sprint3_Python/blob/main/Sistema.py))]**

---

## 7. Diagrama do Funcionamento do Sistema
```plaintext
[Menu Principal]
       |
       | [1] Ambulatório
       |       | Listar pacientes
       |       | Adicionar paciente
       |
       | [2] Pronto Atendimento
       |       | Listar pacientes
       |       | Adicionar paciente
       |
       | [3] Central de Agendamento
       |       | Agendar consulta
       |       | Listar agendamentos
       |
       | [4] Sair
```
## 8. Observações Importantes
Esse codigo funciona para fins educacionais e não utiliza banco de dados.

Todos os dados cadastrados são perdidos ao encerrar o programa.

