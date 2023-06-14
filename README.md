# DP-L2023

Informação sobre o projeto:

- Este é um projeto acadêmico (desafio) que visa comprovar os conhecimentos adquiridos em sala de aula.
- O projeto tem a funcionalidade de executar o WebScraping da pagina do NIST, com informações fornecidas pelo usuário, como:
    - Ferramenta da consulta
    - Email que receberá a consulta
    - Data inicio e fim da consulta

Pre-requisitos (Linux Debian OS)

- Python 3
- Instalação do npm
    - apt install npm
	
- Use o arquivo requirements.txt
- Efetue a configuração do email dentro do arquivo send_mail.py
    - Efetue a configuração das variáveis conforme suas credencias de configuração do email:
    - variáveis - password = '', login = '', no-reply = '', server = '' .

Instalação e configuração

- Configuração do FLASK
    - export FLASK_APP=index.py

Uso local
- O arquivo index.py, pode ser configurado para as configurações que deseja ou ajustar conforme seu OS. Como padrão está configurado para rodar em localhost pora 5000.
    - flask run
	- Abra o navegador de Internet e entre com o endereço http://127.0.0.1:5000
    - Para uso local, copie o arquivo v6_selenium_desktop.py para v6_selenium.py

Uso com Vercel
- O arquivo de configuração para o projeto com o vercel está configurado e pode ser modificado da forma que achar melhor.
- Segue os links de referência para o setup do Vercel:
	- Para uso no serviço da Vercel, copie o arquivo v6_selenium_server.py para v6_selelim.py
    - https://vercel.com/docs/concepts/get-started/deploy
	- https://vercel.com/docs/cli

Autores
- Segue os autores do projeto WebScraping NIST
    - Fabiano Valim
    - Mauricio Rivereto
    - Rodnei Cilto
