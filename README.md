# Wrapped Tile Analysis Tool

## Overview

This project provides a graphical user interface (GUI) for analyzing wrapped tile dimensions from CSV files. It uses Python with libraries such as `numpy`, `pandas`, `matplotlib`, and `tkinter` to extract data and generate comparative graphs.

## Prerequisites

Before running the script, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (Version 3.x recommended)
- [Visual Studio Code](https://code.visualstudio.com/)
- PowerShell (pre-installed on Windows)
- Git (for cloning repositories)
- Required Python libraries (install with `pip`)

## Installation Guide

### Setting Up Visual Studio Code

1. Visit the [VS Code website](https://code.visualstudio.com/).
2. Click on **Download for Windows/macOS/Linux** based on your OS.
3. Run the installer and follow the setup instructions.
4. Open VS Code after installation.
5. Install the Python extension:
   - Open VS Code.
   - Go to **Extensions** (Ctrl+Shift+X or Cmd+Shift+X on macOS).
   - Search for **Python** and install the extension provided by Microsoft.
6. Open a new terminal in VS Code and verify Python installation by running:
   ```sh
   python --version
   ```

### Setting Up PowerShell

1. Open **PowerShell** (search `PowerShell` in Start Menu on Windows).
2. Check if Python is installed by running:
   ```powershell
   python --version
   ```
3. If Python is not recognized, add it to the system's PATH:
   - Open **System Properties** (Win+R, type `sysdm.cpl`, and press Enter).
   - Go to the **Advanced** tab and click **Environment Variables**.
   - Under **System Variables**, find **Path**, select it, and click **Edit**.
   - Click **New** and add the path to your Python installation (e.g., `C:\Python39`).
   - Click **OK** and restart PowerShell.

## Cloning the Repository

1. Open **VS Code** and open the **Terminal** (Ctrl+`).
2. Ensure Git is installed by running:
   ```sh
   git --version
   ```
   If Git is not installed, download and install it from [git-scm.com](https://git-scm.com/).
3. Navigate to a desired directory and run:
   ```sh
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
   ```

## Running the Project

### Step 1: Install Required Python Packages

Run the following command in the terminal:

```sh
pip install numpy pandas matplotlib pillow tk
```

### Step 2: Run the Application

1. Open VS Code and navigate to the project folder.
2. Open `CSV_NIU_PROGRAM.py`.
3. Run the script using:
   ```sh
   python CSV_NIU_PROGRAM.py
   ```

## Usage

1. Click **Select Files** to choose CSV files for analysis.
2. Click **Generate Graph** to visualize the results.
3. The generated plots will display a comparison of tile dimensions.

## Credits

Created by **Danielle Nunez**\
Randolph College, CMS/PURSUE









   
