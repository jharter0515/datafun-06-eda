\# datafun-06-eda



\## Overview

This project initializes a Python Exploratory Data Analysis (EDA) repository using a repeatable workflow.



\## Project Setup (Commands Used)



```powershell

\# Navigate to working folder on external drive

D:

cd D:\\Repos



\# Clone repo

git clone https://github.com/jharter0515/datafun-06-eda.git

cd datafun-06-eda



\# Create and activate virtual environment

python -m venv .venv

.\\.venv\\Scripts\\Activate.ps1



\# Install dependencies

python -m pip install --upgrade pip

pip install -r requirements.txt


(That’s three backticks on a line by itself.)

That closes the code block.

---

### Step 2 — Add the Dataset Section BELOW That

Then paste this:

```markdown
## Data Set

### Source (Name + Link)
**Palmer Penguins dataset** (accessed via `seaborn.load_dataset("penguins")`)  
https://allisonhorst.github.io/palmerpenguins/

### Record Count
- **Rows:** 344  
- **Columns:** 7  

### Columns (What Each Column Holds)
- **species** (str): Penguin species (e.g., Adelie, Chinstrap, Gentoo)
- **island** (str): Island where the penguin was observed
- **bill_length_mm** (float64): Bill length in millimeters
- **bill_depth_mm** (float64): Bill depth in millimeters
- **flipper_length_mm** (float64): Flipper length in millimeters
- **body_mass_g** (float64): Body mass in grams
- **sex** (str): Sex of the penguin


