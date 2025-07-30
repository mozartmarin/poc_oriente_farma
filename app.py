import streamlit as st
import pandas as pd
import plotly.express as px
from style.css import inject_custom_css

# Configuração da interface
st.set_page_config(page_title="POC Oriente Farma", layout="wide")
inject_custom_css()

st.title("📦 Análise de Separação de Pedidos - Oriente Farma")
st.markdown("Esta aplicação analisa a relação entre a quantidade de SKUs distintos por pedido e o tempo de separação da ordem de serviço.")

# Upload do Excel
uploaded_file = st.file_uploader("📁 Faça upload do arquivo Excel (.xlsx) com os dados", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file, sheet_name="DetalhadoWMS")
    
    df["DatInicioVolume"] = pd.to_datetime(df["DatInicioVolume"])
    df["DatFimVolume"] = pd.to_datetime(df["DatFimVolume"])
    
    # SKUs distintos por pedido
    skus_por_pedido = df.groupby("CodPedido")["codigo_produto"].nunique().reset_index()
    skus_por_pedido.columns = ["CodPedido", "Qtd_SKUs"]

    # Tempo médio por pedido
    df["tempo_separacao_min"] = (df["DatFimVolume"] - df["DatInicioVolume"]).dt.total_seconds() / 60
    tempo_por_pedido = df.groupby("CodPedido")["tempo_separacao_min"].mean().reset_index()

    # Merge final
    base = pd.merge(skus_por_pedido, tempo_por_pedido, on="CodPedido")

    # Scatter plot
    fig = px.scatter(
        base,
        x="Qtd_SKUs",
        y="tempo_separacao_min",
        title="Quantidade de SKUs vs Tempo de Separação (minutos)",
        labels={
            "Qtd_SKUs": "Quantidade de SKUs distintos",
            "tempo_separacao_min": "Tempo de separação (min)"
        },
        template="plotly_dark"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Dados em tabela
    with st.expander("🔍 Ver dados consolidados"):
        st.dataframe(base, use_container_width=True)
