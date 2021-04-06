from flask import *
from Algoritma import *

app = Flask(__name__)

file = []
listAdj = []
listCoor = []


@app.route('/search', methods=['POST', 'GET'])
def search():
    file.clear()
    listAdj.clear()
    listCoor.clear()

    file.append(request.data.decode(encoding="utf-8"))
    
    data = file[0]
    listAdj.append(inputToAdjWeb(data))
    listCoor.append(inputToCoorWeb(data))
    node = findAllNode(listAdj[0])

    return render_template('nodes.html', nodeList=node)
    # hasil = AStar('BundaranHI', 'TuguTani', listAdj, listCoor)
    # hasilLatLng = convertToLatLng(hasil, listCoor)
    # res = json.dumps([{"lat": hasil[0], "lng": hasil[1]} for hasil in hasilLatLng])
    # if (request.method == "POST"):
    #     return redirect(url_for('result', res=res))

    # return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    origin = request.form['origin']
    goal = request.form['goal']
    hasil = AStar(goal, origin, listAdj[0], listCoor[0])
    hasilLatLng = convertToLatLng(hasil, listCoor[0])
    res = json.dumps([{"lat": hasil[0], "lng": hasil[1]} for hasil in hasilLatLng])
    return render_template('result.html', res=res)
    # if (request.method == "POST"):
    #     return redirect(url_for('result', res=res))


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)