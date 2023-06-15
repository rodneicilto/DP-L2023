# DP-L2023

/*************************************************************************
*   FACENS - Desafio Python
*   
*   Projeto WebScraping NIST v1.0
*
*   Autores:
*   - Fabiano Valim
*   - Mauricio Rivereto
*   - Rodnei Cilto
*************************************************************************/ 

Informação sobre o projeto:

- Este é um projeto acadêmico (desafio) que visa comprovar os conhecimentos adquiridos em sala de aula.
- O projeto tem a funcionalidade de executar o WebScraping da pagina do NIST, com informações fornecidas pelo usuário, como:
    - Ferramenta da consulta
    - Email que receberá a consulta
    - Data inicio e fim da consulta


/*************************************************************************
*   Pré-requisitos (Linux Debian OS)
*************************************************************************/
- Python 3 (interactive high-level object-oriented language)

- Instalar as bibliotecas python do arquivo requirements.txt
    python3-flask (micro web framework based on Werkzeug and Jinja2 - Python 3.x)
    python3-pandas (data structures for "relational" or "labeled" data)
    python3-xlsxwriter (Python 3 module for creating Excel XLSX files)
    python3-xlrd (extract data from Microsoft Excel spreadsheet files)
    python3-selenium (Python3 bindings for Selenium)
    python3-requests (elegant and simple HTTP library for Python3, built for human beings)
    python3-openpyxl (Python 3 module to read/write OpenXML xlsx/xlsm files)
    python3-pyvirtualdisplay (python wrapper for Xvfb, Xephyr and Xvnc)
    
    #apt install python3-flask python3-pandas python3-xlsxwriter python3-xlrd python3-selenium python3-requests python3-openpyxl python3-pyvirtualdisplay

- Instalar o npm (package manager for Node.js)
    #apt install npm
    
    
/*************************************************************************
*   Instalação e Configuração da aplicação
*************************************************************************/ 
- Configuração da conta para envio de email no arquivo send_mail.py
    - Efetue a configuração das variáveis conforme suas credenciais de configuração do email:
    - variáveis - password = '', login = '', no-reply = '', server = '' .

- Configuração do FLASK
    - export FLASK_APP=index.py

- Configuração da aplicação para uso local
O arquivo index.py, pode ser configurado como desejar ou ajustar conforme seu OS. Por padrão está configurado para rodar a aplicação em localhost porta 5000.
    - Para uso local, copie o arquivo v6_selenium_desktop.py para v6_selenium.py

ou

- Configuração da aplicação para publicada (VERCEL)
O arquivo de configuração para o projeto com o vercel está configurado e pode ser modificado da forma que achar melhor.

- Para uso no serviço da Vercel, copie o arquivo v6_selenium_server.py para v6_selelim.py

/*************************************************************************
*   Rodar a aplicação localmente
*************************************************************************/ 
    - flask run
	- Abra o navegador de Internet e entre com o endereço http://127.0.0.1:5000


/*************************************************************************
*   Rodar a aplicação publicada (VERCEL)
*
*   Links de referência para o setup do Vercel:
*    - https://vercel.com/docs/concepts/get-started/deploy
*	- https://vercel.com/docs/cli
*
*************************************************************************/ 
Uso com Vercel
    - Abra o navegador de Internet e entre com o endereço http://.......
