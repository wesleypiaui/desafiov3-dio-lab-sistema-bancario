# 💳 Sistema Bancário - Versão 3 (POO)

## 📌 Descrição

Este sistema simula as funcionalidades básicas de um banco digital, implementado com os princípios da **Programação Orientada a Objetos (POO)** em Python. A versão 3 refatora e organiza o código usando **herança, abstração, encapsulamento** e **polimorfismo**, garantindo uma estrutura robusta, extensível e reutilizável.

---

## 🧱 Estrutura do Sistema

### 📁 Classes e Responsabilidades

#### 🔹 `InterfaceTransacao (interface)`
Define as operações obrigatórias para uma conta bancária:
- `depositar(valor)`
- `sacar(valor)`

#### 🔹 `ContaAbstrata (classe abstrata)`
Contém os atributos comuns a todas as contas e define:
- `_agencia`
- `_numero_conta`
- `_saldo`
- Método abstrato: `exibir_extrato()`

#### 🔹 `Pessoa`
Representa o usuário do sistema.
- Atributos: `_nome`, `_data_nascimento`, `_cpf`, `_endereco`
- Propriedades: `nome`, `cpf`

#### 🔹 `ContaCorrente (herda ContaAbstrata, implementa InterfaceTransacao)`
Implementação concreta de uma conta corrente:
- Atributos: `_usuario`, `_extrato`, `_numero_saques`
- Constantes: `LIMITE_SAQUES`, `LIMITE_SAQUE_VALOR`
- Métodos:
  - `depositar(valor)`
  - `sacar(valor)`
  - `exibir_extrato()`

#### 🔹 `Banco`
Gerencia os usuários e contas bancárias.
- Atributos: `_usuarios`, `_contas`
- Métodos:
  - `criar_usuario(nome, data_nascimento, cpf, endereco)`
  - `criar_conta_corrente(cpf)`
  - `listar_contas()`

---

## 🧑‍💻 Funcionalidades

- ✅ Criar usuários
- ✅ Criar contas correntes
- ✅ Depositar valores
- ✅ Sacar valores com limite de saques e valor por operação
- ✅ Exibir extrato de transações
- ✅ Listar todas as contas cadastradas

---

## 💡 Tecnologias e Conceitos

- 🐍 **Python 3**
- 🧱 **Orientação a Objetos (POO)**
  - Abstração
  - Herança
  - Polimorfismo
  - Encapsulamento
- 📦 `abc` para interfaces e classes abstratas
- 🕒 `datetime` para registrar data/hora das transações

---

## ▶️ Como Executar

```bash
python sistema_bancario.py
```

---

## 📝 Exemplo de Uso

```text
--- Sistema Bancário com POO ---
1️⃣ Criar Usuário
2️⃣ Criar Conta Corrente
3️⃣ Depositar
4️⃣ Sacar
5️⃣ Exibir Extrato
6️⃣ Listar Contas
7️⃣ Sair
```

---

## 📊 Diagrama UML

Veja o diagrama UML com estrutura horizontal para entender melhor a arquitetura:
![Diagrama UML do Sistema Bancário](./A_UML_class_diagram_in_the_image_represents_the_st.png)

---

## 👨‍💻 Contribuição

Se você deseja contribuir com melhorias para este sistema, sinta-se à vontade para enviar sugestões ou implementar novas funcionalidades.

---

## 📜 Licença

Este projeto é de uso livre e foi desenvolvido para fins educacionais. 🚀