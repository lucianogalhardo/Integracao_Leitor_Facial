# Integracao_Leitor_Facial
## Método de requisição de logs em leitor facial e registro em arquivo.json, utilizando linguagem Python. ##

### " Abaixo segue instruções para rodar a api " ###

### Para rodar este código no VSCode, você precisará instalar o ambiente e dependências adequados para executar um servidor Flask. Aqui estão os passos: ###

### 1- Instale o Python: ####

### 2- Certifique-se de que o Python está instalado no seu sistema. Você pode verificar no terminal com o comando: ###

python --version
ou,
python3 --version

### 3- Crie um Ambiente Virtual (opcional, mas recomendado): No diretório do projeto, execute: ###

python -m venv venv   (Isso criará um ambiente virtual chamado venv.)

#### 4- Para ativá-lo: ####

No Windows:
venv\Scripts\activate

No macOS/Linux:
source venv/bin/activate

####Instale o Flask: Com o ambiente virtual ativado, instale o Flask com o comando:

bash
Copiar código
pip install flask
Instale Extensões do VSCode (opcional): Para facilitar o desenvolvimento, instale a extensão Python no VSCode, que adiciona suporte a sintaxe, depuração e execução de scripts Python.

Execute o Código:

Salve o código em um arquivo, por exemplo, app.py.
No terminal do VSCode, com o ambiente virtual ativado, execute o código com:
bash
Copiar código
python app.py
Teste a API:

O servidor Flask estará rodando em http://127.0.0.1:5000 (por padrão).
Você pode usar o Postman ou cURL para enviar requisições para os endpoints /device_is_alive.fcgi (POST) e /get_access_logs (GET).
Agora, o servidor Flask deve estar ativo, e você conseguirá fazer requisições para verificar o funcionamento dos endpoints.
