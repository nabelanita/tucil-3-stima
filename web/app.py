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
    

@app.route('/result', methods=['POST'])
def result():
    origin = request.form['origin']
    goal = request.form['goal']
    hasil = AStar(origin, goal, listAdj[0], listCoor[0])
    dist = hasil[len(hasil)-1]
    hasilLatLng = convertToLatLng(hasil, listCoor[0])
    temp = findAllNode(listAdj[0])
    temp.append("X")
    temp = convertToLatLng(findAllNode(temp), listCoor[0])

    name = findAllNode(listAdj[0])

    coor = convertAdjToLatLng(listAdj[0], listCoor[0])

    nodeNames = json.dumps(name)
    node = json.dumps([{"lat": n[0], "lng": n[1]} for n in temp])
    res = json.dumps([{"lat": hasil[0], "lng": hasil[1]} for hasil in hasilLatLng])
    adjCoor = json.dumps(coor)
    return render_template('result.html', origin=origin, goal=goal, res=res, node=node, dist=dist, nodeNames=nodeNames, adjCoor=adjCoor)



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)