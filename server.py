from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    data = {
        "frutilla":int(request.form['strawberry']),
        "mora":int(request.form['raspberry']),
        "manzana":int(request.form['apple']),
        "nombre":request.form['first_name'],
        "apellido":request.form['last_name'],
        "identificacion":request.form['student_id'],
    }
    suma_total = data["frutilla"]+data["mora"]+data["manzana"]
    print ("Cobrando a",data["nombre"],data["apellido"],"por",suma_total, "frutas")
    return render_template("checkout.html", data= data, suma_total=suma_total)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)