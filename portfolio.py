import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import requests

# Configuration de la page avec un fond personnalisé et animations
st.set_page_config(page_title="Portfolio Power BI", page_icon="📊", layout="wide")

# Définition du CSS pour un style original et élégant avec animations
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
        .sidebar .sidebar-content {
            background-color: #f8bbd0;
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
        🎯 **Je suis Laura Sébille**, cheffe de projets spécialisée en marketing, qu'il soit imprimé ou digital. Forte d'une expertise en gestion de projets, j’ai piloté des campagnes et stratégies marketing pour des marques variées, toujours avec l’ambition d’optimiser la performance et l’impact.
        
        📊 Passionnée par l’univers de la data et convaincue de sa puissance pour éclairer les décisions, j’ai suivi une formation à la Wild Code School pour devenir Data Analyste. Aujourd’hui, je fusionne mes compétences en marketing avec l’analyse de données pour créer des tableaux de bord interactifs et orientés business.
        
        🔹 **Spécialisation :** Gestion de projets marketing & Data Analytics  
        🔹 **Compétences :** Power BI, SQL, Python (Pandas, NumPy), Data Visualization, Storytelling data, Stratégie marketing digital et imprimé  
        🔹 **Mon approche :** Allier créativité et rigueur analytique pour transformer les données en insights actionnables. Mon objectif est de permettre aux entreprises de prendre des décisions éclairées grâce à une visualisation intuitive et efficace des données.
        
        Découvrez mes projets et mon expertise en Power BI !
        """)
    with col2:
        st.image("profil.jpg", width=250)

# Page Projets Power BI
elif page == "Projets Power BI":
    st.title("📊 Mes Projets Power BI")
    st.write("Tous ces projets sont fictifs et ont été réalisés dans le cadre de ma formation à la Wild Code School.")
    
    # Dashboards Power BI
    dashboards = {
        "🔍 Étude de marché - Vin": "https://app.powerbi.com/reportEmbed?reportId=deb227d8-62fb-4ec3-aa2d-05b9cfe84047&autoAuth=true&ctid=376b1976-41fa-4788-95b3-afdf701e7927",
        "📈 Analyse des ventes": "https://app.powerbi.com/reportEmbed?reportId=8dc8f6da-4a5e-4d6d-b9e9-d9f3519523a2&autoAuth=true&ctid=376b1976-41fa-4788-95b3-afdf701e7927",
        "💳 Étude comportementale clients": "https://app.powerbi.com/reportEmbed?reportId=725a71b4-55aa-4ef7-b030-4c58dd6bcf72&autoAuth=true&ctid=376b1976-41fa-4788-95b3-afdf701e7927",
        "🌍 Dashboard Impact Environnemental": "https://app.powerbi.com/reportEmbed?reportId=19c7a6c8-b6c3-4753-a342-ecce20097742&autoAuth=true&ctid=376b1976-41fa-4788-95b3-afdf701e7927",
        "🛒 Analyse e-commerce": "https://app.powerbi.com/reportEmbed?reportId=e7decbe6-8816-42f2-bda2-951fdfb0066d&autoAuth=true&ctid=376b1976-41fa-4788-95b3-afdf701e7927"
    }
    
    for title, link in dashboards.items():
        st.header(title)
        components.iframe(link, height=600)

# Page CV
elif page == "Mon CV":
    st.title("📄 Mon CV")
    st.write("Vous pouvez télécharger mon CV ci-dessous :")
    with open("mon_cv.pdf", "rb") as cv_file:
        st.download_button("📥 Télécharger mon CV", cv_file, file_name="CV_TonNom.pdf", mime="application/pdf")
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
