import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration de la page
st.set_page_config(
    page_title="Analyse des Forages Miniers",
    layout="wide",  # Utilisation de toute la largeur
    initial_sidebar_state="expanded",
)

# Titre principal
st.title("Analyse des Données de Forages Miniers")

# Création des onglets
tab1, tab2, tab3, tab4 = st.tabs(["📂 Importer les données", "👁️ Aperçu", "📊 Statistiques", "🌐 Visualisation 3D"])

# Variables globales pour stocker les données
collars, survey = None, None

# Onglet 1 : Importer les données
with tab1:
    st.header("📂 Importer vos fichiers CSV")
    collars = st.file_uploader("Fichier des Collars", type=["csv"])
    survey = st.file_uploader("Fichier du Survey", type=["csv"])
    if collars or survey:
        st.success("Fichiers chargés avec succès !")
    else:
        st.warning("Veuillez importer les fichiers nécessaires.")

# Onglet 2 : Aperçu des données
with tab2:
    st.header("👁️ Aperçu des Données")
    if collars:
        df_collars = pd.read_csv(collars)
        st.subheader("Données des Collars")
        st.dataframe(df_collars)
    else:
        st.info("Importez un fichier des Collars pour afficher les données.")
    
    if survey:
        df_survey = pd.read_csv(survey)
        st.subheader("Données du Survey")
        st.dataframe(df_survey)
    else:
        st.info("Importez un fichier du Survey pour afficher les données.")

# Onglet 3 : Statistiques comparatives
with tab3:
    st.header("📊 Statistiques Comparatives")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Collars")
        if collars:
            st.write(df_collars.describe())
        else:
            st.info("Importez un fichier des Collars pour afficher les statistiques.")

    with col2:
        st.subheader("Survey")
        if survey:
            st.write(df_survey.describe())
        else:
            st.info("Importez un fichier du Survey pour afficher les statistiques.")

# Onglet 4 : Visualisation 3D
with tab4:
    st.header("🌐 Visualisation 3D des Forages")
    if collars:
        df_collars = pd.read_csv(collars)
        fig = px.scatter_3d(
            df_collars,
            x="X",  # Remplacez par la colonne correspondant à l'axe X
            y="Y",  # Remplacez par la colonne correspondant à l'axe Y
            z="Z",  # Remplacez par la colonne correspondant à l'axe Z
            color="Elevation",  # Remplacez par une colonne pour la couleur
            title="Visualisation 3D des Collars",
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Importez un fichier des Collars pour générer la visualisation 3D.")