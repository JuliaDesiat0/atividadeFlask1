from flask import Flask, render_template

class Programar:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

class Futebol:
    def __init__(self, nome, tipo, numero):
        self.nome = nome
        self.tipo = tipo
        self.numero = numero

class Viagem:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

app = Flask(__name__)

# DINAMIZANDO OS VALORES
lista = []
lista2 = []
lista3 = []

@app.route('/futebol')
def mostrar_futebol():
    f1 = Futebol('Jaqueline Ribeiro','Atacante', '9')
    f2 = Futebol('Giovanna Campiolo','Zagueira', '2')
    f3 = Futebol('Luana Bertolucc','Meia', '6')
    lista2 = [f1, f2, f3]
    return render_template("atividade2.html", Titulo="As melhores do Corinthians:", ListaFut=lista2)

@app.route('/programar')
def mostrar_programar():
    p1 = Programar("Curso básico", 150.00)
    p2 = Programar("Curso avançado", 250.00)
    p3 = Programar("Curso completo", 350.00)
    lista = [p1, p2, p3]
    return render_template("atividade1.html", Titulo="Cursos: ", ListaCurso=lista)

@app.route('/viagem')
def mostrar_viagem():
    v1 = Viagem("Destino 1: Paris, França", "Paris, a cidade do amor, é famosa por sua arquitetura deslumbrante, museus renomados como o Louvre e monumentos icônicos como a Torre Eiffel. Não deixe de explorar os encantadores bairros de Montmartre e Saint-Germain.")
    v2 = Viagem("Destino 2: Tóquio, Japão", "Tóquio, a capital do Japão, é uma metrópole vibrante, repleta de arranha-céus modernos, templos antigos, lojas de tecnologia e uma rica cultura. Visite o Mercado de Tsukiji, explore o bairro de Akihabara e maravilhe-se com o Santuário Meiji.")
    v3 = Viagem("Destino 3: Rio de Janeiro, Brasil", "O Rio de Janeiro, conhecido por suas deslumbrantes praias como Copacabana e Ipanema, é uma cidade cheia de energia e beleza natural. Aproveite o Pão de Açúcar, visite o Cristo Redentor e dance ao som do samba na Lapa.")
    lista3 = [v1, v2, v3]
    return render_template("atividade3.html", Titulo="Viagens: ", ListaCurso=lista3)


@app.route('/')
def inicio():
    return 'Começando'

if __name__ == '__main__':
    app.run()