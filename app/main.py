import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

st.set_page_config(
    page_title="Clima Agora",
    page_icon="🌤️",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e3a5f);
        color: white;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #cbd5e1;
        font-size: 18px;
        margin-bottom: 35px;
    }

    .weather-card {
        background: rgba(255,255,255,0.10);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 25px;
        padding: 30px;
        margin-top: 25px;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0,0,0,0.25);
    }

    .city {
        font-size: 30px;
        font-weight: 700;
    }

    .temperature {
        font-size: 75px;
        font-weight: 800;
        margin: 10px 0;
    }

    .condition {
        font-size: 22px;
        color: #cbd5e1;
        text-transform: capitalize;
    }

    .info {
        background: rgba(255,255,255,0.08);
        border-radius: 15px;
        padding: 15px;
        text-align: center;
    }

    .info-title {
        color: #94a3b8;
        font-size: 14px;
    }

    .info-value {
        font-size: 21px;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="title">🌤️ Clima Agora</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Consulte as condições climáticas da sua cidade</div>',
    unsafe_allow_html=True
)


cidade = st.text_input(
    "📍 Digite uma cidade",
    placeholder="Ex: São Paulo, Florianópolis, Curitiba..."
)


if st.button("🔎 Consultar clima", use_container_width=True):

    if not cidade:
        st.warning("Digite uma cidade primeiro.")
        st.stop()

    if not API_KEY:
        st.error("API Key não encontrada no arquivo .env")
        st.stop()

    url = "https://api.weatherapi.com/v1/current.json"

    parametros = {
        "key": API_KEY,
        "q": cidade,
        "lang": "pt"
    }

    try:

        resposta = requests.get(
            url,
            params=parametros,
            timeout=10
        )

        dados = resposta.json()

        if resposta.status_code != 200:

            mensagem = dados.get(
                "error",
                {}
            ).get(
                "message",
                "Erro desconhecido"
            )

            st.error(
                f"Não foi possível consultar o clima: {mensagem}"
            )

            st.stop()

        local = dados["location"]
        clima = dados["current"]

        st.markdown(
            f"""
            <div class="weather-card">

                <div class="city">
                    📍 {local["name"]}, {local["region"]}
                </div>

                <div class="temperature">
                    {clima["temp_c"]:.0f}°C
                </div>

                <div class="condition">
                    {clima["condition"]["text"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(
                f"""
                <div class="info">
                    <div class="info-title">🌡️ Sensação</div>
                    <div class="info-value">
                        {clima["feelslike_c"]:.0f}°C
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div class="info">
                    <div class="info-title">💧 Umidade</div>
                    <div class="info-value">
                        {clima["humidity"]}%
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f"""
                <div class="info">
                    <div class="info-title">💨 Vento</div>
                    <div class="info-value">
                        {clima["wind_kph"]:.1f} km/h
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.write("")

        col4, col5, col6 = st.columns(3)

        with col4:
            st.metric(
                "Pressão",
                f'{clima["pressure_mb"]:.0f} hPa'
            )

        with col5:
            st.metric(
                "Visibilidade",
                f'{clima["vis_km"]:.1f} km'
            )

        with col6:
            st.metric(
                "UV",
                f'{clima["uv"]}'
            )

        st.caption(
            f'Última atualização: {clima["last_updated"]}'
        )

    except requests.exceptions.RequestException:
        st.error("Não foi possível conectar à API.")

    except Exception as erro:
        st.error(f"Erro inesperado: {erro}")