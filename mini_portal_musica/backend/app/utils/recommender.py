# Usado para dar recomendaciones musicales.
# Este módulo implementa un sistema de recomendación basado en contenido usando ML

# Importación de módulos para base de datos y ORM
from sqlalchemy.orm import Session
# Importación del modelo Song desde los modelos locales
from ..models import Song
# Importación de pandas para manipulación de datos tabulares
import pandas as pd
# Importación de sklearn para procesamiento de texto y cálculo de similitud
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Función básica por género - Recomendaciones simples basadas en género
def get_recommendations(db: Session, genre: str, limit: int = 5):
    """
    Obtiene recomendaciones básicas de canciones filtrando por género.
    
    Args:
        db (Session): Sesión de base de datos para realizar consultas
        genre (str): Género musical para filtrar las canciones
        limit (int, optional): Número máximo de canciones a retornar. Default: 5
        
    Returns:
        list[Song]: Lista de objetos Song del género especificado
    """
    # Consultar canciones del género específico con límite de resultados
    return db.query(Song).filter(Song.genre == genre).limit(limit).all()

def get_recommendations_ai(db: Session, song_id: int, top_n: int = 5):
    """
    Retorna canciones similares a una canción dada usando IA (TF-IDF + similitud coseno).
    Sistema de recomendación basado en contenido que analiza características textuales.
    
    Args:
        db (Session): Sesión de base de datos para realizar consultas
        song_id (int): ID de la canción de referencia para buscar similares
        top_n (int, optional): Número de recomendaciones a retornar. Default: 5
        
    Returns:
        list[dict]: Lista de diccionarios con información de las canciones recomendadas
        
    Steps:
        1. Obtener todas las canciones de la base de datos
        2. Crear DataFrame con la información relevante
        3. Combinar atributos en un solo campo de texto
        4. Vectorizar el texto usando TF-IDF
        5. Calcular matriz de similitud coseno
        6. Encontrar la canción de referencia
        7. Obtener las canciones más similares
    """
    
    # 1. Traer todas las canciones de la base de datos
    songs = db.query(Song).all()
    
    # 2. Crear DataFrame con la información estructurada
    # Se extraen los campos relevantes para el análisis de similitud
    df = pd.DataFrame([{
        "id": s.id,                    # ID único de la canción
        "title": s.title,              # Título de la canción
        "genre": s.genre,              # Género musical
        "artist": s.artist,            # Artista o banda
        "album": s.album,              # Álbum al que pertenece
        "description": s.description   # Descripción o características adicionales
    } for s in songs])  # Comprensión de lista para crear diccionarios de cada canción
    
    # 3. Combinar atributos como texto para el análisis TF-IDF
    # Se concatenan todos los campos textuales en un solo string
    df['content'] = df['genre'] + ' ' + df['artist'] + ' ' + df['album'] + ' ' + df['description']
    
    # 4. Vectorizar texto usando TF-IDF (Term Frequency-Inverse Document Frequency)
    # stop_words='english' elimina palabras comunes sin significado (the, and, etc.)
    tfidf = TfidfVectorizer(stop_words='english')
    # Crear matriz TF-IDF donde cada fila es una canción y cada columna es un término
    tfidf_matrix = tfidf.fit_transform(df['content'])
    
    # 5. Calcular similitud coseno entre todas las canciones
    # La similitud coseno mide el ángulo entre los vectores TF-IDF (1 = idénticos, 0 = no relacionados)
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # 6. Buscar índice de la canción de referencia en el DataFrame
    # df['id'] == song_id crea una máscara booleana, [0] toma el primer resultado
    idx = df.index[df['id'] == song_id][0]
    
    # 7. Obtener las top N canciones similares
    # enumerate asigna índices a los scores de similitud
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Ordenar por similitud descendente (las más similares primero)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Excluir la misma canción (índice 0) y tomar las siguientes top_n
    sim_scores = sim_scores[1:top_n+1]  # excluir la misma canción
    
    # Extraer los índices de las canciones recomendadas (sin los scores)
    song_indices = [i[0] for i in sim_scores]
    # Obtener las filas correspondientes del DataFrame
    recommended_songs = df.iloc[song_indices]
    
    # Convertir el DataFrame a lista de diccionarios para retornar
    return recommended_songs.to_dict(orient='records')