from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate_client_data',methods=['Post'])
def generate_client_data():

    return jsonify({'message':'Generation of client Data succesfull'})

if __name__ ==" __main__":
    app.run(debug=True)