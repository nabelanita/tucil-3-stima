from flask import *
from test import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    print(request.get_json())
    test(request.get_json())
    return jsonify({"Mean": 10.0})

if __name__ == "__main__":
    app.run(debug=True)