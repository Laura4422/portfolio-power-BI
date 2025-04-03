import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import requests

# Configuration de la page
st.set_page_config(page_title="Portfolio Power BI", page_icon="📊", layout="wide")

# Chargement du CSS personnalisé
def load_css():
    css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Raleway:wght@300&display=swap');
        body {
            background-image: linear-gradient(to right, #ffdde1, #ee9ca7);
            color: #6a1b9a;
            font-family: 'Raleway', sans-serif;
        }
        .stButton>button, .stDownloadButton>button {
            background-color: #ff4081;
            color: white;
            border-radius: 10px;
            padding: 10px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover, .stDownloadButton>button:hover {
            background-color: #e91e63;
            transform: scale(1.05);
        }
        .title {
            font-family: 'Playfair Display', serif;
            text-align: center;
            font-size: 40px;
            color: #880e4f;
            animation: fadeIn 2s;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

load_css()

# Sidebar pour la navigation
st.sidebar.title("📊 Navigation")
st.sidebar.markdown("---")
page = st.sidebar.radio("Aller vers :", ["Présentation", "Projets Power BI", "Mon CV", "Contact"])

# Page Présentation
if page == "Présentation":
    st.markdown("<h1 class='title'>Bienvenue sur mon Portfolio Power BI 📊</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        🎯 **Je suis Laura Sébille**, cheffe de projets spécialisée en marketing, qu'il soit imprimé ou digital. 
        Passionnée par l’univers de la data, j’ai suivi une formation à la Wild Code School pour devenir Data Analyste.
        
        🔹 **Spécialisation :** Gestion de projets marketing & Data Analytics  
        🔹 **Compétences :** Power BI, SQL, Python (Pandas, NumPy), Data Visualization, Storytelling data  
        🔹 **Objectif :** Transformer les données en insights actionnables pour des décisions éclairées.  
        
        Découvrez mes projets en Power BI ci-dessous ! 🚀
        """)
    with col2:
        st.image("profil.JPG", width=250)

# Page Projets Power BI
elif page == "Projets Power BI":
    st.title("📊 Mes Projets Power BI")
    st.write("Projets réalisés dans le cadre de ma formation à la Wild Code School.")

    # Dashboards Power BI mis à jour
    dashboards = {
        "🍷 Étude de marché sur le vin": "https://app.powerbi.com/view?r=eyJrIjoiOGYzMDI0MmEtM2E1Mi00ZDAwLTlhNWMtYTJmZmU0NTFmZDJkIiwidCI6IjM3NmIxOTc2LTQxZmEtNDc4OC05NWIzLWFmZGY3MDFlNzkyNyJ9",
        "💰 Analyse financière": "https://app.powerbi.com/view?r=eyJrIjoiM2MzODQ1ODItZTdmYy00NTcyLWEwYjctMThiN2Y4YWExMmE5IiwidCI6IjM3NmIxOTc2LTQxZmEtNDc4OC05NWIzLWFmZGY3MDFlNzkyNyJ9",
        "🚴 Analyse des trajets Cyclistic": "https://app.powerbi.com/view?r=eyJrIjoiMzdhNzBkMDgtZjlkNS00ODNiLWFiYTAtNjdlYWY0OWMzZTUxIiwidCI6IjM3NmIxOTc2LTQxZmEtNDc4OC05NWIzLWFmZGY3MDFlNzkyNyJ9&pageName=e5b4ea2ba4ac445e5c06",
        "☄️ Analyse des météorites": "https://app.powerbi.com/view?r=eyJrIjoiNzVmMzY4MTYtMTU2NC00YjBlLTgxY2YtYzY0NzAzNDY4ZDgzIiwidCI6IjM3NmIxOTc2LTQxZmEtNDc4OC05NWIzLWFmZGY3MDFlNzkyNyJ9",
        "🎬 Analyse des films IMDB": "https://app.powerbi.com/view?r=eyJrIjoiYWRlM2ZmYzMtNjlhOS00NzgyLTk5NTEtNjA5ODEyNWJkNjczIiwidCI6IjM3NmIxOTc2LTQxZmEtNDc4OC05NWIzLWFmZGY3MDFlNzkyNyJ9"
    }

    for title, link in dashboards.items():
        st.header(title)
        components.iframe(link, height=600)

# Page CV
elif page == "Mon CV":
    st.title("📄 Mon CV")
    st.write("Vous pouvez télécharger mon CV ci-dessous :")
    with open("mon_cv.pdf", "rb") as cv_file:
        st.download_button("📥 Télécharger mon CV", cv_file, file_name="CV_Laura_Sebille.pdf", mime="application/pdf")
    st.write("### 🌟 Compétences :")
    st.write("✅ Power BI - Tableaux de bord interactifs")
    st.write("✅ Python - Pandas, NumPy")
    st.write("✅ SQL - Analyse et requêtage")
    st.write("✅ Data Visualization - Storytelling avec les données")
    st.write("✅ Stratégie Marketing - Digital & imprimé")

# Page Contact
elif page == "Contact":
    st.title("📩 Me Contacter")
    st.write("Vous souhaitez me contacter ? Remplissez le formulaire ci-dessous :")
    nom = st.text_input("💌 Nom")
    email = st.text_input("📧 Email")
    message = st.text_area("💬 Votre message")

    if st.button("Envoyer 💖"):
        formspree_url = "https://formspree.io/f/xwplreag"
        data = {"name": nom, "email": email, "message": message}
        headers = {"Content-Type": "application/json"}
        response = requests.post(formspree_url, json=data, headers=headers)

        if response.status_code == 200:
            st.success("Merci pour votre message ! Je vous répondrai rapidement.")
        else:
            st.error("Oups, une erreur s'est produite. Réessayez plus tard !")

st.sidebar.write("💜 Made with ❤️ using Streamlit")
