import streamlit as st
import pandas as pd
import plotly.express as px
from style.css import inject_custom_css
import os

# Configuração da interface
st.set_page_config(page_title="POC Oriente Farma", layout="wide")
inject_custom_css()

st.title("📦 Análise de Separação de Pedidos - Oriente Farma")
st.markdown(
    "Esta aplicação analisa a relação entre a quantidade "
    "de SKUs distintos por pedido e o tempo de separação "
    "da ordem de serviço, usando os registros de LinhaTempoWMS."
)

# Carrega dados
usar_exemplo = st.checkbox("🔄 Usar dados de exemplo")
if usar_exemplo:
    caminho = os.path.join("data", "levantantamentoDados.xlsx")
    df = pd.read_excel(caminho, sheet_name="LinhaTempoWMS")
else:
    f = st.file_uploader("📁 Faça upload do Excel", type=["xlsx"])
    if not f:
        st.stop()
    df = pd.read_excel(f, sheet_name="LinhaTempoWMS")

# Converte timestamps
df["DatInicioVolume"] = pd.to_datetime(df["DatInicioVolume"])
df["DatFimVolume"]    = pd.to_datetime(df["DatFimVolume"])

# Calcula o tempo de cada volume em minutos
df["tempo_min"] = (
    df["DatFimVolume"] - df["DatInicioVolume"]
).dt.total_seconds() / 60

# Agrega por pedido
base = (
    df.groupby("CodPedido")
      .agg(
          Qtd_SKUs=("QuantidadeSKU", "max"),
          tempo_min=("tempo_min", "sum")
      )
      .reset_index()
)

# Formata para hh:mm:ss
base["tempo_hms"] = (
    pd.to_timedelta(base["tempo_min"], unit="m")
      .astype(str)
      .str.split(".", expand=True)[0]
      .str.replace(r"^0 days ", "", regex=True)
)

# Gráfico de dispersão com hover customizado
fig = px.scatter(
    base,
    x="Qtd_SKUs",
    y="tempo_min",
    custom_data=["tempo_hms"],
    title="Quantidade de SKUs vs Tempo de Separação",
    labels={
        "Qtd_SKUs":  "Quantidade de SKUs distintos",
        "tempo_min": "Tempo total (min)"
    },
    template="plotly_dark"
)
fig.update_traces(
    hovertemplate=(
        "SKUs: %{x}<br>"
        "Tempo: %{customdata[0]}"
    )
)

st.plotly_chart(fig, use_container_width=True)

# Tabela com tempo em hh:mm:ss
with st.expander("🔍 Ver dados consolidados"):
    st.dataframe(
        base[["CodPedido", "Qtd_SKUs", "tempo_hms"]],
        use_container_width=True

    )
