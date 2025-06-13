from flask import Flask, request, jsonify
import numpy as np
from model_loader import loaded_models
from predict_utils import ensemble_predict
from flask_cors import CORS  # 导入 CORS 模块
from gevent import pywsgi


app = Flask(__name__)
CORS(app, supports_credentials=True, methods=["POST"], allow_headers=["Content-Type"])

@app.route('/predict', methods=['POST'])
def predict():
   
    try:
        data = request.get_json()

        # 提取输入字段
        age = float(data['age'])
        sex = int(data['sex'])  # 0: female, 1: male
        height = float(data['height'])
        weight = float(data['weight'])
        systolic = int(data['systolic'])
        diastolic = int(data['diastolic'])
        smoke = int(data['smoke'])  # 0 or 1
        cholesterol = int(data['cholesterol'])
        gluc = int(data['gluc'])
        exercise = int(data['exercise'])  # 0 or 1
        alco = int(data['alco'])

    

        # 构造输入向量（顺序必须与训练时一致）
        input_data = np.array([[age, sex, height, weight, systolic, diastolic, smoke, cholesterol,gluc,exercise, alco]])
        print(input_data)
        # 预测
        result = ensemble_predict(loaded_models, input_data)



        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('127.0.0.1',5000),app)
    server.serve_forever()
    app.run(debug=True)