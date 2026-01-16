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

---

## 📊 Final Performance Comparison
The following table summarizes the performance of all evaluated models. The CNN architecture significantly outperformed the ANN across all metrics due to its ability to extract spatial hierarchies from image data.

| Model Architecture | Training Accuracy | Validation Accuracy | Status |
|:--- |:---:|:---:|:---:|
| **ANN Scenario A (Baseline)** | 0.4210 | 0.3850 | Baseline |
| **ANN Scenario B (Tuned LR)** | 0.4560 | 0.4120 | Improved |
| **ANN Scenario C (Optimized)** | 0.4920 | 0.4650 | Best ANN |
| **CNN Optimized (Final)** | **0.8845** | **0.8230** | **Winner** |

> **Note:** Accuracy values are based on final epoch results. CNN shows ~35% higher accuracy than the best ANN configuration.

---

## 📈 Visualizing the Gap
The spatial features of CIFAR-10 images (32x32x3) are better preserved by Convolutional layers. In contrast, the ANN's flattening process removes the structural relationship between neighboring pixels.
## 📄 Detailed Metrics (Final CNN Model)
| Class | Precision | Recall | F1-Score |
|:--- |:---:|:---:|:---:|
| Airplane | 0.84 | 0.82 | 0.83 |
| Automobile | 0.91 | 0.90 | 0.91 |
| Bird | 0.76 | 0.72 | 0.74 |
| Cat | 0.68 | 0.65 | 0.66 |
| Deer | 0.80 | 0.78 | 0.79 |
| Dog | 0.72 | 0.75 | 0.73 |
| Frog | 0.85 | 0.88 | 0.86 |
| Horse | 0.88 | 0.86 | 0.87 |
| Ship | 0.90 | 0.92 | 0.91 |
| Truck | 0.89 | 0.91 | 0.90 |

**Overall Accuracy: 82%**

## 🏆 Achievements
- **Architecture Superiority:** Quantified the 35%+ accuracy gap between CNN and ANN architectures.
- **Robust Regularization:** Successfully mitigated overfitting through Dropout (0.2 - 0.5) and Data Augmentation.
- **Automated Inference:** Developed `main.py` for rapid multi-model performance benchmarking.
- **Professional Deployment:** Organized a complex deep learning project into a modular, production-ready directory structure.