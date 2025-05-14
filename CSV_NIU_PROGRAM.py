import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk  
import itertools

def select_files():
    global selected_files
    file_paths = filedialog.askopenfilenames(title="Select CSV files", filetypes=[("CSV files", "*.csv")])
    if file_paths:
        selected_files.extend(file_paths)
        file_label.config(text="Selected Files:\n" + "\n".join([os.path.basename(f) for f in selected_files]))

def extract_tile_dimensions(file_path):
    try:
        df = pd.read_csv(file_path, skiprows=11, header=None)

        if df.shape[1] < 11 or df.shape[0] < 13:
            messagebox.showerror("Error", f"Invalid format in {file_path}")
            return None

        means = {
            "top": pd.to_numeric(df.iloc[0, 10], errors='coerce'),
            "bottom": pd.to_numeric(df.iloc[1, 10], errors='coerce'),
            "left": pd.to_numeric(df.iloc[2, 10], errors='coerce'),
            "right": pd.to_numeric(df.iloc[3, 10], errors='coerce'),
            "width": pd.to_numeric(df.iloc[4, 10], errors='coerce'),
            "height": pd.to_numeric(df.iloc[5, 10], errors='coerce')
        }

        errors = {
            "top": pd.to_numeric(df.iloc[6, 10], errors='coerce'),
            "bottom": pd.to_numeric(df.iloc[7, 10], errors='coerce'),
            "left": pd.to_numeric(df.iloc[8, 10], errors='coerce'),
            "right": pd.to_numeric(df.iloc[9, 10], errors='coerce'),
            "width": pd.to_numeric(df.iloc[10, 10], errors='coerce'),
            "height": pd.to_numeric(df.iloc[11, 10], errors='coerce')
        }

        return {"means": means, "errors": errors}
    except Exception as e:
        messagebox.showerror("Error", f"Error reading {file_path}: {e}")
        return None

import matplotlib.lines as mlines  

def plot_analysis():
    if not selected_files:
        messagebox.showwarning("Warning", "Please select files first!")
        return
    
    all_means = {key: [] for key in ["top", "bottom", "left", "right", "width", "height"]}
    all_errors = {key: [] for key in ["top", "bottom", "left", "right", "width", "height"]}

    file_labels = []
    
    for file_path in selected_files:
        data = extract_tile_dimensions(file_path)
        if data:
            for key in all_means:
                all_means[key].append(data["means"][key])
                all_errors[key].append(data["errors"][key])
            file_labels.append(os.path.splitext(os.path.basename(file_path))[0])
    
    sections = ["Top", "Bottom", "Left", "Right", "Width", "Height"]
    fig, axes = plt.subplots(3, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    markers = ['o', 's', '^', 'D', 'v', 'P', '*', 'X', '<', '>', 'h', '8']
    colors = list(plt.cm.tab10.colors) + list(plt.cm.Paired.colors)
    
    
    for idx, section in enumerate(sections):
        ax = axes[idx]
        key = section.lower()

        for file_idx, label in enumerate(file_labels):
            mean_val = all_means[key][file_idx]
            
            marker = markers[file_idx % len(markers)]
            color = colors[file_idx % len(colors)]


            ax.errorbar(
                file_idx,
                mean_val,
                yerr=0.05,
                color=color,
                fmt=marker,
                capsize=5,
                label=label if idx == 0 else "" 
            )

        ax.set_title(f"{section} Comparison", fontsize=10)
        ax.set_xticks(range(len(file_labels)))
        ax.set_xticklabels(file_labels, rotation=30, ha='right', fontsize=8)
        ax.set_ylabel("Measured - Target [mm]", fontsize=10)
        ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)
        ax.axhline(0.6, color='red', linestyle='--', linewidth=1)
        ax.set_ylim(0.0, 0.8)
        ax.grid(which='major', linestyle='--', linewidth=0.7, alpha=0.8)
        ax.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.5)
        ax.minorticks_on()
      
    plt.tight_layout(rect=[0, 0.05, 1, 0.92]) 
    fig.suptitle("Wrapped Tile Comparison", fontsize=14, fontweight='bold')
    
    handles, labels = axes[0].get_legend_handles_labels()
    tolerance_line = mlines.Line2D([], [], color='red', linestyle='--', linewidth=1, label="Tolerance Limit")
    handles.append(tolerance_line)
    labels.append("Tolerance Limit")
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, 0.01), ncol=len(labels), fontsize=10, frameon=True)

    # Save the figure
    output_dir = os.path.join(os.getcwd(), "Tile_Analysis_Results")
    os.makedirs(output_dir, exist_ok=True)  
    save_path = os.path.join(output_dir, "wrapped_tile_comparison.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    messagebox.showinfo("Graph Saved", f"Graph saved to:\n{save_path}")


    plt.show()

# GUI Setup
root = tk.Tk()
root.title("Tile Analysis Tool")
root.geometry("500x450")
selected_files = []

try:
    fnal_img = Image.open(r"C:\Users\danim\Downloads\FNAL-Logo-NAL-Blue-2.png").resize((200, 100))
    niu_img = Image.open(r"C:\Users\danim\Downloads\northern-illinois-university-niu-logo-vector.png").resize((200, 100))

    
    fnal_logo = ImageTk.PhotoImage(fnal_img)
    niu_logo = ImageTk.PhotoImage(niu_img)
    
    logo_frame = tk.Frame(root)
    logo_frame.pack(pady=5)

    fnal_label = tk.Label(logo_frame, image=fnal_logo)
    fnal_label.pack(side="left", padx=10)
    
    niu_label = tk.Label(logo_frame, image=niu_logo)
    niu_label.pack(side="right", padx=10)
except Exception as e:
    print("Error loading logos:", e)

title_label = tk.Label(root, text="Wrapped Tile Analysis Tool", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

file_label = tk.Label(root, text="No files selected", wraplength=400, justify="left")
file_label.pack(pady=10)

button_style = {"height": 2, "width": 20, "font": ("Arial", 12, "bold")}

select_button = tk.Button(root, text="Select Files", command=select_files, bg="blue", fg="white", **button_style)
select_button.pack(pady=10)  # Increased spacing

generate_button = tk.Button(root, text="Generate Graph", command=plot_analysis, bg="red", fg="white", **button_style)
generate_button.pack(pady=10)

credit_label = tk.Label(root, text="Created by Danielle Nunez\n(Randolph College, CMS/PURSUE)", font=("Arial", 10, "italic"))
credit_label.pack(side="bottom", pady=10)

root.mainloop()






