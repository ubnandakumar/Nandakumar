# Troubleshooting Guide

## Import Error: `split_torch_state_dict_into_shards`

### Problem
```
ImportError: cannot import name 'split_torch_state_dict_into_shards' from 'huggingface_hub'
```

### Solution

This is a version compatibility issue. Follow these steps:

#### Option 1: Update All Packages (Recommended)

```bash
# Uninstall conflicting packages
pip uninstall transformers huggingface_hub accelerate -y

# Install fresh with compatible versions
pip install transformers>=4.35.0 huggingface_hub>=0.20.0 accelerate>=0.25.0

# Or simply reinstall from requirements
pip install -r requirements.txt --upgrade
```

#### Option 2: Install Specific Compatible Versions

```bash
pip install transformers==4.36.0 huggingface_hub==0.20.1 accelerate==0.25.0 torch>=2.0.0
```

#### Option 3: Use Virtual Environment (Best Practice)

```bash
# Create a new virtual environment
python -m venv hr_classifier_env

# Activate it
# On Windows:
hr_classifier_env\Scripts\activate
# On Linux/Mac:
source hr_classifier_env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Verify Installation

After fixing, verify it works:

```bash
python -c "from transformers import pipeline; print('Success!')"
```

---

## Out of Memory Error

### Problem
```
RuntimeError: [enforce fail at alloc_cpu.cpp:114] err == 0. DefaultCPUAllocator: can't allocate memory
```

### Solutions

1. **Close Other Applications**
   - Close browsers, IDEs, and other memory-intensive apps
   - Ensure at least 4-5GB RAM is free

2. **Use a Smaller Model**

   Edit `hr_intent_classifier.py` and change the model:

   ```python
   # Original (line 21-22)
   def __init__(self, model_name: str = "MoritzLaurer/deberta-v3-base-zeroshot-v1.1-all-33"):

   # Change to smaller model:
   def __init__(self, model_name: str = "facebook/bart-large-mnli"):
   ```

3. **Monitor Memory Usage**

   ```bash
   # Windows
   taskmgr

   # Linux
   htop

   # Python check
   python -c "import psutil; print(f'Available RAM: {psutil.virtual_memory().available / 1024**3:.2f} GB')"
   ```

---

## Slow Performance

### Problem
Classification takes more than 5-10 seconds per query.

### Solutions

1. **First Run is Slow** - Model downloads and loads (this is normal)
2. **Subsequent Runs** - Should be faster (1-2 seconds on CPU)
3. **Use GPU if Available**

   Install CUDA-enabled PyTorch:
   ```bash
   # For CUDA 11.8
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

   The classifier will automatically use GPU if available.

4. **Optimize for Multiple Queries**

   Classify in batches instead of one-by-one:
   ```python
   queries = ["query1", "query2", "query3"]
   results = [classifier.classify(q) for q in queries]
   ```

---

## Model Download Issues

### Problem
```
OSError: Can't load the model. Make sure you are connected to the internet.
```

### Solutions

1. **Check Internet Connection**
   ```bash
   ping huggingface.co
   ```

2. **Check Firewall/Proxy Settings**
   - Ensure access to huggingface.co
   - Configure proxy if needed:
   ```bash
   export HTTP_PROXY=http://proxy.example.com:8080
   export HTTPS_PROXY=http://proxy.example.com:8080
   ```

3. **Manual Download**
   ```python
   from transformers import AutoTokenizer, AutoModelForSequenceClassification

   model_name = "MoritzLaurer/deberta-v3-base-zeroshot-v1.1-all-33"
   tokenizer = AutoTokenizer.from_pretrained(model_name)
   model = AutoModelForSequenceClassification.from_pretrained(model_name)
   ```

4. **Use Local Cache**
   - Models cache in: `~/.cache/huggingface/` (Linux/Mac) or `C:\Users\<user>\.cache\huggingface\` (Windows)
   - If you have the model elsewhere, copy it there

---

## Python Version Issues

### Problem
```
SyntaxError: invalid syntax
```

### Solution

Ensure you're using Python 3.8 or higher:

```bash
python --version
# Should show: Python 3.8.x or higher
```

If too old, install Python 3.10+:
- Windows: https://www.python.org/downloads/
- Linux: `sudo apt install python3.10`
- Mac: `brew install python@3.10`

---

## Windows-Specific Issues

### Problem
Long path errors or permission issues.

### Solutions

1. **Enable Long Paths**
   - Run as Administrator:
   ```powershell
   New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
   ```

2. **Run with Administrator Privileges**
   - Right-click Command Prompt → "Run as administrator"

3. **Use PowerShell Instead of CMD**

---

## Module Not Found Errors

### Problem
```
ModuleNotFoundError: No module named 'transformers'
```

### Solution

```bash
# Ensure you're in the right environment
pip list | grep transformers

# If not found, install
pip install -r requirements.txt

# Verify
python -c "import transformers; print(transformers.__version__)"
```

---

## Alternative: Lightweight Version

If you continue to have issues, here's a minimal alternative using a rule-based approach:

```python
# lightweight_classifier.py
import re

class SimplHRClassifier:
    """Simple rule-based HR classifier (no ML dependencies)"""

    def __init__(self):
        self.hr_keywords = [
            'leave', 'vacation', 'pto', 'sick', 'maternity', 'paternity',
            'salary', 'pay', 'paycheck', 'compensation', 'bonus', 'raise',
            'benefits', 'insurance', 'health', '401k', 'retirement',
            'hire', 'fired', 'termination', 'resignation', 'onboarding',
            'performance', 'review', 'appraisal', 'feedback',
            'policy', 'handbook', 'hr', 'human resources',
            'timesheet', 'attendance', 'schedule', 'overtime',
            'pregnant', 'pregnancy', 'rights', 'discrimination',
        ]

    def classify(self, query):
        query_lower = query.lower()
        matches = sum(1 for keyword in self.hr_keywords if keyword in query_lower)

        is_hr = matches > 0
        confidence = min(matches * 0.3, 0.95) if is_hr else 0.2

        return {
            'is_hr_related': is_hr,
            'confidence': confidence,
            'label': 'HR-related' if is_hr else 'Non-HR related',
        }

# Usage
classifier = SimpleHRClassifier()
result = classifier.classify("I am pregnant and I want to know my rights")
print(result)
```

This lightweight version doesn't require any ML packages but won't be as accurate as the transformer model.

---

## Still Having Issues?

1. **Check System Requirements**
   - Python 3.8+
   - 16GB RAM (at least 4GB free)
   - Internet connection (first run only)

2. **Try Clean Install**
   ```bash
   # Create new environment
   python -m venv clean_env
   source clean_env/bin/activate  # or clean_env\Scripts\activate on Windows
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Check Error Logs**
   - Share the full error traceback
   - Note your Python version and OS

4. **Contact Support**
   - Open an issue with:
     - Python version: `python --version`
     - OS and version
     - Full error message
     - Output of: `pip list`
