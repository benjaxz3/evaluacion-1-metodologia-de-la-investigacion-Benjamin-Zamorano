import streamlit as st
import pandas as pd

# Configuración inicial de la página
st.set_page_config(page_title="Revisión Sistemática - Patrones Rítmicos", layout="wide")

# --- MENÚ LATERAL ---
st.sidebar.title("Navegación")
opciones = [
    "1. Inicio y Contexto", 
    "2. Metodología y PRISMA", 
    "3. Resultados y Metodologías CD", 
    "4. Discusión y Vacíos", 
    "5. IA, Referencias y Anexos"
]
seleccion = st.sidebar.radio("Ir a la sección:", opciones)

# --- 1. INICIO Y CONTEXTO ---
if seleccion == "1. Inicio y Contexto":
    st.title("Modelado y Clasificación de Patrones Rítmicos de Batería mediante Técnicas de Ciencia de Datos: Una Revisión Sistemática")
    
    st.subheader("Integrante")
    st.write("**Nombre:** Benjamín Alonso Zamorano Soto")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Problema de Investigación")
        st.write("""
        El análisis computacional de la batería presenta desafíos únicos. A diferencia de los instrumentos melódicos, 
        los instrumentos de percusión no afinados poseen características tímbricas relativamente simples y formas de 
        interpretación monótonas que dificultan su análisis mediante modelos analíticos tradicionales basados en el tono. 
        El problema central es **cómo modelar de manera objetiva el ritmo musical extraído de señales de audio crudas**, 
        transformando estos patrones en características cuantificables para su clasificación.
        """)
        
    with col2:
        st.subheader("Preguntas de Investigación")
        st.markdown("""
        * **PI1:** ¿Cuáles son las técnicas de procesamiento de señales más efectivas para extraer características rítmicas cuantificables a partir de señales de audio de batería?
        * **PI2:** ¿Qué arquitecturas de *Machine Learning* y *Deep Learning* demuestran mayor precisión en la clasificación y agrupación de dichos patrones rítmicos?
        * **PI3:** ¿Cuáles son las principales aplicaciones (e.g., identificación de intérpretes, educación) y las limitaciones metodológicas actuales en el modelado objetivo del ritmo?
        """)
        
    st.divider()
    st.subheader("Área OCDE y ODS")
    st.info("""
    * **Área OCDE:** 1.02 Ciencias de la Computación e Información (Inteligencia Artificial / Procesamiento de Señales).
    * **Objetivos de Desarrollo Sostenible (ODS):** 
        * **ODS 4 (Educación de Calidad):** Aplicación de estos modelos en entornos inmersivos de Realidad Virtual para mejorar la educación musical.
        * **ODS 9 (Industria, Innovación e Infraestructura):** Desarrollo de nuevas tecnologías computacionales en Recuperación de Información Musical (MIR).
    """)

# --- 2. METODOLOGÍA Y PRISMA ---
elif seleccion == "2. Metodología y PRISMA":
    st.title("Metodología de Revisión")
    
    st.subheader("Estrategia de Búsqueda")
    st.write("**Bases de datos:** Web of Science (WoS) e IEEE Xplore")
    st.write("**Fecha de búsqueda:** 22 de abril de 2026")
    st.code("""
    ("drum percussion" OR "rhythmic pattern") 
    AND 
    ("signal processing" OR "feature extraction" OR "audio analysis") 
    AND 
    ("machine learning" OR "deep learning" OR "classification")
    """, language="sql")

    st.code("""
    ("music information retrieval" AND "machine learning") 
    """, language="sql")
    
    st.divider()
    
    st.subheader("Diagrama PRISMA")
    st.write("A continuación se presenta el flujo de selección de los 8 artículos finales:")
    st.image("prisma.png", caption="Diagrama de flujo PRISMA")
    
    st.markdown("""
    **Resumen del flujo:**
    1. **Identificación:** 1.245 registros (WoS: 925, IEEE: 320).
    2. **Cribado:** Exclusión de 1.226 registros por título y resumen.
    3. **Elegibilidad:** 16 artículos evaluados a texto completo.
    4. **Inclusión:** 8 artículos seleccionados para la síntesis final.
    """)

# --- 3. RESULTADOS Y METODOLOGÍAS CD ---
elif seleccion == "3. Resultados y Metodologías CD":
    st.title("Resultados Principales y Metodologías de Ciencia de Datos")
    
    st.subheader("Metodologías de Ciencia de Datos Encontradas")
    st.markdown("""
    * **Preprocesamiento y Extracción de Features:** Uso dominante de Coeficientes Cepstrales de las Frecuencias de Mel (MFCC) y Espectrogramas Mel.
    * **Algoritmos Clásicos:** K-Nearest Neighbours (K-NN), Random Forest, Linear Discriminant Analysis (LDA) para datos simbólicos y micro-tiempos.
    * **Deep Learning:** Redes Neuronales Recurrentes (GRU), Arquitecturas Residuales (ResNet_50), Convolutional Neural Networks (CNN) acopladas con Redes Kolmogorov-Arnold (KAN), y Vision Transformers (ViT).
    """)
    
    st.divider()

    # NUEVA SECCIÓN DE HALLAZGOS (Agregada en base a nuestro análisis)
    st.subheader("Hallazgos Principales de la Revisión")
    with st.expander("📌 Ver los 5 resultados clave extraídos de la literatura", expanded=True):
        st.markdown("""
        1. **El "Estándar de Oro" (Preprocesamiento):** Las técnicas basadas en tono no sirven para la batería. Los resultados demuestran que los **Espectrogramas de Mel y MFCC** son óptimos para capturar la "envolvente de energía" y los picos correspondientes a los golpes de percusión.
        2. **Eficacia de ML Clásico para Micro-tiempos:** Para datos ya estructurados (como MIDI), los algoritmos clásicos son altamente efectivos. **K-NN** logró un 97% de precisión en reconocimiento de beats y fue el mejor clasificador para identificar las "huellas dactilares" de los bateristas.
        3. **Superioridad del Deep Learning para Audio Crudo:** Para el audio acústico complejo, se requieren arquitecturas profundas. Modelos híbridos (GRU + ResNet_50) alcanzaron **92.5% de precisión**, y nuevas arquitecturas (CNN + KAN) llegaron al **95.74%**.
        4. **Necesidad de Separación de Fuentes:** Antes de clasificar un ritmo desde una pista polifónica (una canción completa), es obligatorio un preprocesamiento de aislamiento. Modelos de atención en frecuencias como **CISM** demostraron ser vitales para esto.
        5. **Impacto Real en Educación:** La aplicación de estas tecnologías de cuantificación rítmica en entornos de Realidad Virtual (VR) demostró mejorar las habilidades técnicas de los estudiantes en un **30%** y reducir significativamente la ansiedad académica.
        """)

    st.divider()
    
    st.subheader("Artículos Incluidos y Resultados")
    # DataFrame con los 8 artículos para visualización interactiva
    data = {
        "Estudio": [
            "Chen (2022)", 
            "Kumar et al.", 
            "Zheng et al. (ICKAN)", 
            "Cunningham et al.", 
            "Zheng et al. (CISM)", 
            "Garg et al.",
            "Garware et al.",
            "Wang (2026)"
        ],
        "Objetivo": [
            "Reconocimiento de ritmo", 
            "Reconocimiento de beats", 
            "Clasificación de instrumentos", 
            "Huellas de bateristas", 
            "Separación de fuentes", 
            "Estimación de tono",
            "Revisión de patrones rítmicos",
            "Educación inmersiva (VR)"
        ],
        "Método CD": [
            "GRU + ResNet_50", 
            "K-NN, Random Forest", 
            "CNN + KAN", 
            "K-NN, GBC", 
            "CNN + RNN", 
            "DenseNet, ViT",
            "Revisión de literatura",
            "Análisis Estadístico / VR"
        ],
        "Accuracy (%)": [92.5, 97.0, 95.7, 85.0, None, 91.6, None, None] # None para estudios sin métrica de clasificación
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    
    st.subheader("Visualización Interactiva: Rendimiento por Modelo")
    st.write("Gráfico comparativo de la precisión (Accuracy / F1-Score) reportada en los estudios principales (se excluyen estudios de revisión y educación):")
    # Dropna elimina automáticamente los que tienen 'None' solo para el gráfico
    df_chart = df.dropna(subset=['Accuracy (%)'])
    st.bar_chart(data=df_chart, x='Estudio', y='Accuracy (%)', use_container_width=True)

# --- 4. DISCUSIÓN Y VACÍOS ---
elif seleccion == "4. Discusión y Vacíos":
    st.title("Discusión y Related Work")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Related Work y Discusión")
        st.write("""
        El estado del arte ha transitado rápidamente de reglas heurísticas hacia enfoques impulsados por datos (*Data-Driven*).
        Existe un contraste interesante entre la eficiencia y la complejidad: algoritmos clásicos como **K-NN y Random Forest** 
        ofrecen alta interpretabilidad y bajos tiempos de computación con datos simbólicos. Sin embargo, cuando se enfrentan a 
        señales de audio polifónicas no separadas, las **arquitecturas profundas (CISM, GRU, KAN)** demuestran su superioridad, 
        logrando extraer relaciones no lineales complejas del espectro temporal-frecuencia.
        """)
        
    with col2:
        st.subheader("Vacíos de Investigación")
        st.error("""
        1. **Identificación de Intérprete desde Audio Crudo:** Estudios de "huellas dactilares" (micro-tiempos) se basan casi exclusivamente en archivos MIDI. Extraer estas huellas directamente desde audio acústico polifónico sigue siendo un desafío.
        2. **Sesgo en Conjuntos de Datos:** Gran parte de los modelos de MIR están calibrados para métricas y música occidental, marginando percusiones folclóricas o de tradiciones orientales.
        3. **Educación en Tiempo Real:** Faltan herramientas interactivas que conecten los modelos predictivos profundos con plataformas inmersivas de Realidad Virtual (VR) para dar retroalimentación pedagógica instantánea.
        """)

# --- 5. IA, REFERENCIAS Y ANEXOS ---
elif seleccion == "5. IA, Referencias y Anexos":
    st.title("Declaraciones, Referencias y Material Suplementario")
    
    with st.expander("🤖 Declaración de Uso de IA (Cumplimiento Unidad 2)"):
        st.write("""
        **Herramientas utilizadas:** Gemini (Google) y NotebookLM (Google).
        * **Etapas del proceso:** Lluvia de ideas, generación de cadenas booleanas, resumen crítico de textos, estructuración de matriz y traducción de código a LaTeX/Python.
        * **Prompts:** Ej. *"Analiza profundamente los papers y excluye los que no tengan relevancia"* y *"Sugiéreme mejoras en el tono técnico"*.
        * **Verificación:** Todo dato técnico y cita bibliográfica fue contrastada manualmente por el autor con los PDF originales para evitar alucinaciones.
        """)
        
    with st.expander("📚 Referencias Principales"):
        st.markdown("""
        1. Chen, B. "Music Audio Rhythm Recognition Based on Recurrent Neural Network", *Wireless Communications and Mobile Computing*, 2022.
        2. Kumar, N. et al. "Musical Beat Recognition using Machine Learning", India.
        3. Zheng, J. et al. "ICKAN: A deep musical instrument classification model...", *Scientific Reports*, 2025.
        4. Cunningham, C. et al. "Drummistic Fingerprints: Unique Drummer Identification...", Ireland.
        5. Zheng, J. et al. "Chinese instrument music source separation...", *EURASIP Journal*, 2025.
        6. Garg, M. et al. "Comparative Analysis of Deep Learning Architectures and ViT...", *Information*, 2023.
        7. Garware, C. P. et al. "Rhythmic Pattern Recognition - A Review", India.
        8. Wang, W. "Enhancing Chinese Percussion Education through Virtual Reality...", China, 2026.
        """)
        
    st.divider()
    st.subheader("📎 Material Suplementario")
    st.info("Puedes acceder a las matrices de extracción, capturas de bases de datos, código LaTeX y registro de prompts en el siguiente repositorio:")
    st.write("👉 **[Enlace al Repositorio de GitHub / Google Drive del Proyecto] (Reemplazar con enlace real)**")
