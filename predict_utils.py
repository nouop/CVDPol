import numpy as np
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.models import load_model

def load_all_models(model_paths):
    models = []
    # custom_objs = {'InputLayer': InputLayer}  # 添加这一行

    for path in model_paths:
        model = load_model(path)  # 修改这里
        models.append(model)
        print(path)
        print(models)
    return models

# 进行集成预测
def ensemble_predict(models, input_data):
    predictions = []

    for model in models:
        pred = model.predict(input_data)
        predictions.append(pred)


        # app.logger.info('hello')
    # 平均概率
    # ensemble_prob = np.mean(predictions, axis=0)
    # print(ensemble_prob)
    # ensemble_pred = (ensemble_prob >= 0.5).astype(int)
    # 对每个模型的预测值四舍五入后求和
    rounded_predictions = [np.round(pred) for pred in predictions]
    ensemble_sum = np.sum(rounded_predictions)
    print(f"四舍五入后的预测值: {rounded_predictions}")
    print(f"求和结果: {ensemble_sum}")

    return int(ensemble_sum)  