# Usado para dar recomendaciones musicales.

from sqlalchemy.orm import Session
from ..models import Song
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations_ai(db: Session, song_id: int, top_n: int = 5):
    """
    Retorna canciones similares a una canción dada usando IA (TF-IDF + similitud coseno).
    """
    # 1. Traer todas las canciones
    songs = db.query(Song).all()
    
    # 2. Crear DataFrame
    df = pd.DataFrame([{
        "id": s.id,
        "title": s.title,
        "genre": s.genre,
        "artist": s.artist,
        "album": s.album,
        "description": s.description
    } for s in songs])
    
    # 3. Combinar atributos como texto
    df['content'] = df['genre'] + ' ' + df['artist'] + ' ' + df['album'] + ' ' + df['description']
    
    # 4. Vectorizar texto
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['content'])
    
    # 5. Calcular similitud coseno
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # 6. Buscar índice de la canción
    idx = df.index[df['id'] == song_id][0]
    
    # 7. Obtener las top N canciones similares
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]  # excluir la misma canción
    
    song_indices = [i[0] for i in sim_scores]
    recommended_songs = df.iloc[song_indices]
    
    return recommended_songs.to_dict(orient='records')
