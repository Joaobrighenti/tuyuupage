import streamlit as st

# Configuração da página
st.set_page_config(page_title="Tuyuu - Conectando Serviços", page_icon="🔧", layout="wide")
survey_url = "https://docs.google.com/forms/d/e/1FAIpQLScwZpsettrL24qrPWEe2tZ0HEZK8N1cbD8r_WiFSa0IP0BwoA/viewform"

# Estilos personalizados
st.markdown(
    """
    <style>
        /* Fonte e layout */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        * {
            font-family: 'Poppins', sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Fundo e container */
        body {
            background-color: #F4F7F6;
        }

        .container {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 40px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            margin: auto;
            max-width: 900px;
            text-align: center;
        }

        /* Título */
        .title {
            font-size: 48px;
            font-weight: 700;
            color: #1A2E35;
            margin-bottom: 15px;
        }

        /* Subtítulo */
        .subtitle {
            font-size: 24px;
            color: #3C6E71;
            margin-bottom: 30px;
        }

        /* Seções */
        .section-title {
            font-size: 28px;
            font-weight: 600;
            color: #00A896;
            margin-bottom: 20px;
        }

        .section-text {
            font-size: 18px;
            color: #1A2E35;
            line-height: 1.6;
            margin-bottom: 30px;
        }

        /* Benefícios */
        .benefits-list {
            font-size: 18px;
            color: #1A2E35;
            text-align: left;
            margin-left: 40px;
            margin-bottom: 30px;
        }

        .benefit-item {
            margin-bottom: 10px;
        }

        /* Link e botões */
        .survey-button {
            background-color: #00A896;
            color: white;
            padding: 16px 32px;
            font-size: 22px;
            font-weight: 600;
            text-decoration: none;
            border-radius: 10px;
            display: inline-block;
            transition: 0.3s;
            cursor: pointer;
        }

        .survey-button:hover {
            background-color: #028090;
        }

        /* Posicionamento fixo para o botão no topo */
        .top-button {
            position: fixed;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 9999;  /* Aumentei o valor do z-index para garantir que o botão fique em cima */
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown('<div class="title">🚀 Tuyuu - O Novo Jeito de Conectar Serviços! 🔧📱</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Facilitamos a conexão entre clientes e prestadores de serviços, com agilidade e transparência!</div>', unsafe_allow_html=True)

col1, col2 = st.columns([6, 4])

# Coluna 1 - Já existe no código
with col1:
    with st.container():
        st.markdown('<div class="section-title">📌 Sobre a Empresa Tuyuu?</div>', unsafe_allow_html=True)
        
        # Texto com sublinhado e cor customizada
        st.markdown('<div class="section-text">No dia a dia acelerado de hoje, as pessoas precisam resolver tarefas rapidamente, mas ainda é difícil encontrar prestadores de serviços qualificados sem perder tempo com cotações demoradas ou dúvidas sobre preços e qualidade.</div>', unsafe_allow_html=True)
        
        # Palavras sublinhadas e coloridas
        st.markdown('<div class="section-text"><strong><u style="color:#00A896;">O Tuyuu</u></strong> veio para mudar isso! Criamos um <strong><u style="color:#028090;">aplicativo inovador</u></strong> onde clientes encontram prestadores de forma rápida, com valores claros e profissionais qualificados.</div>', unsafe_allow_html=True)
        
        # Explicação sobre a pesquisa
        st.markdown('<div class="section-text">Para tornar o <strong><u style="color:#00A896;">Tuyuu</u></strong> ainda melhor e mais eficiente para todos, precisamos da sua ajuda!</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-text"><strong>Estamos conduzindo uma pesquisa</strong> para entender melhor suas necessidades e melhorar a plataforma de acordo com o que você realmente espera de um serviço como o nosso.</div>', unsafe_allow_html=True)
        
        # Pedindo ajuda com sublinhado e cor
        st.markdown('<div class="section-text">Sua opinião é fundamental para que possamos continuar oferecendo uma experiência que atenda perfeitamente às suas expectativas. Com poucos minutos do seu tempo, você nos ajudará a criar uma plataforma ainda mais útil e prática.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-text"><strong>Contamos com você!</strong> 😊</div>', unsafe_allow_html=True)
        # Benefícios
        st.markdown('<div class="section-title">🔥 Benefícios do Tuyuu</div>', unsafe_allow_html=True)
        st.markdown(
        """
        <ul class="benefits-list">
            <li class="benefit-item">✅ <strong>Acesso rápido a profissionais qualificados</strong></li>
            <li class="benefit-item">✅ <strong>Preços pré-definidos, sem surpresas</strong></li>
            <li class="benefit-item">✅ <strong>Avaliações reais para maior segurança</strong></li>
            <li class="benefit-item">✅ <strong>Conexão instantânea entre cliente e prestador</strong></li>
            <li class="benefit-item">✅ <strong>Maior visibilidade para profissionais do setor</strong></li>
        </ul>
        """,
        unsafe_allow_html=True
    )

# Coluna 2 - MVV
with col2:
    st.markdown('<div class="section-title">🌍 Nossa missão, visão e valores</div>', unsafe_allow_html=True)
    st.markdown(
    """
    <div class="section-text">
    <strong>🎯 Missão</strong><br>
    Tornar a busca e contratação de serviços simples, rápida e acessível para todos.  
    </div>
    <div class="section-text">
    <strong>🚀 Visão</strong><br>
    Ser a principal plataforma de prestação de serviços do Brasil, revolucionando a forma como clientes e profissionais se conectam.  
    </div>
    <div class="section-text">
    <strong>💡 Valores</strong><br>
    🔹 Segurança | 🔹 Conforto | 🔹 Velocidade | 🔹 Valorização dos Profissionais | 🔹 Inovação  
    </div>
    """,
    unsafe_allow_html=True
    )

    # Pedido de pesquisa e link para formulário (fora das colunas)
    st.markdown("---")
    st.write("### 🔎 Queremos sua opinião!")
    st.write("Sua opinião é essencial para criarmos um serviço que realmente atenda às suas necessidades. Responda nossa pesquisa e nos ajude a melhorar! 😊")

    # Botão para pesquisa com link direto
    st.markdown(f'<a href="{survey_url}" target="_blank"><button class="survey-button">📋 Responder à Pesquisa</button></a>', unsafe_allow_html=True)
