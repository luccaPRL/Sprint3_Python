# Sistema de Gestão Hospitalar Simples
# Desenvolvido para demonstrar conceitos básicos de Python
# Funcionalidades: Controle de ambulatório, pronto atendimento e agendamento de consultas

# Listas para armazenar dados de pacientes e agendamentos
pacientes_ambulatorio = []
pacientes_pronto_atendimento = []
agendamentos = []

# Função principal que gerencia o menu inicial do sistema
def menu_principal():
    while True:
        print("\n=== Sistema de Gestão Hospitalar ===")
        print("1. Ambulatório")
        print("2. Pronto Atendimento")
        print("3. Central de Agendamento")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        # Encaminhamento do usuário conforme a escolha
        if escolha == "1":
            menu_ambulatorio()
        elif escolha == "2":
            menu_pronto_atendimento()
        elif escolha == "3":
            menu_agendamento()
        elif escolha == "4":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para gerenciamento de pacientes do ambulatório
def menu_ambulatorio():
    while True:
        print("\n--- Ambulatório ---")
        print("1. Listar pacientes")
        print("2. Adicionar paciente")
        print("3. Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_pacientes(pacientes_ambulatorio)
        elif escolha == "2":
            adicionar_paciente(pacientes_ambulatorio)
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para gerenciamento de pacientes do pronto atendimento
def menu_pronto_atendimento():
    while True:
        print("\n--- Pronto Atendimento ---")
        print("1. Listar pacientes")
        print("2. Adicionar paciente")
        print("3. Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_pacientes(pacientes_pronto_atendimento)
        elif escolha == "2":
            adicionar_paciente(pacientes_pronto_atendimento)
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para gerenciamento de agendamentos de consultas
def menu_agendamento():
    while True:
        print("\n--- Central de Agendamento ---")
        print("1. Agendar consulta")
        print("2. Listar agendamentos")
        print("3. Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            agendar_consulta()
        elif escolha == "2":
            listar_agendamentos()
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para listar pacientes de uma determinada lista
def listar_pacientes(lista):
    if not lista:
        print("Nenhum paciente cadastrado.")
    else:
        print("Lista de pacientes:")
        for paciente in lista:
            print(f"- {paciente}")

# Função para adicionar pacientes em uma lista específica
def adicionar_paciente(lista):
    nome = input("Digite o nome do paciente: ").strip().title()
    if nome:
        lista.append(nome)
        print(f"Paciente {nome} adicionado com sucesso.")
    else:
        print("Nome inválido.")

# Função para registrar um novo agendamento de consulta
def agendar_consulta():
    nome = input("Digite o nome do paciente para agendar: ").strip().title()
    data = input("Digite a data da consulta (dd/mm/aaaa): ").strip()
    horario = input("Digite o horário da consulta (hh:mm): ").strip()

    if nome and data and horario:
        agendamento = f"{nome} - {data} às {horario}"
        agendamentos.append(agendamento)
        print(f"Consulta agendada para {agendamento}.")
    else:
        print("Informações inválidas.")

# Função para listar todos os agendamentos realizados
def listar_agendamentos():
    if not agendamentos:
        print("Nenhum agendamento realizado.")
    else:
        print("Agendamentos:")
        for agendamento in agendamentos:
            print(f"- {agendamento}")

# Ponto de entrada do sistema
menu_principal()
