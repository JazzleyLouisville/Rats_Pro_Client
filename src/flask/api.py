from flask import Flask, request, jsonify, send_file
# from data_processing import filter_client_details
from ..data_processing import filter_client_details
from ..utils import log_info, save_csv
app = Flask(__name__)

@app.route('/generate_client_data',methods=['POST','GET'])
def generate_client_data():
    if request.method == 'GET':
        
        df_obj = filter_client_details("../../client_data/dataset_one.csv","../../client_data/dataset_two.csv")
        group_by_id = df_obj.groupby('client_identifier').apply(lambda x: x.drop('client_identifier', axis=1).to_dict(orient='records')).reset_index(name='data_client')
        return jsonify(group_by_id.to_dict(orient='records'))

    if request.method == 'POST':
        countries = request.json.get('countries', [])
        
        if not countries:
            countries = ['United States','United Kingdom','France','Netherlands']
        df_obj = filter_client_details("../../client_data/dataset_one.csv","../../client_data/dataset_two.csv",countries)
        group_by_id = df_obj.groupby('client_identifier').apply(lambda x: x.drop('client_identifier', axis=1).to_dict(orient='records')).reset_index(name='data_client')
        save_csv(df_obj,"api")
        return jsonify(group_by_id.to_dict(orient='records')) , send_file("../../client_data/filtered_client_data.csv")

from flask import Flask, request, jsonify, send_file
# from data_processing import filter_client_details
from ..data_processing import filter_client_details
from ..utils import log_info, save_csv
app = Flask(__name__)

@app.route('/generate_client_data',methods=['POST','GET'])
def generate_client_data():
    if request.method == 'GET':
        
        # df_obj = filter_client_details("../../client_data/dataset_one.csv","../../client_data/dataset_two.csv")
        # group_by_id = df_obj.groupby('client_identifier').apply(lambda x: x.drop('client_identifier', axis=1).to_dict(orient='records')).reset_index(name='data_client')
        # return jsonify(group_by_id.to_dict(orient='records'))
        return send_file("../../client_data/filtered_client_data.csv")
    
    if request.method == 'POST':
        countries = request.json.get('countries', [])
        
        if not countries:
            countries = ['United States','United Kingdom','France','Netherlands']
        df_obj = filter_client_details("../../client_data/dataset_one.csv","../../client_data/dataset_two.csv",countries)
        group_by_id = df_obj.groupby('client_identifier').apply(lambda x: x.drop('client_identifier', axis=1).to_dict(orient='records')).reset_index(name='data_client')
        save_csv(df_obj,"api")
        return jsonify(group_by_id.to_dict(orient='records'))

# @app.route('/download_filtered_data',methods=["POST"])
# def send_client_data():
#     if request.method == 'POST':
#         countries = request.json.get('countries', [])
        
#         if not countries:
#             countries = ['United States','United Kingdom','France','Netherlands']
#         df_obj = filter_client_details("../../client_data/dataset_one.csv","../../client_data/dataset_two.csv",countries)
#         group_by_id = df_obj.groupby('client_identifier').apply(lambda x: x.drop('client_identifier', axis=1).to_dict(orient='records')).reset_index(name='data_client')
#         save_csv(df_obj,"api")
#         return send_file("../../client_data/filtered_client_data.csv")

if __name__ ==" __main__":
    app.run(debug=True)
