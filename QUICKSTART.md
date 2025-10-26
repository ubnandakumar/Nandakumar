# Quick Start Guide

Get started with the HR Intent Classifier in 3 simple steps!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note**: This will install PyTorch, Transformers, and other required packages. Installation may take a few minutes.

## Step 2: Run the Chatbot

```bash
python hr_intent_classifier.py
```

**First run**: The model (~1GB) will be automatically downloaded. This happens only once.

## Step 3: Test with Queries

Try these example queries:

### HR-Related Examples
```
You: How do I apply for vacation leave?
You: What's the policy on sick days?
You: I need help with my paycheck
You: Can I update my emergency contact?
```

### Non-HR Examples
```
You: What's the weather today?
You: How do I code in Python?
You: Tell me a joke
You: What time is it?
```

### Indirect/Confusing Examples
```
You: Someone told me we get bonuses
You: My friend asked about health insurance here
You: I heard something about maternity leave
You: They said I should talk to someone about my hours
```

## Commands

While chatting:
- `history` - View conversation history
- `stats` - See classification statistics
- `quit` or `exit` - End session

## Run Examples

See more usage examples:
```bash
python examples.py
```

## Run Tests

Test the classifier accuracy:
```bash
python test_classifier.py
```

## System Requirements

- **Python**: 3.8 or higher
- **RAM**: 16GB minimum
- **Disk**: ~2GB for model and dependencies
- **Internet**: Required for first-time model download only

## Troubleshooting

### "Out of memory" error
- Close other applications
- Ensure you have 16GB RAM available
- Check system resources: `top` or `htop`

### "Model download failed"
- Check internet connection
- Verify firewall settings
- Try again (downloads resume automatically)

### Slow performance
- First run is slower (model loading)
- CPU inference is normal (1-2 seconds per query)
- Subsequent queries are faster

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [examples.py](examples.py) for integration patterns
- Run [test_classifier.py](test_classifier.py) to see accuracy metrics

## Need Help?

- Check the README.md for detailed information
- Review examples.py for usage patterns
- Open an issue if you encounter problems

---

**Ready to start? Run**: `python hr_intent_classifier.py`
