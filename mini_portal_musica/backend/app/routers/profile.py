from fastapi import APIRouter
from .. import schemas

router = APIRouter(
    prefix="/api/profile",
    tags=["Profile"]
)

# Perfil fijo de ejemplo
@router.get("/", response_model=schemas.Profile)
def get_profile():
    return {
        "id": 1,
        "nombre": "Hanna Abril",
        "carrera": "Ingeniería de Software",
        "universidad": "Tu Universidad",
        "email": "hanna.abril@example.com",
        "descripcion": "Estudiante de ingeniería de software apasionada por la programación y la música."
    }
