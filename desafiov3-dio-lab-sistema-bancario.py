from abc import ABC, abstractmethod
from datetime import datetime

# Interface para transações
class InterfaceTransacao(ABC):
    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass


# Classe abstrata para contas
class ContaAbstrata(ABC):
    def __init__(self, agencia, numero_conta, saldo=0.0):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    @abstractmethod
    def exibir_extrato(self):
        pass


# Classe Pessoa (usuário)
class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._endereco = endereco

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf


# Classe ContaCorrente (herança e polimorfismo)
class ContaCorrente(ContaAbstrata, InterfaceTransacao):
    LIMITE_SAQUES = 3
    LIMITE_SAQUE_VALOR = 500.0

    def __init__(self, agencia, numero_conta, usuario):
        super().__init__(agencia, numero_conta)
        self._usuario = usuario
        self._extrato = []
        self._numero_saques = 0

    def depositar(self, valor):
        if valor <= 0:
            print("❌ Valor inválido para depósito.")
            return

        self._saldo += valor
        self._extrato.append({"tipo": "depósito", "valor": valor, "data_hora": datetime.now()})
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if self._numero_saques >= self.LIMITE_SAQUES:
            print("❌ Limite de saques diários atingido.")
            return

        if valor > self.LIMITE_SAQUE_VALOR:
            print("❌ Valor excede o limite permitido para saque.")
            return

        if valor > self._saldo:
            print("❌ Saldo insuficiente.")
            return

        if valor <= 0:
            print("❌ Valor inválido para saque.")
            return

        self._saldo -= valor
        self._numero_saques += 1
        self._extrato.append({"tipo": "saque", "valor": valor, "data_hora": datetime.now()})
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        print("\n=================== Extrato Bancário ====================")
        print("📌 Transações:")

        if self._extrato:
            for transacao in self._extrato:
                data_formatada = transacao["data_hora"].strftime("%d/%m/%Y %H:%M:%S")
                print(f"   - {transacao['tipo'].capitalize()}: R$ {transacao['valor']:.2f} em {data_formatada}")
        else:
            print("   Nenhuma transação registrada.")

        print(f"\n💰 Saldo atual: R$ {self._saldo:.2f}")
        print("=======================================================")


# Classe Banco (gerencia usuários e contas)
class Banco:
    def __init__(self):
        self._usuarios = []
        self._contas = []

    def criar_usuario(self, nome, data_nascimento, cpf, endereco):
        if any(usuario.cpf == cpf for usuario in self._usuarios):
            return "❌ Usuário já cadastrado com este CPF."

        usuario = Pessoa(nome, data_nascimento, cpf, endereco)
        self._usuarios.append(usuario)
        return "✅ Usuário criado com sucesso!"

    def criar_conta_corrente(self, cpf):
        usuario = next((usuario for usuario in self._usuarios if usuario.cpf == cpf), None)
        if not usuario:
            return "❌ Usuário não encontrado. Verifique o CPF informado."

        numero_conta = len(self._contas) + 1
        conta = ContaCorrente("0001", numero_conta, usuario)
        self._contas.append(conta)
        return f"✅ Conta criada com sucesso! Agência: 0001, Número da conta: {numero_conta}"

    def listar_contas(self):
        print("\n=================== Contas Cadastradas ====================")
        for conta in self._contas:
            print(f"Agência: {conta._agencia}, Número da Conta: {conta._numero_conta}, Usuário: {conta._usuario.nome}")
        print("==========================================================")

def main():
    banco = Banco()

    while True:
        print("\n--- Sistema Bancário com POO ---")
        print("1️⃣ Criar Usuário")
        print("2️⃣ Criar Conta Corrente")
        print("3️⃣ Depositar")
        print("4️⃣ Sacar")
        print("5️⃣ Exibir Extrato")
        print("6️⃣ Listar Contas")
        print("7️⃣ Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            data_nascimento = input("Data de nascimento (dd/mm/yyyy): ")
            cpf = input("CPF (somente números): ")
            endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            print(banco.criar_usuario(nome, data_nascimento, cpf, endereco))
        elif opcao == "2":
            cpf = input("CPF do usuário: ")
            print(banco.criar_conta_corrente(cpf))
        elif opcao == "3":
            cpf = input("CPF do usuário: ")
            conta = next((c for c in banco._contas if c._usuario.cpf == cpf), None)
            if conta:
                valor = float(input("Digite o valor para depositar: "))
                conta.depositar(valor)
            else:
                print("❌ Conta não encontrada.")
        elif opcao == "4":
            cpf = input("CPF do usuário: ")
            conta = next((c for c in banco._contas if c._usuario.cpf == cpf), None)
            if conta:
                valor = float(input("Digite o valor para sacar: "))
                conta.sacar(valor)
            else:
                print("❌ Conta não encontrada.")
        elif opcao == "5":
            cpf = input("CPF do usuário: ")
            conta = next((c for c in banco._contas if c._usuario.cpf == cpf), None)
            if conta:
                conta.exibir_extrato()
            else:
                print("❌ Conta não encontrada.")
        elif opcao == "6":
            banco.listar_contas()
        elif opcao == "7":
            print("👋 Obrigado por usar o sistema bancário. Até logo!")
            break
        else:
            print("❌ Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
