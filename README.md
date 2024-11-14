# Automação da Planilha do Epimed

## Visão Geral
Este projeto tem como objetivo automatizar o processo de extração de dados do sistema Epimed e a atualização de uma planilha compartilhada no Outlook. A planilha conterá informações sobre pacientes, internações, comorbidades, diagnósticos e dispositivos invasivos, organizadas por setor do hospital. Além disso, a planilha incluirá indicadores da unidade, como taxa de ocupação, índices de cuidados de enfermagem e turnover de pacientes, exibidos em gráficos.

## Estrutura de Arquivos
- `main.py`: Ponto de entrada do programa. Coordena a execução das diferentes etapas do processo de automação.
- `epimed_connector.py`: Módulo responsável pela conexão e autenticação no sistema Epimed.
- `data_extractor.py`: Responsável por extrair os dados relevantes do Epimed.
- `sheet_generator.py`: Gera a planilha Excel com as informações extraídas.
- `report_generator.py`: Gera relatórios, gráficos e outras saídas a partir dos dados.
- `ui/app.py`: Implementa a interface gráfica do usuário.
- `ui/components.py`: Contém os componentes reutilizáveis da interface.
- `ui/styles.css`: Folha de estilos CSS para a interface.
- `requirements.txt`: Lista as bibliotecas Python necessárias para o projeto.

## Deployment no Render
1. Crie uma conta no Render (https://render.com).
2. Crie um novo serviço web na sua conta do Render.
3. Selecione "Python" como a linguagem.
4. Defina o comando de inicialização como `python main.py`.
5. Conecte o seu repositório do GitHub ao serviço web do Render.
6. Configure as variáveis de ambiente necessárias, como o nome de usuário e senha do Epimed.
7. Habilite o Autobuild e Autodeploy para que o serviço seja atualizado automaticamente sempre que você fizer um novo commit no seu repositório.
8. Salve as alterações e aguarde o primeiro deploy ser concluído.
9. Acesse a URL do seu serviço web para utilizar a aplicação de automação da planilha do Epimed.

Certifique-se de que todos os arquivos e requisitos do projeto estejam incluídos no seu repositório do GitHub antes de configurar o deploy no Render.