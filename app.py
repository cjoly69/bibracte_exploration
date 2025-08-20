
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Exploration Bibracte", layout="wide")

st.title("Exploration des opérations archéologiques à Bibracte")
st.markdown("""
### Présentation

Ce tableau de bord présente un jeu de données **fictif**, inspiré des campagnes de terrain à Bibracte entre 2017 et 2021.  
Les opérations ont été reconstruites à partir des exemples documentés dans l'article suivant :

🔗 [Opérations archéologiques à Bibracte (RAE, 2021)](https://journals.openedition.org/rae/17199)

Vous pouvez explorer les données par **année**, **type d’intervention**, ou **responsable**.
""")


# Charger les données
df = pd.read_csv("base_bibracte.csv")

# Filtres
annees = st.multiselect("Filtrer par année :", sorted(df["annee"].unique()), default=sorted(df["annee"].unique()))
types = st.multiselect("Filtrer par type d'intervention :", df["type"].unique(), default=df["type"].unique())

df_filtered = df[df["annee"].isin(annees) & df["type"].isin(types)]

# Affichage tableau
st.subheader("Tableau des opérations")
st.dataframe(df_filtered)

# Graphique : surface par année
st.subheader("Surface totale par année")
fig_annee = px.bar(
    df_filtered.groupby("annee")["surface_m2"].sum().reset_index(),
    x="annee", y="surface_m2",
    labels={"annee": "Année", "surface_m2": "Surface totale (m²)"},
    title="Surface fouillée ou prospectée par année"
)
st.plotly_chart(fig_annee, use_container_width=True)

# Graphique : répartition par type
st.subheader("Répartition par type d'intervention")
fig_type = px.pie(
    df_filtered,
    names="type",
    values="surface_m2",
    title="Part relative des interventions par type (en surface)"
)
st.plotly_chart(fig_type, use_container_width=True)

# Bouton de téléchargement
st.subheader("Télécharger les données")

with open("base_bibracte.csv", "rb") as f:
    st.download_button(
        label="📥 Télécharger le fichier CSV",
        data=f,
        file_name="base_bibracte.csv",
        mime="text/csv"
    )
