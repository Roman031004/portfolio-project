from flask import Flask, render_template, request
from models import db, Proyect
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)  

@app.route('/proyect')
def proyectos():
    proyect_lista = Proyect.query.all()
    return render_template('proyect.html', proyect=proyect_lista)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        print(f'Mensaje de {nombre} ({email}): {mensaje}')  
        return render_template('contact.html', mensaje_enviado=True)
    return render_template('contact.html', mensaje_enviado=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    proyects = Proyect.query.all()  
    return render_template('portfolio.html', proyects=proyects)  

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
