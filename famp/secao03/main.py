from typing import Optional

from fastapi import FastAPI, HTTPException, Path, Query, Response, status

from models import Curso

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
async def get_curso(curso_id: int = Path(default=None, title="O ID do curso", description="Deve ser entre 1 2 3", gt=0, le=3)):
    try:
        return cursos[curso_id]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso não encontrado"
        )


@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    id: int = len(cursos) + 1
    cursos[id] = curso
    del curso.id
    return curso


@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Curso não encontrado com o id {curso_id}'
        )


@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Curso não encontrado com o id {curso_id}'
        )
        
@app.get('/calculadora')
async def calcular(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), c: Optional[int] = None):
    soma: int = a + b
    if c:
        soma = soma + c
    return {"resultado": soma}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        debug=True,
        reload=True,
    )
