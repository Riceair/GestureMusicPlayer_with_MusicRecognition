from tensorflow import keras
from keras import Sequential

load_model_path = "FinalFeature/MS_test6833.h5"
save_model_path = "FinalFeature/FeatureModel.h5"

model = keras.models.load_model(load_model_path)
feature_model = Sequential()

for layer in model.layers[:-1]: #移掉最後一層，以倒數第二層為特徵向量
    feature_model.add(layer)

keras.models.save_model(feature_model, save_model_path)