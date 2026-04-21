from iniciar import app
from flask import render_template

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/agendamento')
def agendamento():
    return render_template('agendamento.html')

@app.route('/servicos')
def servicos():
    return render_template('serviços.html')

@app.route('/finalizar')
def finalizar():
    return render_template('final.html')