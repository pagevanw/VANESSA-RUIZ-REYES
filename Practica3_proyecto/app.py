from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('cuadrado.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    lado = float(request.form['lado'])

    area = lado * lado
    perimetro = 4 * lado

    return render_template(
        'cuadrado.html',
        area=area,
        perimetro=perimetro
    )

if __name__ == '__main__':
    app.run(debug=True)