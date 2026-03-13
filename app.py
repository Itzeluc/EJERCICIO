import streamlit as st

# Configuración de la página
st.set_page_config(page_title="IA y Salud Mental", layout="centered")

# CSS personalizado para diseño moderno y elegante
st.markdown("""
    <style>
    .main {
        background-color: #fdfdfd;
    }
    .medium-text {
        font-size: 1.15rem !important;
        line-height: 1.6;
        color: #2c3e50;
        text-align: justify;
    }
    .quote-text {
        text-align: right;
        font-style: italic;
        color: #7f8c8d;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    h1 {
        color: #1a1a1a;
        font-family: 'Helvetica Neue', sans-serif;
        border-bottom: 2px solid #3498db;
        padding-bottom: 10px;
    }
    h2 {
        color: #2980b9;
        margin-top: 2rem;
    }
    .ref-section {
        font-size: 0.9rem;
        color: #555;
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        margin-top: 3rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Título del artículo ---
st.markdown("# ¿Un psicólogo en tu bolsillo? Luces y sombras de la IA generativa frente a la ansiedad [cite: 2]")

# --- Frase motivadora ---
st.markdown('<p class="quote-text">Tu mente es el territorio y la innovación la herramienta; <br> el verdadero poder de cambio siempre reside en la valentía de conocerte a ti mismo. [cite: 4, 5]</p>', unsafe_allow_html=True)

# --- Cuerpo del artículo ---
st.markdown('<div class="medium-text">', unsafe_allow_html=True)

st.write("En la última década, la ansiedad ha dejado de ser una preocupación individual para convertirse en un desafío de salud pública global. [cite: 9]")
st.write("Se ha consolidado como una de las principales causas de discapacidad y pérdida de productividad en la población activa. [cite: 10]")
st.write("A pesar de que existen tratamientos efectivos, factores como el alto costo de la terapia, la falta de profesionales en zonas rurales y el estigma social impiden que muchas personas reciban ayuda oportuna. [cite: 11]")
st.write("En este escenario, la Inteligencia Artificial (IA) generativa surge como una herramienta disruptiva que promete democratizar el cuidado de la salud mental. [cite: 12] Pero, ¿qué tan sólida es esta promesa y cuáles son sus riesgos? [cite: 13]")

st.markdown("## El potencial: ¿Por qué la IA funciona para la ansiedad? [cite: 14]")
st.write("La mayoría de los chatbots actuales no operan al azar; su sustento teórico es la Terapia Cognitivo-Conductual (TCC). [cite: 15]")
st.write("Esta terapia se centra en identificar y reestructurar patrones de pensamiento catastróficos, algo que, por su naturaleza protocolizada, es ideal para ser traducido a algoritmos de respuesta. [cite: 16]")

st.markdown("## Las ventajas de un 'entrenador de bolsillo' [cite: 17]")
st.write("El uso de estos agentes conversacionales ofrece beneficios que el sistema tradicional difícilmente puede igualar: [cite: 18]")
st.markdown("""
* **Disponibilidad 24/7 e inmediatez:** El apoyo está presente en el momento exacto de una crisis de pánico o estrés, sin importar el horario. [cite: 19]
* **Anonimato y reducción del estigma:** Al interactuar con una máquina, muchos pacientes se sienten libres del juicio social, lo que facilita una mayor apertura emocional. [cite: 20]
* **Alianza terapéutica digital:** Sorprendentemente, los estudios indican que los usuarios pueden desarrollar un vínculo de confianza con la IA, sintiéndose validados por sus respuestas empáticas. [cite: 21]
* **Personalización profunda:** A diferencia de los chatbots antiguos que eran rígidos, la IA generativa (como GPT-4) adapta su tono, metáforas y sugerencias a la historia específica del usuario. [cite: 22]
""")

st.write("Incluso se están explorando fronteras como la Realidad Virtual (RV) asistida por IA. [cite: 23] Esta combinación permite que personas con ansiedad social practiquen interacciones en escenarios simulados y seguros, reduciendo la fobia social hasta en un 20% en periodos breves. [cite: 24]")

st.markdown("## La otra cara de la moneda: Riesgos y desafíos éticos [cite: 25]")
st.write("No todo es optimismo. La implementación de la IA en la salud mental plantea dilemas profundos que la comunidad científica analiza con cautela. [cite: 26]")

st.markdown("### El peligro de las 'alucinaciones' y la seguridad clínica [cite: 27]")
st.write("Uno de los mayores retos técnicos son las 'alucinaciones' de la IA, donde el sistema genera información que parece coherente pero es incorrecta o peligrosa. [cite: 28] En un contexto de salud mental, una instrucción errónea podría tener consecuencias graves. [cite: 29]")
st.write("Además, existe el riesgo de que la IA no detecte señales sutiles de ideación suicida o autolesión, lo que hace imperativo contar con protocolos de derivación inmediata a profesionales humanos. [cite: 30]")

st.markdown("### Privacidad y persistencia [cite: 31]")
st.write("La confidencialidad es la piedra angular de la psicología. El uso de datos sensibles por parte de empresas tecnológicas genera preocupaciones legítimas sobre la protección de la privacidad. [cite: 32]")
st.write("Por otro lado, la evidencia científica actual es limitada en el tiempo. [cite: 33] Aunque se observa una reducción de síntomas en las primeras semanas, aún no sabemos si estos efectos perduran una vez que el 'efecto de novedad' tecnológica desaparece. [cite: 34]")

st.markdown("## El Modelo de Cuidado Escalonado: Una solución híbrida [cite: 35]")
st.write("La ciencia actual no sugiere que la IA deba reemplazar a los psicólogos, sino que debe integrarse en un modelo de cuidado escalonado. [cite: 36, 37]")
st.markdown("""
* **Primera línea:** Los chatbots actúan como apoyo preventivo y de autogestión para personas con síntomas leves o moderados. [cite: 38]
* **Segunda línea:** Los profesionales humanos se concentran en los casos de mayor complejidad clínica y supervisan el uso de la tecnología. [cite: 39]
""")

st.markdown("## Conclusión [cite: 40]")
st.write("El impacto de la IA generativa en la sintomatología de la ansiedad es, hasta ahora, significativamente positivo. [cite: 41]")
st.write("Representa un cambio de paradigma que ofrece una mano amiga a quienes históricamente han estado excluidos del sistema de salud. [cite: 42]")
st.write("Sin embargo, para que esta herramienta sea realmente efectiva a largo plazo, debe avanzar bajo un marco de responsabilidad ética, garantizando que el bienestar del individuo siempre esté por encima de la eficiencia tecnológica. [cite: 43]")

st.markdown('</div>', unsafe_allow_html=True)

# --- Referencias ---
st.markdown('<div class="ref-section">', unsafe_allow_html=True)
st.markdown("### Referencias [cite: 45]")
st.write("* Camones, V., Cisneros, P. y Quevedo, D. (2025). Del miedo a la confianza: Realidad Virtual y ChatGPT-4 en el tratamiento de la ansiedad social. [cite: 46]")
st.write("* Farzan, M., Ebrahimi, H., Pourali, M. y Sabeti, F. (2024). Artificial Intelligence-Powered Cognitive Behavioral Therapy Chatbots, a Systematic Review. [cite: 47]")
st.write("* Ferreira, D. S., et al. (2024). Uso do chatbot no enfrentamento da ansiedade: uma revisão integrativa. [cite: 48]")
st.write("* Heinz, M. V., et al. (2025). Randomized Trial of a Generative AI Chatbot for Mental Health Treatment. [cite: 49]")
st.write("* Joshi, A. C., Ghogare, A. S. y Madavi, P. B. (2025). Systematic review of artificial intelligence enabled psychological interventions for depression and anxiety. [cite: 50, 51]")
st.write("* Klos, M. C., et al. (2021). Artificial Intelligence-Based Chatbot for Anxiety and Depression in University Students. [cite: 52]")
st.write("* Lima Neto, J. G. F. y Castro, A. F. C. (2025). Eficácia de programas de inteligência artificial com aplicação de chatbots no auxílio ao cuidado a saúde mental. [cite: 53, 54]")
st.write("* Manole, A., et al. (2024). An Exploratory Investigation of Chatbot Applications in Anxiety Management. [cite: 55]")
st.write("* Pavlopoulos, A., Rachiotis, T. y Maglogiannis, I. (2024). An Overview of Tools and Technologies for Anxiety and Depression Management Using AI. [cite: 56]")
st.markdown('</div>', unsafe_allow_html=True)
