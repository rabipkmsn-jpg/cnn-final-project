import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def show_project_summary():
    print("--- CNN Project Evaluation Summary ---")
    
    # 1. Show all saved results
    results_dir = 'results'
    files = os.listdir(results_dir)
    print(f"\n✅ Found {len(files)} result files in /results folder.")
    
    # 2. Function to display the Comparison Graph
    comparison_img = 'results/final_mega_comparison.png'
    if os.path.exists(comparison_img):
        img = mpimg.imread(comparison_img)
        plt.figure(figsize=(10,6))
        plt.imshow(img)
        plt.axis('off')
        plt.title("Model Evolution: Baseline vs Augmented vs Dropout")
        plt.show()
    
    # 3. Read and print the Final Report
    report_path = 'results/final_dropout_report.txt'
    if os.path.exists(report_path):
        with open(report_path, 'r') as f:
            print("\n--- Final Model (Scenario C) Classification Report ---")
            print(f.read())

if __name__ == "__main__":
    show_project_summary()