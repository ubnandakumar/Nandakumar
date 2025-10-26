# Installation Guide

## Quick Fix (For the Import Error)

If you're seeing the error:
```
ImportError: cannot import name 'split_torch_state_dict_into_shards' from 'huggingface_hub'
```

### Option 1: Automated Fix (Recommended)

**On Windows:**
```bash
fix_dependencies.bat
```

**On Linux/Mac:**
```bash
chmod +x fix_dependencies.sh
./fix_dependencies.sh
```

### Option 2: Manual Fix

Follow these steps **exactly** in your command prompt/terminal:

#### Step 1: Uninstall Conflicting Packages

```bash
pip uninstall transformers huggingface-hub accelerate -y
```

#### Step 2: Upgrade Pip

```bash
python -m pip install --upgrade pip
```

#### Step 3: Install Specific Compatible Versions

**Copy and paste these commands ONE AT A TIME:**

```bash
pip install huggingface-hub==0.20.3
```

```bash
pip install accelerate==0.26.1
```

```bash
pip install transformers==4.37.2
```

```bash
pip install torch
```

```bash
pip install sentencepiece protobuf
```

#### Step 4: Verify Installation

```bash
python -c "from transformers import pipeline; print('Success!')"
```

If you see "Success!", you're ready to go!

#### Step 5: Test the Classifier

```bash
python test_pregnancy_query.py
```

---

## Clean Install (If Above Doesn't Work)

If you're still having issues, do a completely clean installation:

### Windows

```cmd
# 1. Create a new virtual environment
python -m venv hr_env

# 2. Activate it
hr_env\Scripts\activate

# 3. Upgrade pip
python -m pip install --upgrade pip

# 4. Install packages
pip install huggingface-hub==0.20.3
pip install accelerate==0.26.1
pip install transformers==4.37.2
pip install torch sentencepiece protobuf

# 5. Test
python test_pregnancy_query.py
```

### Linux/Mac

```bash
# 1. Create a new virtual environment
python3 -m venv hr_env

# 2. Activate it
source hr_env/bin/activate

# 3. Upgrade pip
python -m pip install --upgrade pip

# 4. Install packages
pip install huggingface-hub==0.20.3
pip install accelerate==0.26.1
pip install transformers==4.37.2
pip install torch sentencepiece protobuf

# 5. Test
python test_pregnancy_query.py
```

---

## What These Versions Mean

These are **tested, compatible versions** that work together:

| Package | Version | Purpose |
|---------|---------|---------|
| transformers | 4.37.2 | NLP library from HuggingFace |
| huggingface-hub | 0.20.3 | Model downloading and management |
| accelerate | 0.26.1 | Training/inference acceleration |
| torch | 2.0+ | PyTorch deep learning framework |
| sentencepiece | 0.1.99+ | Tokenization |
| protobuf | 3.20+ | Serialization |

---

## Checking Your Current Versions

To see what you currently have installed:

```bash
pip list | findstr "transformers huggingface-hub accelerate torch"
```

**On Linux/Mac:**
```bash
pip list | grep -E "transformers|huggingface-hub|accelerate|torch"
```

---

## Still Not Working?

### 1. Check Python Version

```bash
python --version
```

Should be **Python 3.8 or higher** (3.10+ recommended).

### 2. Check Available RAM

You need at least **4-5GB free RAM**:

```bash
# Windows PowerShell
Get-CimInstance Win32_OperatingSystem | Select FreePhysicalMemory

# Linux
free -h
```

### 3. Try Alternative Model

If the default model is causing issues, edit `hr_intent_classifier.py`:

Change line 21 from:
```python
def __init__(self, model_name: str = "MoritzLaurer/deberta-v3-base-zeroshot-v1.1-all-33"):
```

To:
```python
def __init__(self, model_name: str = "facebook/bart-large-mnli"):
```

### 4. Use Lightweight Version (No ML)

If all else fails, use the rule-based version from `TROUBLESHOOTING.md`.

---

## Verification Checklist

After installation, verify everything works:

- [ ] Python imports work: `python -c "from transformers import pipeline; print('OK')"`
- [ ] Test script runs: `python test_pregnancy_query.py`
- [ ] Chatbot starts: `python hr_intent_classifier.py`
- [ ] No memory errors
- [ ] Model downloads successfully (first run only, ~1GB)

---

## Getting Help

If you're still stuck:

1. Check TROUBLESHOOTING.md
2. Run this diagnostic:
   ```bash
   python --version
   pip list
   python -c "import sys; print(sys.executable)"
   ```
3. Share the output when asking for help

---

## Success!

Once everything is working, you should see:

```
$ python test_pregnancy_query.py

Loading HR Intent Classifier...
Model: MoritzLaurer/deberta-v3-base-zeroshot-v1.1-all-33
Using device: CPU
HR Intent Classifier ready!

======================================================================
TESTING SPECIFIC QUERY
======================================================================

Query: "I am pregnant and I want to know my rights"

✓ HR-RELATED (confidence: 92.5%)
This query appears to be related to Human Resources topics.
```

🎉 You're all set!
