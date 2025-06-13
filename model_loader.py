import os
from predict_utils import load_all_models

MODEL_DIR = "models"
MODEL_FILES = ["model1.h5", "model2.h5", "model3.h5"]

# 获取完整路径
model_paths = [os.path.join(MODEL_DIR, f) for f in MODEL_FILES]

print(model_paths)

# 加载模型
loaded_models = load_all_models(model_paths)