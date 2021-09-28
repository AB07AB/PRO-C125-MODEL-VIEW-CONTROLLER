from flask import Flask, jsonify, request 
from classyFire import get_prd

app = Flask(__name__)
@app.route('/predict-alphabet',methods=["POST"])

def prd_data():
    image = request.files.get('alphabet')
    prd = get_prd(image)
    return jsonify({
        "prediction":
        prd
    }),200

if __name__ == "__main__":
    app.run(debug=True)