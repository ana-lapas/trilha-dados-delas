import streamlit as st
import pandas as pd
import requests # Nova biblioteca para enviar o formulário

# Configuração da página
st.set_page_config(page_title="Trilha Dados Delas", page_icon="🌸", layout="wide")

# --- INJEÇÃO DE CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    .stButton>button {
        background-color: #C08BB3; 
        color: white;
        border-radius: 25px; 
        border: none;
        padding: 10px 24px;
        font-weight: 600;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #9B6490; 
        color: white;
        transform: scale(1.05);
    }
    .stAlert {
        border-radius: 15px;
        background-color: #FDF2F8; 
        color: #831843; 
        border-left: 5px solid #C08BB3;
    }
    h1, h2, h3 {
        color: #4A154B; 
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        color: #9B6490;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FDF2F8;
        color: #4A154B;
        border-bottom: 3px solid #C08BB3;
    }
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.title("🌸 Trilha Dados Delas")
st.markdown("""
Oi, mana! 👋 Seja muito bem-vinda à sua jornada em Ciência de Dados! 
Este é o seu espaço seguro para começar. Aqui você encontra recursos gratuitos, verificados e organizados especialmente para mulheres iniciantes da comunidade **Developer Girls**. 
**Sua jornada começa agora! ✨**
""")

# --- BASE DE DADOS ---
dados = {
    'Plataforma': ['FGV', 'FGV', 'Data Science Academy', 'Santander Open Academy', 'Cisco Networking Academy', 'UFMS', 'FGV EMAp'],
    'Curso': [
        'Introdução à Ciência de Dados (60h)',
        'SQL - Structured Query Language',
        'Fundamentos de Data Science e IA (24h)',
        'Introdução à Ciência de Dados (6h)',
        'Data Science Essentials',
        'Tecnólogo em Ciência de Dados (EaD Gratuito)',
        'Graduação em Ciência de Dados e IA'
    ],
    'Foco': ['Conceitos', 'Prática', 'Conceitos', 'Conceitos', 'Conceitos', 'Graduação EaD', 'Carreira'],
    'Link': [
        'https://cursosgratuitos.fgv.br/curso/introducao-a-ciencia-de-dados',
        'https://educacao-executiva.fgv.br/cursos/gratuitos',
        'https://www.datascienceacademy.com.br/cursosgratuitos',
        'https://app.santanderopenacademy.com/pt-BR/course/introduction-to-data-science',
        'https://www.netacad.com/pt/catalogs/learn/data-science',
        'https://vestibular.ufms.br', 
        'https://emap.fgv.br/curso/ciencia-de-dados-e-inteligencia-artificial'
    ]
}

df = pd.DataFrame(dados)

# --- BARRA LATERAL (Filtros) ---
st.sidebar.header("🔍 Encontre o seu perfil")
filtro_foco = st.sidebar.multiselect(
    "Qual o seu momento atual?",
    options=df['Foco'].unique(),
    default=df['Foco'].unique()
)

# Filtrando os dados
df_filtrado = df[df['Foco'].isin(filtro_foco)]

# --- MÉTRICAS (KPIs) ---
col1, col2, col3 = st.columns(3)
col1.metric("Recursos Gratuitos", len(df_filtrado))
col2.metric("Plataformas Parceiras", df_filtrado['Plataforma'].nunique())
col3.metric("Opções de Carreira", "2")

# --- GRÁFICO ---
st.markdown("### Distribuição por Plataforma")
if not df_filtrado.empty:
    contagem = df_filtrado['Plataforma'].value_counts()
    st.bar_chart(contagem, color="#E5989B", height=200) 
else:
    st.warning("Ops! Nenhum recurso encontrado. Tente mudar os filtros na barra lateral.")

st.markdown("---")

# --- CRIAÇÃO DAS ABAS (Agora com 4 abas) ---
aba1, aba2, aba3, aba4 = st.tabs(["🎯 Curadoria", "🎓 UFMS: Ciência de Dados", "🤔 Não é a sua praia?", "💌 Deixe seu Feedback"])

# ABA 1: Curadoria
with aba1:
    st.subheader("Seus Estudos Curados")
    for index, row in df_filtrado.iterrows():
        col_info, col_link = st.columns([3, 1])
        with col_info:
            st.markdown(f"**{row['Plataforma']}** — {row['Curso']} *(Foco: {row['Foco']})*")
        with col_link:
            st.link_button("Acessar 🔗", row['Link'], use_container_width=True)
            
    st.markdown("---")
    st.subheader("📝 Seu Diário de Bordo")
    st.write("Vá marcando aqui conforme for avançando nos estudos:")
    st.checkbox("Semana 1: Entendi o que é Ciência de Dados e dei os primeiros passos")
    st.checkbox("Semana 2: Aprendi os primeiros comandos de SQL")
    st.checkbox("Semana 3: Explorei o ecossistema de IA e Fundamentos")
    st.checkbox("Semana 4: Descobri as opções de graduação (como o EaD da UFMS) e planejei minha carreira")

# ABA 2: UFMS Detalhes
with aba2:
    st.subheader("Descubra o Curso Gratuito da UFMS")
    st.markdown("""
    Sabia que você pode se formar em Ciência dos Dados sem pagar nada? A **UFMS (Universidade Federal de Mato Grosso do Sul)** oferece o curso de Tecnólogo em Ciência dos Dados 100% a distância e gratuito!
    """)
    
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.info("""
        **📋 Dados Oficiais do Curso**
        *   **Unidade:** AGEAD
        *   **Grau:** Tecnólogo (Curso Superior de Tecnologia)
        *   **Modalidade:** A Distância (EaD)
        *   **Código MEC:** 1599606
        *   **Reconhecimento:** Portaria SERES/MEC Nº 662, de 22/09/2025.
        *   **Coordenadora:** Bianca de Almeida Dantas
        """)
    with col_d2:
        st.success("""
        **🚀 O que você vai aprender?**
        A grade curricular é focada no mercado de trabalho e em tecnologias de ponta. Destaques para as disciplinas de:
        *   Mineração de Dados e Modelagem Estatística
        *   Aprendizado de Máquina (Machine Learning)
        *   Redes Neurais e Aprendizado Profundo (Deep Learning)
        *   Processamento de Linguagem Natural (PLN)
        *   Visualização Computacional
        """)
    
    st.warning("🎓 **Fique ligada no Vestibular!** A UFMS abre processo seletivo (vestibular) gratuito todo ano. Acesse o site do vestibular para conferir as datas e garantir sua vaga!")

# ABA 3: Outros Cursos UFMS
with aba3:
    st.subheader("A UFMS tem portas abertas em várias áreas!")
    st.write("Se você descobriu que Ciência de Dados não é o seu momento, não desanime! A AGEAD/UFMS oferece uma variedade de outros cursos superiores gratuitos e 100% a distância. Veja as opções:")
    
    outros_cursos = [
        "Inteligência Artificial", "Educação e Processos de Trabalho: Alimentação Escolar", 
        "Educação e Processos de Trabalho: Secretaria Escolar", "Gestão Comercial", 
        "Gestão de Mídias Sociais Digitais", "Gestão de Recursos Humanos", 
        "Gestão de Serviços Jurídicos e Notariais", "História", 
        "Letras Português e Espanhol", "Pedagogia", "Processos Gerenciais", 
        "Tecnologia da Informação"
    ]
    
    col_e1, col_e2 = st.columns(2)
    for i, curso in enumerate(outros_cursos):
        if i % 2 == 0:
            col_e1.markdown(f"🎓 {curso}")
        else:
            col_e2.markdown(f"🎓 {curso}")

    st.info("💡 **Como ingressar?** Todos esses cursos utilizam o mesmo vestibular gratuito da UFMS.")
    
    # Link Geral solicitado
    st.link_button("🔗 Ver a Lista Completa de Cursos da UFMS", "https://graduacao.ufms.br/cursos?sort=Cursos.modalidade_id&direction=desc", use_container_width=True)

# ABA 4: Feedback
with aba4:
    st.subheader("💌 Conte para a gente!")
    st.write("Sua opinião é super importante para melhorarmos cada vez mais a nossa trilha. Deixe suas dúvidas, sugestões ou elogios!")
    
    # Formulário de Feedback
    with st.form("form_feedback", clear_on_submit=True):
        nome = st.text_input("Seu nome (opcional)")
        email = st.text_input("Seu e-mail (opcional, caso queira retorno)")
        nota = st.slider("De 0 a 10, o quanto você recomendaria esta trilha para uma amiga?", 0, 10, 10)
        mensagem = st.text_area("Mensagem / Sugestão:")
        
        # Botão de enviar
        submit = st.form_submit_button("Enviar Feedback 💜")

        if submit:
            if mensagem: # Validação simples
                formspree_url = "https://formspree.io/f/xljjvzvl"
                
                dados_form = {
                    "Nome": nome if nome else "Anônima",
                    "Email": email if email else "Não informado",
                    "Nota": nota,
                    "Mensagem": mensagem
                }
                
                try:
                    response = requests.post(formspree_url, json=dados_form)
                    if response.status_code == 200:
                        st.success("Obrigada pelo seu feedback! Ele foi enviado com sucesso. 💜")
                    else:
                        st.error("Ops, tivemos um problema ao enviar. Tente novamente mais tarde.")
                except Exception as e:
                    st.error("Erro de conexão. Verifique sua internet.")
            else:
                st.warning("Por favor, escreva uma mensagem antes de enviar. 🥺")

# --- RODAPÉ ---
st.markdown("---")
st.caption("Feito com 💜 por Ana Paula Lapas Leão | Projeto Integrador de Ciência dos Dados II - UFMS Digital (2026.2)")
st.caption("📅 Data de Publicação: 05/11/2026 | Última Atualização: 05/11/2026")