# Integracao_Leitor_Facial
## Método de requisição de logs em leitor facial e registro em arquivo.json, utilizando linguagem Python. ##

# Instruções para Executar o Código Flask no VSCode

Este guia descreve os passos necessários para rodar um servidor Flask no Visual Studio Code (VSCode).

## Pré-requisitos

1. **Instalar o Python**:
   - Verifique se o Python está instalado usando o comando:
     
     
     python --version


   - Ou, em alguns sistemas:

     
     python3 --version


## Passos para Configuração

### 1. Criar um Ambiente Virtual (opcional, mas recomendado)

   No diretório do projeto, execute o seguinte comando para criar um ambiente virtual:


   python -m venv venv


   1.1 Em seguida, ative o ambiente virtual:

   - No Windows:

   
   venv\Scripts\activate


   - No macOS/Linux:


   venv/bin/activate


### 2. Instalar o Flask

   Com o ambiente virtual ativado, instale o Flask, que é o framework necessário para executar a aplicação:


   pip install flask


### 3. Instalar Extensões do VSCode (opcional)

   Para facilitar o desenvolvimento, instale a extensão Python no VSCode. 
   Esta extensão fornece funcionalidades como suporte à sintaxe, depuração e execução de scripts Python.


### 4. Executar o Código

   - Salve o código fornecido em um arquivo, por exemplo, app.py.
   - No terminal do VSCode, com o ambiente virtual ativado, execute o arquivo com o seguinte


   python app.py


### 5. Testar a API

   - O servidor Flask estará rodando em http://127.0.0.1:5000 (por padrão).
   - Use uma ferramenta como Postman ou cURL para testar os endpoints disponíveis na aplicação:


   Endpoint: /device_is_alive.fcgi: 
   (faça uma requisição POST enviando um JSON com o campo access_logs.)
   
   
   Endpoint: /get_access_logs: 
   (faça uma requisição GET para visualizar os logs armazenados no arquivo received_data.json.)

   
   5.1 Exemplo de Teste com cURL:

   Para enviar dados de teste para o endpoint /device_is_alive.fcgi:


   curl -X POST http://127.0.0.1:5000/device_is_alive.fcgi -H "Content-Type: application/json" -d '{"access_logs": "seu_log_aqui"}'


   Para consultar os logs armazenados:


   curl http://127.0.0.1:5000/get_access_logs


### Observação

   Se o arquivo received_data.json já existir no diretório do projeto, o servidor irá adicionar novos logs a ele sem duplicatas.
   
   - A opção debug=True na linha app.run(debug=True) permite ver mensagens de erro detalhadas durante o desenvolvimento. 
   - Remova ou desative esta opção em produção para maior segurança.
   - Agora, o servidor Flask deve estar ativo, e você poderá interagir com ele por meio dos endpoints configurados.

   - 
