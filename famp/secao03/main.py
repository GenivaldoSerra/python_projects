from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status


app = FastAPI()


cursos = {
    1: {
        "titulo": "Curso de Python",
        "aulas": 10,
        "horas": 20,
    },
    2: {
        "titulo": "Curso de Django",
        "aulas": 15,
        "horas": 30,
    },
    3: {
        "titulo": "Curso de FastAPI",
        "aulas": 15,
        "horas": 25,
    }
}

@app.get("/cursos")
async def get_cursos():
    return cursos 

@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int):
    try:
        return cursos[curso_id]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso não encontrado"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        debug=True,
        reload=True,
    )