from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            error = "Todos los campos son obligatorios."
            return render_template('contact.html', error=error)

        # En lugar de solo mostrar un mensaje de éxito, pasamos los datos a la plantilla
        return render_template('contact.html', name=name, email=email, message=message)

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
