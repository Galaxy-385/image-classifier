# Image Classifier

A local image classification project developed using deep learning techniques. The goal is to build, train, evaluate, and improve an image classification model entirely from scratch using our own GPU hardware.

## Project Overview

This project will implement an image classification system capable of identifying different categories of images.

The neural network will be trained **entirely from scratch**, without using pre-trained models or transfer learning. Its weights will be initialized before training and progressively adjusted through backpropagation and optimization.

The model will be trained locally using NVIDIA GPUs, taking advantage of CUDA acceleration and GPU-based deep learning.

The dataset and final classification categories are still being decided.

## Planned Approach

Instead of using a pre-trained model, we will develop our own neural network architecture and train it from scratch.

The project will start with a simple **Convolutional Neural Network (CNN)** and progressively improve it through experimentation.

Different versions of the model may be created by modifying aspects such as:

- Network architecture
- Number of layers
- Number of convolutional filters
- Activation functions
- Batch normalization
- Dropout
- Data augmentation
- Optimizer and learning rate
- Learning-rate scheduling
- Other training hyperparameters

Each version will be trained and evaluated so that the results can be compared with previous versions.

The final architecture will be determined experimentally according to the characteristics of the selected dataset and the results obtained during training.

## Technologies

### Programming

- Python 3.14
- PyTorch
- Torchvision

### GPU Acceleration

- NVIDIA CUDA
- CUDA 13.0
- GPU-accelerated training

### Hardware

- NVIDIA GeForce RTX 5070
- NVIDIA GeForce RTX 5060

Both GPUs will use the same codebase, allowing us to run the same experiments on different hardware and compare their training performance.

## Machine Learning Techniques

The project is expected to include:

- Convolutional neural networks
- Training from scratch
- Data preprocessing
- Data augmentation
- GPU-accelerated training
- Mixed-precision training
- Batch normalization
- Dropout and other regularization techniques
- Optimizer and learning-rate experimentation
- Hyperparameter optimization
- Model evaluation
- Experiment comparison

No pre-trained model weights or transfer learning will be used.

## Model Training

The model will learn through an iterative training process:

```text
Input image
     ↓
Neural network
     ↓
Prediction
     ↓
Loss calculation
     ↓
Backpropagation
     ↓
Weight update
     ↓
Next training iteration
```

The initial model will provide a baseline. Later versions will introduce controlled modifications to the architecture and training process.

This will allow us to study how each modification affects the model's performance.

## Evaluation

The trained models will be evaluated using metrics such as:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Training and validation results will also be visualized to analyze model performance and detect problems such as overfitting.

Different model versions will be compared to determine which modifications provide meaningful improvements.

## Project Structure

```text
image-classifier/
│
├── src/
│   ├── train.py
│   ├── model.py
│   ├── dataset.py
│   ├── evaluate.py
│   └── predict.py
│
├── data/
│
├── models/
│
├── notebooks/
│
├── tests/
│
├── gpu_test.py
├── requirements.txt
├── .gitignore
└── README.md
```

Additional files and directories may be added as the project develops.

## Current Status

- [x] Create GitHub repository
- [x] Configure Python environment
- [x] Install PyTorch
- [x] Configure CUDA
- [x] Verify NVIDIA GPU acceleration
- [ ] Select dataset
- [ ] Prepare dataset
- [ ] Design initial CNN architecture
- [ ] Implement dataset pipeline
- [ ] Implement training pipeline
- [ ] Train initial model
- [ ] Evaluate initial model
- [ ] Develop improved model versions
- [ ] Compare experiments
- [ ] Implement image prediction
- [ ] Finalize project

## Hardware Verification

The current development environment has been successfully tested with:

```text
Python: 3.14.5
PyTorch: 2.14.1+cu130
CUDA: 13.0
GPU: NVIDIA GeForce RTX 5070
CUDA available: True
```

The same project will be configured on an NVIDIA RTX 5060 system.

## Goals

The main goals of the project are:

1. Build a complete image classification pipeline.
2. Develop a neural network trained entirely from scratch.
3. Understand how a CNN learns through training and backpropagation.
4. Experiment with different architectures and training techniques.
5. Compare different model versions and their performance.
6. Take advantage of GPU acceleration for local training.
7. Analyze the effect of different modifications on model performance.
8. Produce a reproducible project that can be trained and executed locally.
