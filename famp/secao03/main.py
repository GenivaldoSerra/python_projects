from fastapi import FastAPI


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
    return cursos[curso_id]
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        debug=True,
        reload=True,
    )