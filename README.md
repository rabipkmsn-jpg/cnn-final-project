# 🧠 CIFAR-10 Image Classification via Optimized CNN
**A Comparative Study of Regularization and Augmentation Techniques**

## 📝 Project Overview
This project implements a Convolutional Neural Network (CNN) to classify images from the CIFAR-10 dataset. The core objective was to analyze how different optimization strategies affect model performance and generalization.

## 📂 Project Structure
- **/models**: Stores trained weights for Baseline (.h5), Augmented, and Dropout models (.keras).
- **/results**: Contains learning curves (PNG), comparison plots, and classification reports (TXT).
- **run_evaluation.py**: A Python script to visualize results and evaluate the final model.
- **Project_Notebook.ipynb**: The original training source from Google Colab.

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