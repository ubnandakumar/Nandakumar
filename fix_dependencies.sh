#!/bin/bash

echo "========================================"
echo "HR Intent Classifier - Dependency Fix"
echo "========================================"
echo ""
echo "This script will fix the package compatibility issues."
echo ""
read -p "Press Enter to continue..."

echo ""
echo "Step 1: Uninstalling conflicting packages..."
echo ""
pip uninstall transformers huggingface-hub accelerate -y

echo ""
echo "Step 2: Upgrading pip..."
echo ""
python -m pip install --upgrade pip

echo ""
echo "Step 3: Installing compatible versions..."
echo ""
pip install huggingface-hub==0.20.3
pip install accelerate==0.26.1
pip install transformers==4.37.2
pip install torch>=2.0.0
pip install sentencepiece>=0.1.99
pip install protobuf>=3.20.0

echo ""
echo "Step 4: Verifying installation..."
echo ""
python -c "from transformers import pipeline; print('SUCCESS: All packages installed correctly!')"

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "Installation completed successfully!"
    echo "========================================"
    echo ""
    echo "You can now run:"
    echo "  python test_pregnancy_query.py"
    echo "  python hr_intent_classifier.py"
    echo ""
else
    echo ""
    echo "========================================"
    echo "ERROR: Installation failed"
    echo "========================================"
    echo "Please check the error messages above."
    echo ""
fi
