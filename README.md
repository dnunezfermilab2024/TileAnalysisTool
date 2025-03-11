# TileAnalysisTool
This script processes CSV files containing tile dimension measurements, extracts relevant data, and visualizes the analysis using Matplotlib.

📌 Prerequisites

Before running the script, ensure you have the following installed:

  Python (3.x) (Ensure you check "Add Python to PATH" during installation)

  Visual Studio Code (VS Code)

  Required Python libraries (see installation steps below)

📥 Installation and Setup

1️⃣ Install VS Code

Download and install VS Code.

Open VS Code and install the Python extension:

    Press Ctrl + Shift + X to open the Extensions Marketplace.

    Search for "Python" and click Install.

2️⃣ Install Python and Dependencies

Install Python if not already installed.

Open VS Code and launch the integrated terminal:

  Press Ctrl + ~ (tilde key) to open the terminal.

Run the following command to install the required Python libraries:

  pip install numpy pandas matplotlib tkinter

3️⃣ Clone This Repository (Optional)

If you are using Git, you can clone this repository:

git clone https://github.com/your-username/tile-analysis.git
cd tile-analysis

Alternatively, download and extract the project files manually.

4️⃣ Prepare Your CSV Files

Ensure that your CSV files follow this naming format:

  DATA_<tile_type>_<version>.csv

📌 Example filenames:

  DATA_T34_V2.csv

  DATA_T34_V3.csv

Note: The script extracts the tile type from the filename, so this format is mandatory for correct labeling.

🚀 Running the Script

1. Open VS Code and navigate to the folder containing tile_analysis.py.

2. Open the integrated terminal (Ctrl + ~).

3. Run the script titled:

        CSV_NIU_PROGRAM.py

4. A file selection dialog will appear. Choose one or more CSV files for analysis.

5. The script will process the files and generate a comparison plot.

6. You can save the plot as a PNG file when prompted.


   
