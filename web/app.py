from flask import *
from Input import *
from Algoritma import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    data = request.data.decode(encoding="utf-8")
    listAdj = inputToAdjWeb(data)
    listCoor = inputToCoorWeb(data)
    print(listAdj)
    print(listCoor)
    hasil = AStar('GerbangDepan', 'KebunBinatang', listCoor, listAdj)
    print(hasil)
    return jsonify({"Mean": 10.0})

if __name__ == "__main__":
    app.run(debug=True)