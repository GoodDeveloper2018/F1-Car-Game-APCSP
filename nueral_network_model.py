import tensorflow as tf
import numpy as np

class NeuralNetwork:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)

    def predict_action(self, game_state):
        state = np.array(game_state).reshape(-1, *game_state.shape)
        prediction = self.model.predict(state)
        return np.argmax(prediction[0])
