from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("sait.html")

@app.route('/sait')
def index2():
    return render_template("sait.html")

@app.route('/stalker2')
def stalker2():
    return render_template("stalker2.html")

@app.route('/cyberpunk2077')
def cyberpunk():
    return render_template("cyberpunk2077.html")

@app.route('/hogwarts')
def hogwarts():
    return render_template("hogwarts.html")

@app.route('/hoi4')
def hoi4():
    return render_template("hoi4.html")

@app.route('/warthunder')
def warthunder():
    return render_template("warthunder.html")

@app.route('/chivalry2')
def chivalry2():
    return render_template("chivalry2.html")

@app.route('/battlefield1')
def battlefield1():
    return render_template("battlefield1.html")

@app.route('/buckshotroulette')
def buckshotroulette():
    return render_template("buckshotroulette.html")

@app.route('/darkanddarker')
def darkanddarker():
    return render_template("darkanddarker.html")

@app.route('/squad')
def squad():
    return render_template("squad.html")

@app.route('/silenthill2')
def silenthill2():
    return render_template("silenthill2.html")

@app.route('/witcher3')
def witcher3():
    return render_template("witcher3.html")

@app.route('/Skyrim5')
def Skyrim5():
    return render_template("Skyrim5.html")

@app.route('/Choice of Life')
def Choice():
    return render_template("Choice of Life.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

