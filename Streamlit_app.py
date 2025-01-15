import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger le dataset des voitures
df = sns.load_dataset("mpg").dropna()

# Titre de l'application
st.title("Analyse des Voitures par Région")

# Boutons pour filtrer par région
region = st.radio("Choisissez une région :", ("Toutes", "US", "Europe", "Japan"))

# Filtrer les données selon la région
if region != "Toutes":
    df = df[df["origin"] == region.lower()]

# Analyse de corrélation
st.header("Analyse de Corrélation")
corr_matrix = df.corr(numeric_only=True)
st.write("Matrice de corrélation :")
st.dataframe(corr_matrix)

# Heatmap
st.subheader("Heatmap de Corrélation")
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
st.pyplot(plt)

# Analyse de distribution
st.header("Analyse de Distribution")
col_to_analyze = st.selectbox(
    "Sélectionnez une colonne numérique à analyser :",
    df.select_dtypes(include=["float", "int"]).columns
)

st.subheader(f"Distribution de {col_to_analyze}")
plt.figure(figsize=(10, 6))
sns.histplot(df[col_to_analyze], kde=True, bins=30, color="blue")
plt.title(f"Distribution de {col_to_analyze}")
st.pyplot(plt)

# Diagramme de dispersion
st.subheader("Relation entre deux variables")
col_x = st.selectbox("Sélectionnez une colonne pour l'axe X :", df.columns)
col_y = st.selectbox("Sélectionnez une colonne pour l'axe Y :", df.columns)

if col_x != col_y:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=col_x, y=col_y, hue="origin")
    plt.title(f"Relation entre {col_x} et {col_y}")
    st.pyplot(plt)
