from flask import Flask,  render_template, request

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        if(request.form["num1"] != "" and request.form["num2"] != ""):
            if (request.form["opc"] == "soma"):
                soma = int(request.form["num1"]) + int(request.form["num2"])
                return {
                    "Resultado" : str(soma)
                }

            elif (request.form["opc"] == "subtracao"):
                subtracao = int(request.form["num1"]) - int(request.form["num2"])
                return {
                    "Resultado" : str(subtracao)
                }

            elif (request.form["opc"] == "divisao"):
                divisao = int(request.form["num1"]) // int(request.form["num2"])
                return {
                    "Resultado" : str(divisao)
                }

            elif (request.form["opc"] == "multi"):
                multi = int(request.form["num1"]) * int(request.form["num2"])
                return {
                    "Resultado" : str(multi)
                }
        else:
            return {
                "Resultado" : "Informe um valor válido!"
                }

#@app.route("/<int:id>")
#def home_id(id):
#   return str(id+1)

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")



app.run(port=5000, debug=True)    

