# Internet Interceptor

Este projeto utiliza o `mitmproxy` para interceptar e filtrar o tráfego de internet, bloqueando automaticamente URLs com palavras-chave específicas. O script `interceptor.py` realiza a filtragem de conteúdo indesejado, útil para controle de acesso e segurança.

## Funcionalidades

- **Filtragem de conteúdo**: Bloqueia URLs e Referers que contêm substrings específicas, como palavras-chave de sites indesejados.
- **Configuração de bloqueios**: As palavras-chave de bloqueio podem ser configuradas no arquivo `.env`.
- **Portabilidade**: Uso de variáveis de ambiente para definir o caminho do script, tornando-o independente do diretório em que é executado.

## Pré-requisitos

- [Python 3.6+](https://www.python.org/downloads/)
- [mitmproxy](https://mitmproxy.org/): pode ser instalado via pip:
    ```bash
    pip install mitmprox
    ```

## Biblioteca python-dotenv para carregar variáveis do arquivo .env:

    ```bash
    pip install python-dotenv
    ```
--- 

## Configuração

### 1. Clonar o repositório:

    ```bash
    git clone https://github.com/seuusuario/internet_interceptor.git
    cd internet_interceptor
    ```

### 2. Criar o arquivo .env:
Crie um arquivo .env na raiz do projeto e defina a variável SUBSTRINGS_TO_BLOCK com as palavras-chave que devem ser bloqueadas, conforme o exemplo abaixo:

    ```env
    SUBSTRINGS_TO_BLOCK='[ "tiktok", "kwai", "shorts", "facebook"]'
    ```

## 3. Configurar um servidor proxy
Configure um servidor proxy na máquina em que o interceptador atuará. 
>***Atenção:*** lemnbre de definir o proxy na ***porta 8888***

## 4. Executar o interceptor:

Utilize o script .bat para iniciar o mitmproxy com o filtro configurado:

    ```bash
    start_interceptor.bat
    ```
--- 


## Como Funciona

O interceptor.py monitora o tráfego e verifica se as URLs ou cabeçalhos "Referer" contêm alguma das substrings bloqueadas.
Quando uma correspondência é encontrada, o mitmproxy responde com um código HTTP 403 e uma mensagem de bloqueio personalizada.

--- 


## Estrutura do Projeto

    ```plaintext
    internet_interceptor/
    ├── interceptor.py          # Script Python com lógica de filtragem de conteúdo
    ├── .env                    # Configura as substrings bloqueadas (não incluído no controle de versão)
    ├── start_interceptor.bat   # Script para iniciar o mitmproxy com variáveis de ambiente
    └── README.md               # Documentação do projeto
    ```

--- 

## Personalização

Para modificar as palavras-chave de bloqueio, edite a variável SUBSTRINGS_TO_BLOCK no arquivo .env. Não é necessário alterar o código do script interceptor.py.
Considerações de Segurança

Este projeto é destinado ao uso em ambientes controlados e pode interferir no tráfego de rede. Certifique-se de obter autorização para interceptar o tráfego antes de usar este software.
Contribuição

--- 

## Contribuições são bem-vindas! Para contribuir:

Faça um fork do repositório.
Crie uma nova branch para suas modificações (git checkout -b minha-modificacao).
Commit suas alterações (git commit -m 'Minha modificação').
Faça o push para a branch (git push origin minha-modificacao).
Abra um Pull Request.

## Licença

Este projeto está licenciado sob a MIT License.