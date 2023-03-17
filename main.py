from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello_world():
    return {"message":"servidor ejecutandose"}

usuarios = [
    {'_id':1,'username': 'reinel', 'password': 'quiz'},
    {'_id':2,'username': 'james', 'password': 'jajaja'},
    {'_id':3,'username': 'johan', 'password': 'pina'},
    {'_id':4,'username': 'camilo', 'password': '1234'},
    {'_id':5,'username': 'chatgpt', 'password': 'version4'},
]

@app.get("/users/all/")
def listar_allUsers():
    return usuarios

@app.get("/users/unique/{id_usuario}")
def listar_justOne(id_usuario: int):
    #Listar solo un usuario
    for user in usuarios:
        if user['_id'] == id_usuario:
            return user
    return ['message', 'usuario no encontrado']    
    
        