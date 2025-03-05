# TileAnalysisTool
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog, messagebox

def select_files():
    root = Tk()
    root.withdraw()
    file_paths = []
    while True:
        file_path = filedialog.askopenfilename(title="Select a CSV file (Cancel to finish)", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            break
        file_paths.append(file_path)
    return file_paths

def extract_tile_dimensions(file_path):
    try:
        df = pd.read_csv(file_path, skiprows=11, header=None)
        
        if df.shape[1] < 11:
            messagebox.showerror("Error", f"Invalid format in {file_path}")
            return None
        
        values = {
            "top": pd.to_numeric(df.iloc[0, 10], errors='coerce'),
            "bottom": pd.to_numeric(df.iloc[1, 10], errors='coerce'),
            "left": pd.to_numeric(df.iloc[2, 10], errors='coerce'),
            "right": pd.to_numeric(df.iloc[3, 10], errors='coerce'),
            "width": pd.to_numeric(df.iloc[4, 10], errors='coerce'),
            "height": pd.to_numeric(df.iloc[5, 10], errors='coerce')
        }
        return values
    except Exception as e:
        messagebox.showerror("Error", f"Error reading {file_path}: {e}")
        return None

def plot_analysis(stats, file_labels):
    sections = ["Top", "Bottom", "Left", "Right", "Width", "Height"]
    fig, axes = plt.subplots(3, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    markers = ['o', 's', '^', 'D', 'v', 'P']
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']
    
    for idx, section in enumerate(sections):
        ax = axes[idx]
        for file_idx, label in enumerate(file_labels):
            mean_value, std_dev = stats[section.lower()]
            
            # Extract tile type from filename
            tile_type = label.split('_')[1] if '_' in label else "Unknown"
            
            ax.errorbar(
                file_idx, mean_value, yerr=std_dev,
                fmt=f'{markers[file_idx % len(markers)]}',
                color=colors[file_idx % len(colors)],
                capsize=5, 
                label=f"{tile_type} ({label})"
            )
         
        ax.set_title(f"{section} Comparison", fontsize=10)
        ax.set_xticks(range(len(file_labels)))
        ax.set_xticklabels(file_labels, rotation=30, ha='right', fontsize=8)
        ax.set_ylabel("Measured - Target [mm]", fontsize=10)
        ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)
        ax.axhline(0.6, color='red', linestyle='--', linewidth=1, label='Tolerance Limit')
        ax.set_ylim(0.0, 0.8) 
        ax.grid(which='major', linestyle='--', linewidth=0.7, alpha=0.8)
        ax.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.5)
        ax.minorticks_on()
    
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    fig.suptitle("Wrapped Tile Comparison", fontsize=14, fontweight='bold')
    
    handles, labels = axes[0].get_legend_handles_labels()
    unique_labels = dict(zip(labels, handles))
    fig.legend(
        unique_labels.values(),
        unique_labels.keys(),
        loc='upper center',
        ncol=3,
        bbox_to_anchor=(0.5, 0.05),
        fontsize=9
    )
    
    output_path = filedialog.asksaveasfilename(title="Save Plot As", defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight', format='png')
        messagebox.showinfo("Success", f"Plot saved successfully at {output_path}!")
    plt.show()

def main():
    file_paths = select_files()
    if not file_paths:
        print("No files selected.")
        return
    
    all_data = {key: [] for key in ["top", "bottom", "left", "right", "width", "height"]}
    file_labels = []
    
    for file_path in file_paths:
        data = extract_tile_dimensions(file_path)
        if data:
            for key in all_data:
                all_data[key].append(data[key])
            file_labels.append(os.path.splitext(os.path.basename(file_path))[0])
    
    stats = {key: (np.mean(all_data[key]), np.std(all_data[key])) for key in all_data}
    
    print("Tile Dimension Averages and Standard Deviations:")
    for key, (mean, std) in stats.items():
        print(f"{key.capitalize()}: Mean = {mean:.3f}, Std Dev = {std:.3f}")
    
    plot_analysis(stats, file_labels)
    
if __name__ == "__main__":
    main()
