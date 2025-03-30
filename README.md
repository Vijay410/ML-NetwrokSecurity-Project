# ML Project Setup Guide

## 📌 Project Structure Setup

Follow these steps to set up your Machine Learning project with best practices, Poetry for package management, and GitHub Actions for CI/CD.

### **1️⃣ Create Project Folder**
Choose a name for your ML project and create a directory:
```sh
mkdir ML-Project
cd ML-Project
```

### **2️⃣ Create a Virtual Environment**
Set up and activate a virtual environment:
```sh
python -m venv venv  # Create virtual environment
```
For **Windows (PowerShell):**
```sh
.\venv\Scripts\Activate
```
For **Mac/Linux:**
```sh
source venv/bin/activate
```

### **3️⃣ Install Poetry for Package Management**
Poetry is used to manage dependencies efficiently:
```sh
pip install poetry
```

✅ **Poetry helps in installing packages and managing dependencies using version control.**

### **4️⃣ Initialize Poetry and Install Dependencies**
Create a `pyproject.toml` file:
```sh
poetry init  # Follow the prompts to configure
```
Add required dependencies:
```sh
poetry add pandas numpy scikit-learn fastapi uvicorn
```

### **5️⃣ Create Project Folder Structure**
Organize the source code into a `src/` directory:
```sh
mkdir src
cd src
mkdir components logging pipelines error_handling utils tests
```

📂 **Final Directory Structure:**
```
ML-Project/
├── Netwroksecurity_data
│   ├── __init__.py
│   └── netwroksecurity.csv
├── README.md
├── my_tree_structure.txt
├── notebooks
── nsp
│   ├── bin
│   │   ├── Activate.ps1
│   │   ├── activate
│   └── pyvenv.cfg
├── poetry.lock
├── pyproject.toml
└── src
    ├── Dockerfile
    ├── __init_.py
    ├── cloud
    ├── components
    ├── constant
    ├── entity
    ├── exception
    ├── logging
    ├── pipelines
    ├── setup.py
    └── utils
```

### **6️⃣ Set Up GitHub Actions for CI/CD**
Create a `.github/workflows/ci.yml` file:
```sh
mkdir -p .github/workflows
nano .github/workflows/ci.yml
```
Add the following content for automated testing and deployment:
```yaml
name: CI/CD Pipeline
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.12'
      
      - name: Install Dependencies
        run: |
          pip install poetry
          poetry install
      
      - name: Run Tests
        run: |
          poetry run pytest
```

### **7️⃣ Initialize Git and Push Code to GitHub**
```sh
git init
git add .
git commit -m "Initial project setup"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

### **8️⃣ Run and Test the Setup**
```sh
poetry run python -m src.main  # Run your main script
```

🚀 **Now your ML project is ready with proper structure, package management, and CI/CD!**

