# backend/app/seed.py

from datetime import date
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models import Song

# Crear tablas (si no existen aún)
Base.metadata.create_all(bind=engine)

def seed_data():
    db: Session = SessionLocal()

    # Verificamos si ya hay datos
    if db.query(Song).first():
        print("La base de datos ya tiene canciones.")
        db.close()
        return

    songs = [
        Song(
            title="Bohemian Rhapsody",
            genre="Rock",
            artist="Queen",
            discografic="EMI",
            album="A Night at the Opera",
            description="Una de las canciones más icónicas de Queen.",
            album_image="https://upload.wikimedia.org/wikipedia/en/9/9f/Bohemian_Rhapsody.png",
            url_video="https://www.youtube.com/watch?v=fJ9rUzIMcZQ",
            country="Reino Unido",
            release_date=date(1975, 10, 31),
            lyrics="Is this the real life? Is this just fantasy?...",
        ),
        Song(
            title="Shape of You",
            genre="Pop",
            artist="Ed Sheeran",
            discografic="Asylum Records",
            album="÷ (Divide)",
            description="Canción pop de gran éxito mundial en 2017.",
            album_image="https://upload.wikimedia.org/wikipedia/en/4/45/Divide_cover.png",
            url_video="https://www.youtube.com/watch?v=JGwWNGJdvx8",
            country="Reino Unido",
            release_date=date(2017, 1, 6),
            lyrics="The club isn't the best place to find a lover...",
        ),
        Song(
            title="Hips Don't Lie",
            genre="Latin Pop",
            artist="Shakira ft. Wyclef Jean",
            discografic="Epic Records",
            album="Oral Fixation, Vol. 2",
            description="Éxito global que mezcla pop y ritmos latinos.",
            album_image="https://upload.wikimedia.org/wikipedia/en/2/2d/Hips_Don%27t_Lie.png",
            url_video="https://www.youtube.com/watch?v=DUT5rEU6pqM",
            country="Colombia",
            release_date=date(2006, 2, 28),
            lyrics="Ladies up in here tonight, no fighting...",
        ),
    ]

    db.add_all(songs)
    db.commit()
    db.close()
    print("Seed ejecutado correctamente. Canciones insertadas.")

if __name__ == "__main__":
    seed_data()
