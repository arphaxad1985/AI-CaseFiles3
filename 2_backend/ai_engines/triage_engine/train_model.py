"""
train_model.py

Crime type and urgency classifier training script for AI CaseFiles system.
"""

import tensorflow as tf
from tensorflow.keras import layers, models

def create_model(input_shape, num_classes):
    model = models.Sequential([
        layers.InputLayer(input_shape=input_shape),
        layers.Dense(128, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def train_model(train_data, train_labels, input_shape, num_classes, epochs=10):
    model = create_model(input_shape, num_classes)
    model.fit(train_data, train_labels, epochs=epochs)
    model.save('triage_model.h5')

if __name__ == "__main__":
    # Placeholder for loading training data
    # train_data, train_labels = load_data()
    # train_model(train_data, train_labels, input_shape=(100,), num_classes=5)
    pass
