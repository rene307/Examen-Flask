from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculo", methods=["GET", "POST"])
def calculo_compras():
    if request.method == "POST":
        # Lógica para manejar los datos del formulario
        nombre = request.form.get("nombre")
        edad = int(request.form.get("edad"))
        cantidad_tarros = int(request.form.get("cantidad_tarros"))

        # Cálculos
        precio_unitario = 90000
        total_sin_descuento = cantidad_tarros * precio_unitario

        # Aplicar descuentos
        if edad >= 60:
            descuento = total_sin_descuento * 0.30
        elif cantidad_tarros >= 10:
            descuento = total_sin_descuento * 0.25
        else:
            descuento = 0

        total_a_pagar = total_sin_descuento - descuento

        # Mostrar resultados
        return render_template("resultados.html",
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               descuento=descuento,
                               total_a_pagar=total_a_pagar)

    # Si es GET, mostrar el formulario
    return render_template("calculo.html")




@app.route("/formulariob", methods=["GET", "POST"])
def mostrar_formulariob():
    message = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"Datos recibidos: Usuario={username}, Contraseña={password}")

        USERS = {
            "juan": {"password": "1234", "role": "Administrador"},
            "pepe": {"password": "5678", "role": "Usuario"}
        }

        user = USERS.get(username)
        if user and user["password"] == password:
            role = user["role"]
            message = f"Bienvenido {role} {username}"
        else:
            message = "Usuario o contraseña incorrectos."

    return render_template("formulariob.html", message=message)




if __name__ == "__main__":
    app.run(debug=True)
