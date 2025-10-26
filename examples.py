"""
Usage Examples for HR Intent Classifier

This file demonstrates various ways to use the HR Intent Classifier
in your own applications.
"""

from hr_intent_classifier import HRIntentClassifier, HRChatbot


def example_1_basic_classification():
    """Example 1: Basic classification of a single query."""
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Basic Classification")
    print("=" * 70)

    classifier = HRIntentClassifier()

    query = "How do I apply for parental leave?"
    result = classifier.classify(query)

    print(f"Query: {query}")
    print(f"Is HR-related: {result['is_hr_related']}")
    print(f"Confidence: {result['confidence']:.2%}")
    print(f"Label: {result['label']}")


def example_2_batch_classification():
    """Example 2: Classify multiple queries in batch."""
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Batch Classification")
    print("=" * 70)

    classifier = HRIntentClassifier()

    queries = [
        "What's the company policy on sick leave?",
        "How do I make a pizza?",
        "I want to discuss my career progression",
        "What's the weather today?",
    ]

    for query in queries:
        result = classifier.classify(query)
        label = "HR" if result['is_hr_related'] else "Non-HR"
        print(f"[{label:6}] {result['confidence']:.1%} - {query}")


def example_3_with_explanation():
    """Example 3: Get classification with explanation."""
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Classification with Explanation")
    print("=" * 70)

    classifier = HRIntentClassifier()

    query = "Someone mentioned something about health insurance benefits"
    is_hr, explanation = classifier.classify_with_explanation(query)

    print(f"Query: {query}")
    print(explanation)


def example_4_filtering_hr_queries():
    """Example 4: Filter HR queries from a mixed list."""
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Filtering HR Queries")
    print("=" * 70)

    classifier = HRIntentClassifier()

    all_queries = [
        "I need help with my 401k enrollment",
        "What's the best programming language?",
        "How do I submit my expense report?",
        "Can you recommend a good movie?",
        "I want to update my direct deposit information",
    ]

    hr_queries = []
    non_hr_queries = []

    for query in all_queries:
        result = classifier.classify(query)
        if result['is_hr_related']:
            hr_queries.append(query)
        else:
            non_hr_queries.append(query)

    print("HR-RELATED QUERIES:")
    for q in hr_queries:
        print(f"  - {q}")

    print("\nNON-HR QUERIES:")
    for q in non_hr_queries:
        print(f"  - {q}")


def example_5_confidence_threshold():
    """Example 5: Using confidence threshold for uncertain queries."""
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Using Confidence Threshold")
    print("=" * 70)

    classifier = HRIntentClassifier()

    queries = [
        "How do I request vacation time?",  # Clear HR
        "I need help",  # Ambiguous
        "What's 2+2?",  # Clear non-HR
    ]

    confidence_threshold = 0.7

    for query in queries:
        result = classifier.classify(query)
        confidence = result['confidence']

        if confidence >= confidence_threshold:
            label = "HR" if result['is_hr_related'] else "Non-HR"
            print(f"[{label:6}] {confidence:.1%} - {query}")
        else:
            print(f"[UNSURE] {confidence:.1%} - {query} (needs clarification)")


def example_6_routing_system():
    """Example 6: Route queries to appropriate department."""
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Query Routing System")
    print("=" * 70)

    classifier = HRIntentClassifier()

    def route_query(query):
        """Route query to the appropriate department."""
        result = classifier.classify(query)

        if result['is_hr_related'] and result['confidence'] >= 0.6:
            return "HR Department"
        else:
            return "General Support"

    queries = [
        "I need to update my tax withholding",
        "The printer is broken",
        "Can I change my work schedule?",
        "The WiFi isn't working",
    ]

    for query in queries:
        department = route_query(query)
        print(f"[{department:18}] {query}")


def example_7_interactive_chatbot():
    """Example 7: Run the interactive chatbot."""
    print("\n" + "=" * 70)
    print("EXAMPLE 7: Interactive Chatbot")
    print("=" * 70)
    print("To run the interactive chatbot, use:")
    print("  python hr_intent_classifier.py")
    print("\nOr programmatically:")
    print("  chatbot = HRChatbot()")
    print("  chatbot.start()")


def example_8_integration_pattern():
    """Example 8: Integration pattern for existing applications."""
    print("\n" + "=" * 70)
    print("EXAMPLE 8: Integration Pattern")
    print("=" * 70)

    # Initialize once (e.g., at application startup)
    classifier = HRIntentClassifier()

    def handle_user_message(user_message: str):
        """
        Example handler for user messages in your application.
        """
        # Classify the message
        result = classifier.classify(user_message)

        if result['is_hr_related']:
            # Route to HR bot or HR support
            response = f"I've identified this as an HR-related query. "
            response += f"Let me connect you with our HR support team..."
            return response
        else:
            # Handle as general query
            response = f"I can help you with that. "
            response += f"This appears to be a general inquiry..."
            return response

    # Example usage
    user_messages = [
        "I want to know my remaining vacation days",
        "What's the company's address?",
    ]

    for msg in user_messages:
        response = handle_user_message(msg)
        print(f"User: {msg}")
        print(f"Bot: {response}\n")


def run_all_examples():
    """Run all examples."""
    print("\n" + "=" * 70)
    print("HR INTENT CLASSIFIER - USAGE EXAMPLES")
    print("=" * 70)

    example_1_basic_classification()
    example_2_batch_classification()
    example_3_with_explanation()
    example_4_filtering_hr_queries()
    example_5_confidence_threshold()
    example_6_routing_system()
    example_7_interactive_chatbot()
    example_8_integration_pattern()

    print("\n" + "=" * 70)
    print("All examples completed!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    run_all_examples()
