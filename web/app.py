from flask import *
from Algoritma import *

app = Flask(__name__)

@app.route('/search', methods=['POST', 'GET'])
def search():
    data = request.data.decode(encoding="utf-8")
    listAdj = inputToAdjWeb(data)
    listCoor = inputToCoorWeb(data)
<<<<<<< HEAD
    print(listAdj)
    print(listCoor)
    hasil = AStar('GerbangDepan', 'KebunBinatang', listCoor, listAdj)
    print(hasil)
    return jsonify({"Mean": 10.0})
=======
    hasil = AStar('BundaranHI', 'TuguTani', listAdj, listCoor)
    hasilLatLng = convertToLatLng(hasil, listCoor)
    res = json.dumps([{"lat": hasil[0], "lng": hasil[1]} for hasil in hasilLatLng])
    if (request.method == "POST"):
        return redirect(url_for('result', res=res))

    return render_template('index.html')

@app.route('/result')
def result():
    res = request.args['res']
    return render_template('result.html', res=res)

@app.route('/')
def index():
    return render_template('index.html')
>>>>>>> ab3a19554207a3ef889a89efece7ac3b0adb3f9f

if __name__ == "__main__":
    app.run(debug=True)