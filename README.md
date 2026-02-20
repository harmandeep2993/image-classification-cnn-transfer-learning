# CIFAR-10 Image Classification: CNN Vs Transfer Learning
![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Keras](https://img.shields.io/badge/Keras-CNN-red)
![Deep Learning](https://img.shields.io/badge/Focus-DeepLearning-success)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

## 📖 Project Overview

This project explores image classification on the CIFAR-10 dataset using a structured deep learning workflow.

Rather than directly applying complex models, the development followed a progressive approach:
- Build a baseline CNN
- Increase architectural depth
- Increase architectural width
- Apply transfer learning
- Fine-tune selectively for better generalization

The objective was not only to improve accuracy, but to understand how architectural scaling impacts performance, stability, and overfitting.

## 📊 Dataset Description

* CIFAR-10
* 60,000 RGB images (32×32×3)
* 10 object classes
* 50,000 training / 10,000 testing

## Model Evolution

### 1. Baseline CNN

A simple architecture with two convolution blocks, pooling, dropout, and a dense classifier.
Used as the performance reference point.

### 2. Deeper CNN

Expanded to four convolution stages with progressive filter scaling:

**32 → 64 → 128 → 256**

- Added hierarchical feature extraction
- Used GlobalAveragePooling instead of Flatten
- Reduced parameter explosion

📌 Observation:
Improved validation accuracy and better feature abstraction compared to baseline.

### 3. Wider CNN

Increased filter sizes to test model capacity:

**64 → 128 → 256 → 512**

📌 Observation:
Higher training accuracy but increased overfitting.
Demonstrated the trade-off between capacity and generalization.

### 4. Transfer Learning

Pretrained backbone used:
DenseNet-121

⚙️ Implementation Steps

- Loaded ImageNet pretrained weights

- Replaced classification head

- Trained with frozen base model

- Unfroze last ~20% of layers

- Fine-tuned with reduced learning rate

📌 Observation:
Transfer learning significantly improved stability and overall performance compared to training from scratch.

🧪 Experimentation Framework

A reusable experiment pipeline was developed to:

🔧 Modify filters and dense units

📦 Adjust batch size and learning rate

⏹️ Apply EarlyStopping

📉 Use ReduceLROnPlateau

📊 Track training, validation, and test metrics

📝 Log structured results in a DataFrame

This ensured reproducibility and systematic comparison across architectures..

---

## Key Learnings

* Increasing depth improves hierarchical feature learning.
* Increasing width increases capacity but raises overfitting risk.
* GlobalAveragePooling helps control parameter growth.
* Transfer learning is highly effective on small image datasets.
* Fine-tuning only part of a pretrained model gives better balance than unfreezing everything.


## Tech Stack

Python • TensorFlow / Keras • NumPy • Pandas • Matplotlib • Scikit-learn

---

If needed, a more technical research-style version or a highly minimal portfolio-ready version can also be provided.
