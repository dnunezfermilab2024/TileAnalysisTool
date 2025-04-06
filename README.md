# Wrapped Tile Analysis Tool

## 📌 Overview  
This project provides a graphical user interface (GUI) for analyzing wrapped tile dimensions from CSV files.

## ✅ Prerequisites

Ensure you have the following installed before running the project:

- Python (Version 3.x recommended)
- Visual Studio Code
- PowerShell (pre-installed on Windows)
- Git (for cloning repositories)
- Required Python libraries (install via `pip`)

---

## 🧰 Visual Studio Code Setup

### 1. Installing VS Code
- Visit the [Visual Studio Code website](https://code.visualstudio.com).
- Download the installer for your operating system (Windows/macOS/Linux).
- Run the installer and follow the setup instructions.
- Open **Visual Studio Code** after installation.

### 2. Installing the Python Extension
- Launch Visual Studio Code.
- Open the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X` on macOS).
- Search for **Python** and install the extension by **Microsoft**.

### 3. Verifying Python Installation
- Open a new terminal in VS Code (`Ctrl+\`` or `Cmd+\``).
- Run:
  ```bash
  python --version

### 💻 PowerShell Setup

### 1. Open PowerShell
Search for PowerShell in the Start Menu and open it.

### 2. Check Python Installation
Run:
   ```bash
   python --version
   ```
### 3. Add Python to PATH (if needed)

If Python is not recognized as a command, follow these steps to add it to your system's PATH:

1. Press `Win + R`, type `sysdm.cpl`, and press **Enter**.
2. Go to the **Advanced** tab and click **Environment Variables**.
3. Under **System Variables**, select **Path**, then click **Edit**.
4. Click **New** and add the path to your Python installation (e.g., `C:\Python39`).
5. Click **OK** to save the changes.
6. Restart **PowerShell** for the changes to take effect.


---

## 📂 Cloning the Repository

You can use either the **VS Code Terminal** or **PowerShell** for this.

### 1. Verify Git Installation

Run:
```bash
git --version
```
If Git is not installed, download and install it from [git-scm.com](https://git-scm.com).

### 2. Navigate to Your Project Directory
Use the cd command to move into your desired folder:
```bash
cd path\to\your\folder
```

### 3. Clone the Repository
Run:
```bash
git clone https://github.com/your-username/repository-name.git
cd repository-name
```

## ▶️ Running the Project
### Step 1: Install Required Packages
In the terminal, run:
```bash
pip install numpy pandas matplotlib pillow tk
```

### Step 2: Run the Application
   1.Open VS Code and go to the cloned project folder.
   
   2.Open the file CSV_NIU_PROGRAM.py.
   
   3.In the terminal, run:
   ```bash
   python CSV_NIU_PROGRAM.py
   ```

## 📊 Usage
 -Click Select Files to choose one or more CSV files for analysis.
 
 -Click Generate Graph to visualize the results.
 
 -The application will generate plots showing a comparison of tile dimensions.

## 👩‍💻 Credits
**Created by:** Danielle Nunez

**Institution:** Randolph College, CMS/PURSUE
