# HR Intent Classifier Chatbot

An intelligent chatbot that accurately classifies user queries as HR-related or not. It uses advanced natural language processing to understand direct questions, indirect speech, and even confusing statements related to Human Resources.

## Features

- **Accurate Classification**: Uses zero-shot classification with transformer models
- **Handles Complex Queries**: Understands indirect speech and ambiguous statements
- **Lightweight**: Runs locally on 16GB RAM without additional software
- **Easy Installation**: Only requires pip packages
- **Interactive Interface**: User-friendly command-line chatbot
- **Conversation Tracking**: History and statistics features

## Requirements

- Python 3.8 or higher
- 16GB RAM (minimum)
- Internet connection (for first-time model download only)

## Installation

1. **Clone or download this repository**

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

This will install:
- `transformers`: HuggingFace library for NLP models
- `torch`: PyTorch for model inference
- `sentencepiece`: Tokenization library
- `protobuf`: Protocol buffers for model serialization

3. **First run** (downloads the model, ~1GB):
```bash
python hr_intent_classifier.py
```

The model will be automatically downloaded and cached on first run.

## Usage

### Interactive Chatbot Mode

Simply run the script:
```bash
python hr_intent_classifier.py
```

Then type your queries and the chatbot will classify them:

```
You: How do I apply for vacation leave?
✓ HR-RELATED (confidence: 94.5%)
This query appears to be related to Human Resources topics.

You: What's the weather like today?
✗ NOT HR-RELATED (confidence: 89.2%)
This query does not appear to be related to Human Resources.
```

### Available Commands

- **Type any query**: Get classification results
- **`history`**: View all previous queries and their classifications
- **`stats`**: See statistics about your session
- **`quit`** or **`exit`**: End the session

### Programmatic Usage

You can also use the classifier in your own Python code:

```python
from hr_intent_classifier import HRIntentClassifier

# Initialize classifier
classifier = HRIntentClassifier()

# Classify a query
result = classifier.classify("Can I get my payslip?")
print(f"HR-related: {result['is_hr_related']}")
print(f"Confidence: {result['confidence']:.2%}")

# Get detailed explanation
is_hr, explanation = classifier.classify_with_explanation("I need to update my address")
print(explanation)
```

## Example Queries

### HR-Related Queries (Direct)
- "How do I apply for maternity leave?"
- "What is the company policy on remote work?"
- "When will I receive my salary?"
- "Can you help me with my performance review?"
- "I need to update my emergency contact information"

### HR-Related Queries (Indirect/Confusing)
- "My friend wants to know about the benefits here"
- "Someone told me we get bonuses, is that true?"
- "I heard something about health insurance options"
- "They said I should talk to HR about my schedule"
- "Is there a person I can speak to about workplace issues?"

### Non-HR Queries
- "What's the weather forecast for tomorrow?"
- "How do I write a Python function?"
- "Can you recommend a good restaurant?"
- "What time is it?"
- "Tell me a joke"

## How It Works

The classifier uses **zero-shot classification**, which means it can classify queries without being explicitly trained on HR-specific data. Here's how:

1. **Model**: Uses DeBERTa-v3 (a state-of-the-art transformer model)
2. **Classification**: Compares the query against predefined categories
3. **Context**: Leverages understanding of HR topics like benefits, leave, payroll, etc.
4. **Confidence**: Provides a probability score for the classification

### HR Topics Covered

- Employee benefits, compensation, salary
- Leave management (vacation, sick leave, PTO)
- Recruitment, hiring, onboarding
- Performance reviews and feedback
- Training and development
- Employee relations and conflicts
- Termination and resignation
- Company policies
- Payroll and attendance
- Health insurance and retirement plans
- Workplace safety and compliance
- Career development
- Employee engagement

## Technical Details

### Model Information
- **Model**: MoritzLaurer/deberta-v3-base-zeroshot-v1.1-all-33
- **Type**: Zero-shot classification
- **Size**: ~400MB
- **RAM Usage**: ~2-3GB during inference
- **Device**: Automatically uses GPU if available, otherwise CPU

### Performance
- **Accuracy**: High accuracy on both direct and indirect queries
- **Speed**: ~1-2 seconds per classification on CPU
- **Memory**: Optimized for 16GB RAM systems

## Customization

### Using a Different Model

You can use a different model by modifying the initialization:

```python
classifier = HRIntentClassifier(model_name="facebook/bart-large-mnli")
```

Note: Larger models may require more RAM.

### Adjusting Confidence Threshold

```python
result = classifier.classify(query, confidence_threshold=0.7)
```

### Adding Custom HR Categories

Modify the `hr_labels` in the `HRIntentClassifier` class:

```python
self.hr_labels = [
    "HR and human resources related query",
    "Non-HR related query",
    "Ambiguous query requiring clarification"
]
```

## Troubleshooting

### Out of Memory Error
- Close other applications to free up RAM
- Use a smaller model (e.g., distilbert-base-uncased)
- Ensure you have at least 16GB RAM available

### Slow Performance
- First classification is slower due to model loading
- CPU inference is slower than GPU
- Subsequent queries are faster due to model caching

### Model Download Issues
- Ensure you have internet connection
- Check firewall settings
- Models are cached in `~/.cache/huggingface/`

## License

This project uses open-source models and libraries. Please refer to their respective licenses:
- Transformers: Apache 2.0
- PyTorch: BSD-style license
- Model: Check HuggingFace model card

## Contributing

Feel free to submit issues or pull requests to improve the classifier!

## Support

For questions or issues, please open an issue in the repository.
