from flask import Flask, render_template
from alunos import Alunos

pagina_nome = 'Lista Alunos'
aluno1 = Alunos('Eduardo Jeremias dos Anjos', 4732097328)
aluno2 = Alunos('Lais hoffman', 4732097328)
lista_alunos = [aluno1, aluno2]

app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html', pagina_nome = pagina_nome, lista=lista_alunos)
app.run()
