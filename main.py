# Importar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Resultados del formulario
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # obtener la imagen seleccionada
        selected_image = request.form.get('image-selector')

        # Asignación #2. Recepción del texto
        texto1=request.form.get("textTop")
        texto2=request.form.get("textBottom")
        color=request.form.get("color-selector")
        

        # Assignment #3. Receiving the text's positioning

        # Asignación #3. Recepción del posicionamiento del texto
        

        return render_template('index.html', 
                               # Visualización de la imagen seleccionada
                               selected_image=selected_image, 

                               # Asignación #2. Visualización del texto
                               texto1=texto1,
                               texto2=texto2,
                               color=color,

                               #  Asignación #3. Visualización del color
                               
                               
                               # Asignación #3. Visualización de la posición del texto


                               )
    else:
        # Mostrar la primera imagen por defecto
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
