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

@app.route('/Battlefield5')
def Battlefield5():
    return render_template("Battlefield5.html")

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

@app.route('/MetroExodus')
def MetroExodus():
    return render_template("MetroExodus.html")

@app.route('/DOOM')
def DOOM():
    return render_template("DOOM.html")

@app.route('/EldenRing')
def EldenRing():
    return render_template("EldenRing.html")

@app.route('/DarkSouls3')
def DarkSouls3():
    return render_template("DarkSouls3.html")

@app.route('/Bannerlord')
def Bannerlord():
    return render_template("Bannerlord.html")

@app.route('/KingdomComeDeliverance')
def KingdomComeDeliverance():
    return render_template("KingdomComeDeliverance.html")

@app.route('/KingdomComeDeliverance2')
def KingdomComeDeliverance2():
    return render_template("KingdomComeDeliverance2.html")


@app.route('/ResidentEvilVillage')
def ResidentEvilVillage():
    return render_template("ResidentEvilVillage.html")

@app.route('/RedDeadRedemption2')
def RedDeadRedemption2():
    return render_template("RedDeadRedemption2.html")

@app.route('/TheForest')
def TheForest():
    return render_template("TheForest.html")

@app.route('/Fallout4')
def Fallout4():
    return render_template("Fallout4.html")

@app.route('/CallofDuty')
def CallofDuty():
    return render_template("CallofDuty.html")

@app.route('/HITMAN')
def HITMAN():
    return render_template("HITMAN.html")

@app.route('/AssassinsCreedOdyssey')
def AssassinsCreedOdyssey():
    return render_template("AssassinsCreedOdyssey.html")

@app.route('/AssassinCreedShadows')
def AssassinCreedShadows():
    return render_template("AssassinCreedShadows.html")

@app.route('/GodofWar')
def GodofWar():
    return render_template("GodofWar.html")

@app.route('/BaldurGate3')
def BaldurGate3():
    return render_template("BaldurGate3.html")

@app.route('/Civilization')
def Civilization():
    return render_template("Civilization.html")

#if __name__ == '__main__':
    #app.run(debug=True)
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=False)
