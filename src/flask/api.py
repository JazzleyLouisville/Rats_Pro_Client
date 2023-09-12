from flask import Flask, request, jsonify
# from data_processing import filter_client_details
from src.data_processing import filter_client_details
from src.utils import log_info
app = Flask(__name__)

@app.route('/generate_client_data',methods=['Post','GET'])
def generate_client_data():
    if request.method == 'GET':
        
        df_obj = filter_client_details("../../client_data/dataset_one.csv","../../client_data/dataset_two.csv")
        group_by_id = df_obj.groupby('client_identifier').apply(lambda x: x.drop('client_identifier', axis=1).to_dict(orient='records')).reset_index(name='data_client')
        return jsonify(group_by_id.to_dict(orient='records'))

    if request.method == 'POST':
        countries = request.json.get('countries', [])

        df_obj = filter_client_details("../../client_data/dataset_one.csv","../../client_data/dataset_two.csv",countries)
        group_by_id = df_obj.groupby('client_identifier').apply(lambda x: x.drop('client_identifier', axis=1).to_dict(orient='records')).reset_index(name='data_client')
        return jsonify(group_by_id.to_dict(orient='records'))

if __name__ ==" __main__":
    app.run(debug=True)
