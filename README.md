# Image Classifier

A local image classification project developed using modern deep learning techniques. The goal is to build, train, evaluate, and deploy an image classification model using our own GPU hardware.

## Project Overview

This project will implement an image classification system capable of identifying different categories of images.

The model will be trained locally using NVIDIA GPUs, taking advantage of CUDA acceleration and GPU-based deep learning.

The dataset and final classification categories are still being decided.

## Planned Approach

We plan to use **transfer learning** rather than training a neural network entirely from scratch.

A modern pre-trained computer vision model will be selected and fine-tuned for our specific dataset.

The candidate architectures currently include:

- **ConvNeXt**
- **EfficientNet**
- **Vision Transformer (ViT)**
- **Swin Transformer**

The final architecture will be selected after evaluating the characteristics and size of the dataset.

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

Both GPUs will use the same codebase and model configuration, allowing us to compare training performance between the two systems.

## Machine Learning Techniques

The project is expected to include:

- Transfer learning
- Fine-tuning
- Convolutional neural networks and/or vision transformers
- Data preprocessing
- Data augmentation
- GPU-accelerated training
- Mixed-precision training
- Hyperparameter optimization
- Model evaluation

## Evaluation

The trained models will be evaluated using metrics such as:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Training and validation results will also be visualized to analyze model performance and detect problems such as overfitting.

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
├── results/
│   ├── graphs/
│   └── confusion_matrix/
│
├── notebooks/
│
├── gpu_test.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Current Status

- [x] Create GitHub repository
- [x] Configure Python environment
- [x] Install PyTorch
- [x] Configure CUDA
- [x] Verify NVIDIA GPU acceleration
- [ ] Select dataset
- [ ] Prepare dataset
- [ ] Select final model architecture
- [ ] Implement training pipeline
- [ ] Train initial model
- [ ] Fine-tune model
- [ ] Evaluate model
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
2. Use modern deep learning architectures.
3. Take advantage of GPU acceleration.
4. Experiment with different model configurations.
5. Evaluate and compare model performance.
6. Produce a reproducible project that can be trained and executed locally.
