# 🖼️ CIFAR-10 Image Classification: CNN vs ANN Comparative Study
**Aligning with UN Sustainable Development Goal 9: Industry, Innovation, and Infrastructure**

## 📝 Introduction
Automated image recognition is a core component of modern industrial innovation. This project explores the classification of the CIFAR-10 dataset using two distinct deep learning architectures: Convolutional Neural Networks (CNN) and Artificial Neural Networks (ANN). By benchmarking these models, we demonstrate the technical advantages of hierarchical feature extraction in computer vision.

---

## 🚀 Project Description
This system implements a comprehensive pipeline for training and evaluating multiple neural network configurations. It evaluates three optimization scenarios for both CNN and ANN architectures to determine the most effective strategy for real-world image data.

**Key Features:**
* **End-to-End Pipeline:** Data preprocessing, model training, and performance visualization.
* **Architecture Benchmarking:** Direct comparison between spatial (CNN) and non-spatial (ANN) models.
* **Optimization Scenarios:** Implementation of Data Augmentation and Dropout Regularization.
* **Automated Evaluation:** A master script (`main.py`) to generate consolidated comparison reports and tables.

---

## 🎯 Objectives
* **Baseline Development:** Establish performance benchmarks for standard neural network architectures.
* **Model Optimization:** Implement regularization techniques to mitigate overfitting and improve generalization.
* **Structural Comparison:** Analyze the efficiency of CNN layers versus traditional flattened ANN layers.
* [cite_start]**Documentation & Reproducibility:** Maintain a clean, version-controlled repository according to professional standards[cite: 123, 141].

---

## 🛠 Tech Stack
* **Programming Language:** Python
* **Deep Learning Framework:** TensorFlow / Keras
* **Libraries:** NumPy, Pandas, Matplotlib, Seaborn
* **Development Environment:** Google Colab & VS Code

---

## 📂 Project Structure
```text
cnn_final_project/
├── ann_experiment/          # Dedicated folder for ANN research
│   ├── models/              # Scenario A, B, and C trained models (.keras)
│   └── results/             # ANN learning curves and history files (.pkl)
├── cnn_experiment/          # Dedicated folder for CNN research
│   ├── models/              # Baseline, Dropout, and Optimized CNN models
│   └── results/             # CNN plots and classification reports
├── main.py                  # Master script for architecture comparison
├── run_evaluation.py        # Summary script for model visualization
└── README.md                # Project documentation
 ## 🛠 Optimization Scenarios
1. **Scenario A (Baseline):** A standard CNN architecture. Highly prone to overfitting.
2. **Scenario B (Data Augmentation):** Implemented random flips, rotations, and zooms to increase data variety and improve robustness.
3. **Scenario C (Dropout & Tuning):** Added Dropout layers (0.2 - 0.5) to prevent co-adaptation of neurons, resulting in the most generalized model.

## ⚠️ Challenges & Hurdles (Major Learning Points)
During development, the following hurdles were addressed:
* **Overfitting:** The initial model (Scenario A) showed a large gap between training and validation accuracy. This was mitigated using Dropout and Augmentation.
* **Accuracy Trade-off:** Introducing data augmentation initially slowed down the learning process, but ultimately led to a more reliable model for unseen data.
* **Environment Compatibility:** Transitioning from the cloud (Google Colab) to local execution (VS Code) required careful management of file paths and library versions.

## 🚀 How to Run
Execute the following command in the terminal:
`py -m run_evaluation`