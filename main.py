import pandas as pd 
import numpy as np 
import tensorflow as tf
from tensorflow.keras.layers import Embedding, Flatten, Dense
from surprise.model_selection import GridSearchCV


print(grid_search.best_params['rmse'])

user_input = tf.keras.layers.Input(shape=(1,), name='user_input')
item_input = tf.keras.layers.Input(shape=(1,), name='item_input')

user_embedding = Embedding(input_dim=num_users, output_dim=embedding_dim)(user_input)
item_embedding = Embedding(input_dim=num_items, output_dim=embedding_dim)(item_input)

user_vec = Flatten()(user_embedding)
item_vec = Flatten()(item_embedding)

concat = tf.keras.layers.Concatenate()([user_vec, item_vec])
dense = Dense(128, activation='relu')(concat)
output = Dense(1)(dense)

param_grid = {'n_factors': [50, 100], 'n_epochs': [20, 50], 'lr_all': [0.002, 0.005]}
grid_search = GridSearchCV(SVD, param_grid, measures=['rmse', 'mae'], cv=3)
grid_search.fit(data)

model = tf.keras.models.Model(inputs=[user_input, item_input], outputs=output)
model.compile(optimizer='adam', loss='mse')

model.fit([train_users, train_items], train_ratings, epochs=5, batch_size=64, validation_split=0.2)


