---

# 🎉 **Instruções para Executar o Código Flask no VSCode**

Este guia explica os passos para configurar e executar um servidor Flask no Visual Studio Code (VSCode) para o código fornecido.

---

## 📋 **Pré-requisitos**

### 1. **Instale o Python**  
   Verifique se o Python está instalado usando o comando:
   ```bash
   python --version
   ```
   Ou, em alguns sistemas:
   ```bash
   python3 --version
   ```

---

## ⚙️ **Passos para Configuração e Execução**

### 1. **Criar um Ambiente Virtual (opcional, mas recomendado)**  
   No diretório do projeto, crie um ambiente virtual para isolar as dependências do projeto. Execute o seguinte comando:
   ```bash
   python -m venv venv
   ```

   Em seguida, ative o ambiente virtual:

   - **No Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **No macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

---

### 2. **Instalar o Flask**  
   Com o ambiente virtual ativado, instale o Flask, que é o framework necessário para executar a aplicação:
   ```bash
   pip install flask
   ```

---

### 3. **Instalar Extensões do VSCode (opcional)**  
   Para facilitar o desenvolvimento, instale a extensão **Python** no VSCode. Esta extensão fornece funcionalidades como suporte à sintaxe, depuração e execução de scripts Python.

---

### 4. **Executar o Código**  
   - Salve o código fornecido em um arquivo, por exemplo, `app.py`.
   - No terminal do VSCode, com o ambiente virtual ativado, execute o arquivo com o seguinte comando:
     ```bash
     python app.py
     ```

---

### 5. **Testar a API**

   O servidor Flask estará rodando em **`http://127.0.0.1:5000`** (por padrão).

   - Use uma ferramenta como **Postman** ou **cURL** para testar os endpoints disponíveis na aplicação:
     - Endpoint `/device_is_alive.fcgi`: faça uma requisição **POST** enviando um JSON com o campo `access_logs`.
     - Endpoint `/get_access_logs`: faça uma requisição **GET** para visualizar os logs armazenados no arquivo `received_data.json`.

#### 🛠 **Exemplo de Teste com cURL**
   - Para enviar dados de teste para o endpoint `/device_is_alive.fcgi`:
     ```bash
     curl -X POST http://127.0.0.1:5000/device_is_alive.fcgi -H "Content-Type: application/json" -d '{"access_logs": "seu_log_aqui"}'
     ```
   - Para consultar os logs armazenados:
     ```bash
     curl http://127.0.0.1:5000/get_access_logs
     ```

---

### 📝 **Observação**
   - Se o arquivo `received_data.json` já existir no diretório do projeto, o servidor irá adicionar novos logs a ele sem duplicatas.
   - A opção `debug=True` na linha `app.run(debug=True)` permite ver mensagens de erro detalhadas durante o desenvolvimento. **Remova ou desative esta opção em produção** para maior segurança.

---

Agora, o servidor Flask deve estar ativo, e você poderá interagir com ele por meio dos endpoints configurados. 🚀

---

Agora, o servidor Flask deve estar ativo, e você poderá interagir com ele por meio dos endpoints configurados.

