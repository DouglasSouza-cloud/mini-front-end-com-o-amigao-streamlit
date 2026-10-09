# Clima Agora

Aplicação web desenvolvida com **Python e Streamlit** para consultar as condições climáticas de uma cidade utilizando a API da WeatherAPI.

##  Funcionalidades

* Consulta do clima por cidade.
* Temperatura atual e sensação térmica.
* Umidade do ar.
* Velocidade do vento.
* Pressão atmosférica, visibilidade e índice UV.
* Interface gráfica desenvolvida com Streamlit.

##  Tecnologias utilizadas

* Python
* Streamlit
* Requests
* Python Dotenv
* WeatherAPI

##  Instalação

1. Clone o repositório ou baixe os arquivos do projeto.

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da WeatherAPI:

   ```env
   WEATHER_API_KEY=sua_chave_aqui
   ```

4. Execute a aplicação:

   ```bash
   python -m streamlit run app/main.py
   ```

5. Acesse o endereço exibido no terminal, geralmente `http://localhost:8501`.

##  Estrutura do projeto

```text
mini-front-end-com-o-amigao-streamlit/
├── app/
│   ├── main.py
│   ├── services/
│   │   └── weather_api.py
│   └── utils/
│       └── config.py
├── .env
├── requirements.txt
└── README.md
```

##  API

A aplicação utiliza a [WeatherAPI](https://www.weatherapi.com/) para obter os dados meteorológicos. É necessário criar uma conta e configurar uma chave de API válida.

##  Autor

Projeto desenvolvido para aprendizado de Python, consumo de APIs e criação de interfaces com Streamlit.
