
# 💊 POC Oriente Farma – Separação de Pedidos

Esta POC analisa a relação entre a **quantidade de SKUs distintos por pedido** e o **tempo necessário para separação** no centro de distribuição da Oriente Farma.

O objetivo é fornecer insights logísticos, como o **horário-limite ideal para realizar pedidos** sem comprometer o envio no mesmo dia.

---

## ✅ Funcionalidades

- Upload de planilhas Excel (.xlsx) com os dados da separação
- Cálculo automático de:
  - Quantidade de SKUs distintos por pedido
  - Tempo médio de separação (minutos)
- Gráfico de dispersão interativo (Plotly)
- Visual moderno e escuro com Streamlit

---

## 📊 Exemplo de uso

1. Clique em **"Browse files"** e envie sua planilha Excel com a aba `DetalhadoWMS`
2. O app calculará os indicadores e exibirá o gráfico
3. Expanda a seção de dados para ver os resultados em tabela

---

## 🚀 Como executar localmente

```bash
# Clone o repositório
git clone https://github.com/mozartmarin/poc_oriente_farma.git
cd poc_oriente_farma

# Crie o ambiente virtual (se desejar)
python -m venv .venv
.venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Rode o app
streamlit run app.py
```

---

## ☁️ Deploy no Streamlit Cloud

Acesse: https://share.streamlit.io  
Selecione este repositório e o arquivo `app.py` como entrada.

---

## 📁 Estrutura do projeto

```
poc_oriente_farma/
├── app.py
├── requirements.txt
├── README.md
├── style/
│   └── css.py
└── utils/
```

---

## 📬 Contato

Mozart Marin – [@marin.bebold](https://www.instagram.com/marin.bebold)  
Engenheiro de Dados e IA  
