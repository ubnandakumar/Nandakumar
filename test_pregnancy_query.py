"""
Quick test for specific prompt
"""

from hr_intent_classifier import HRIntentClassifier

# Initialize classifier
print("Loading classifier...")
classifier = HRIntentClassifier()

# Test the specific prompt
query = "I am pregnant and I want to know my rights"

print("\n" + "=" * 70)
print("TESTING SPECIFIC QUERY")
print("=" * 70)
print(f"\nQuery: \"{query}\"\n")

# Get classification
result = classifier.classify(query)
is_hr, explanation = classifier.classify_with_explanation(query)

# Show detailed results
print(explanation)
print(f"\nDetailed scores:")
for label, score in result['all_scores'].items():
    print(f"  - {label}: {score:.2%}")

print("\n" + "=" * 70)
print("ANALYSIS")
print("=" * 70)
print("""
This query is about pregnancy rights, which falls under HR topics:
- Maternity leave policies
- Pregnancy-related workplace accommodations
- Employee benefits during pregnancy
- Legal rights and protections (FMLA, pregnancy discrimination)
- Healthcare and insurance coverage

The classifier should identify this as strongly HR-related because it involves:
1. Employee rights (HR policy domain)
2. Pregnancy/maternity (core HR benefit category)
3. Legal compliance (HR responsibility)
""")
print("=" * 70)
