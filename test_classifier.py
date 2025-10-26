"""
Test script for HR Intent Classifier
Demonstrates classification on various types of queries
"""

from hr_intent_classifier import HRIntentClassifier


def test_classifier():
    """Test the classifier with various query types."""

    print("Initializing HR Intent Classifier...")
    classifier = HRIntentClassifier()

    # Test cases: (query, expected_is_hr)
    test_cases = [
        # Direct HR-related queries
        ("How do I apply for vacation leave?", True),
        ("What is my current salary?", True),
        ("Can I get a copy of my payslip?", True),
        ("I want to update my emergency contact information", True),
        ("When is the next performance review?", True),
        ("How do I enroll in health insurance?", True),
        ("What are the company policies on remote work?", True),
        ("I need to submit my timesheet", True),
        ("Can I speak to someone about workplace harassment?", True),
        ("How much PTO do I have left?", True),

        # Indirect/Confusing HR-related queries
        ("My friend wants to know about benefits here", True),
        ("Someone told me we get bonuses, is that true?", True),
        ("I heard something about maternity leave options", True),
        ("They said I should talk to someone about my schedule", True),
        ("Is there a person I can speak to about my paycheck?", True),
        ("I'm confused about the 401k matching", True),
        ("What happens if I want to leave the company?", True),
        ("Do we have any training programs?", True),
        ("I think my coworker mentioned something about raises", True),
        ("Can someone explain the employee handbook?", True),

        # Non-HR queries
        ("What's the weather like today?", False),
        ("How do I write a Python function?", False),
        ("Can you recommend a good restaurant?", False),
        ("What time is it?", False),
        ("Tell me a joke", False),
        ("How do I bake a cake?", False),
        ("What's the capital of France?", False),
        ("Can you help me with my math homework?", False),
        ("What's the latest news?", False),
        ("How do I fix my car?", False),

        # Edge cases - ambiguous queries
        ("I have a question", None),  # Too vague
        ("Can you help me?", None),  # Too vague
        ("I need information", None),  # Too vague
        ("What should I do about my manager asking me to work overtime?", True),  # Context-dependent
        ("How do I talk to my boss?", True),  # Could be HR-related
    ]

    print("\n" + "=" * 80)
    print("TESTING HR INTENT CLASSIFIER")
    print("=" * 80)
    print()

    correct = 0
    total = 0

    for query, expected in test_cases:
        result = classifier.classify(query)
        is_hr = result['is_hr_related']
        confidence = result['confidence']

        # Determine if prediction is correct
        if expected is not None:
            is_correct = is_hr == expected
            if is_correct:
                correct += 1
            total += 1
            status = "✓" if is_correct else "✗"
        else:
            status = "~"  # Ambiguous case

        # Display result
        hr_label = "HR" if is_hr else "Non-HR"
        print(f"{status} [{hr_label:8}] {confidence:5.1%} | {query}")

        # Show detailed scores for edge cases
        if expected is None:
            print(f"           Scores: {result['all_scores']}")

    print()
    print("=" * 80)
    if total > 0:
        accuracy = (correct / total) * 100
        print(f"RESULTS: {correct}/{total} correct ({accuracy:.1f}% accuracy)")
    print("=" * 80)
    print()

    # Additional detailed test
    print("\nDETAILED TEST EXAMPLES:")
    print("-" * 80)

    detailed_queries = [
        "I need to know how to request time off for a doctor's appointment",
        "What's the process for getting reimbursed for work expenses?",
        "Can you help me debug this Python code?",
        "I think there's an issue with my last paycheck, it seems too low",
    ]

    for query in detailed_queries:
        is_hr, explanation = classifier.classify_with_explanation(query)
        print(f"\nQuery: {query}")
        print(explanation)
        print("-" * 80)


if __name__ == "__main__":
    test_classifier()
