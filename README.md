# streamlit-template
A streamlined template for Streamlit applications.

## Usage

### 1. Create Initial Environment
```bash
# For conda users
conda create -n my_streamlit_env python=3.9
conda activate my_streamlit_env

# For venv users
python -m venv streamlit_env
source streamlit_env/bin/activate # Linux
streamlit_env\Scripts\activate    # Windows

# Users who do not wish to use a virtual environment can proceed to the next step directly
```

### 2. Install Dependencies
```bash
# Using conda
conda env update -f environment.yml --prune # Ensure to modify some details in the environment.yml file
# Using pip
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run streamlit_app.py
```

**Open for issues!** Enjoy!

By Maicarons
