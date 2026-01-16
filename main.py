import pickle
import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_final_report():
    print("\n" + "="*65)
    print("      FINAL PROJECT EVALUATION: CNN vs ANN ARCHITECTURES      ")
    print("="*65)

    # 1. Update paths to your new organized structure
    history_paths = {
        'ANN Baseline (A)': 'ann_experiment/results/scenario_a_history.pkl',
        'ANN Tuned LR (B)': 'ann_experiment/results/scenario_b_history.pkl',
        'ANN Optimized (C)': 'ann_experiment/results/scenario_c_history.pkl',
        'CNN Optimized': 'cnn_experiment/results/history_cnn_c.pkl'
    }

    comparison_data = []

    # 2. Extract Accuracy data
    for name, path in history_paths.items():
        if os.path.exists(path):
            with open(path, 'rb') as f:
                hist = pickle.load(f)
                comparison_data.append({
                    'Model Name': name,
                    'Training Acc': f"{hist['accuracy'][-1]:.4f}",
                    'Validation Acc': f"{hist['val_accuracy'][-1]:.4f}"
                })
        else:
            print(f"⚠️ Missing file: {path}")

    # 3. Create and Print Comparison Table
    df = pd.DataFrame(comparison_data)
    print("\n", df.to_string(index=False))
    print("="*65)

    # 4. Final Showdown Graph
    plt.figure(figsize=(12, 6))
    for name, path in history_paths.items():
        if os.path.exists(path):
            with open(path, 'rb') as f:
                hist = pickle.load(f)
                # Plotting validation accuracy for comparison
                plt.plot(hist['val_accuracy'], label=name, linewidth=2)

    plt.title('Final Showdown: Validation Accuracy Comparison (CNN vs ANN)', fontsize=14)
    plt.xlabel('Epochs', fontsize=12)
    plt.ylabel('Accuracy', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Save this master plot
    plt.savefig('cnn_experiment/results/final_mega_comparison.png')
    print("\n✅ Final comparison plot displayed and saved.")
    plt.show()

if __name__ == "__main__":
    generate_final_report()