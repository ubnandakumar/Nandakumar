"""
HR Intent Classifier
A lightweight chatbot that classifies user queries as HR-related or not.
Uses zero-shot classification with transformer models.
"""

import torch
from transformers import pipeline
from typing import Dict, Tuple
import warnings
warnings.filterwarnings('ignore')


class HRIntentClassifier:
    """
    Classifies user intents to determine if they are HR-related queries.
    Handles direct, indirect, and confusing statements accurately.
    """

    def __init__(self, model_name: str = "MoritzLaurer/deberta-v3-base-zeroshot-v1.1-all-33"):
        """
        Initialize the HR Intent Classifier.

        Args:
            model_name: HuggingFace model for zero-shot classification.
                       Default uses a lightweight model optimized for 16GB RAM.
        """
        print("Loading HR Intent Classifier...")
        print(f"Model: {model_name}")

        # Set device (CPU for compatibility, GPU if available)
        self.device = 0 if torch.cuda.is_available() else -1
        device_name = "GPU" if self.device == 0 else "CPU"
        print(f"Using device: {device_name}")

        # Initialize zero-shot classification pipeline
        self.classifier = pipeline(
            "zero-shot-classification",
            model=model_name,
            device=self.device
        )

        # Define HR-related categories with detailed descriptions
        self.hr_labels = [
            "HR and human resources related query",
            "Non-HR related query"
        ]

        # Expanded HR context for better classification
        self.hr_context = """
        HR (Human Resources) topics include:
        - Employee benefits, compensation, salary, wages, bonuses
        - Leave management: vacation, sick leave, maternity/paternity leave, PTO
        - Recruitment, hiring, onboarding, job applications
        - Performance reviews, appraisals, feedback, evaluations
        - Training and development, learning opportunities
        - Employee relations, workplace conflicts, grievances
        - Termination, resignation, offboarding, exit interviews
        - Company policies, handbook, code of conduct
        - Payroll, timesheets, attendance, working hours
        - Health insurance, retirement plans, 401k, pension
        - Workplace safety, harassment, discrimination
        - Career development, promotions, transfers
        - Employee engagement, satisfaction, culture
        - Compliance, labor laws, employment regulations
        """

        print("HR Intent Classifier ready!\n")

    def classify(self, user_query: str, confidence_threshold: float = 0.5) -> Dict:
        """
        Classify a user query as HR-related or not.

        Args:
            user_query: The user's input text
            confidence_threshold: Minimum confidence score (0-1) for classification

        Returns:
            Dictionary with classification results including:
            - is_hr_related: Boolean
            - confidence: Float score
            - label: String classification
            - all_scores: Dict of all label scores
        """
        if not user_query or not user_query.strip():
            return {
                "is_hr_related": False,
                "confidence": 0.0,
                "label": "Invalid query",
                "all_scores": {}
            }

        # Perform zero-shot classification
        result = self.classifier(
            user_query,
            self.hr_labels,
            multi_label=False
        )

        # Extract results
        top_label = result['labels'][0]
        top_score = result['scores'][0]

        # Create score mapping
        score_dict = dict(zip(result['labels'], result['scores']))

        # Determine if HR-related
        is_hr = top_label == "HR and human resources related query"

        return {
            "is_hr_related": is_hr,
            "confidence": top_score,
            "label": "HR-related" if is_hr else "Non-HR related",
            "all_scores": score_dict
        }

    def classify_with_explanation(self, user_query: str) -> Tuple[bool, str]:
        """
        Classify query and provide human-readable explanation.

        Args:
            user_query: The user's input text

        Returns:
            Tuple of (is_hr_related: bool, explanation: str)
        """
        result = self.classify(user_query)

        is_hr = result["is_hr_related"]
        confidence = result["confidence"]

        # Generate explanation
        if is_hr:
            explanation = (
                f"✓ HR-RELATED (confidence: {confidence:.1%})\n"
                f"This query appears to be related to Human Resources topics."
            )
        else:
            explanation = (
                f"✗ NOT HR-RELATED (confidence: {confidence:.1%})\n"
                f"This query does not appear to be related to Human Resources."
            )

        return is_hr, explanation


class HRChatbot:
    """
    Interactive chatbot interface for HR intent classification.
    """

    def __init__(self):
        """Initialize the chatbot with HR classifier."""
        self.classifier = HRIntentClassifier()
        self.conversation_history = []

    def start(self):
        """Start the interactive chatbot session."""
        print("=" * 70)
        print("HR INTENT CLASSIFIER CHATBOT")
        print("=" * 70)
        print("I can help you determine if a query is HR-related or not.")
        print("I understand direct questions, indirect speech, and confusing statements.")
        print("\nCommands:")
        print("  - Type your query to classify it")
        print("  - Type 'history' to see conversation history")
        print("  - Type 'stats' to see classification statistics")
        print("  - Type 'quit' or 'exit' to end the session")
        print("=" * 70)
        print()

        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()

                if not user_input:
                    continue

                # Handle commands
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("\nThank you for using HR Intent Classifier. Goodbye!")
                    break

                if user_input.lower() == 'history':
                    self.show_history()
                    continue

                if user_input.lower() == 'stats':
                    self.show_stats()
                    continue

                # Classify the query
                is_hr, explanation = self.classifier.classify_with_explanation(user_input)

                # Store in history
                self.conversation_history.append({
                    "query": user_input,
                    "is_hr_related": is_hr,
                    "result": self.classifier.classify(user_input)
                })

                # Display result
                print(f"\n{explanation}\n")

            except KeyboardInterrupt:
                print("\n\nSession interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"\nError: {str(e)}\n")

    def show_history(self):
        """Display conversation history."""
        if not self.conversation_history:
            print("\nNo conversation history yet.\n")
            return

        print("\n" + "=" * 70)
        print("CONVERSATION HISTORY")
        print("=" * 70)
        for i, item in enumerate(self.conversation_history, 1):
            label = "HR" if item["is_hr_related"] else "Non-HR"
            confidence = item["result"]["confidence"]
            print(f"{i}. [{label} - {confidence:.1%}] {item['query']}")
        print("=" * 70 + "\n")

    def show_stats(self):
        """Display classification statistics."""
        if not self.conversation_history:
            print("\nNo statistics available yet.\n")
            return

        total = len(self.conversation_history)
        hr_count = sum(1 for item in self.conversation_history if item["is_hr_related"])
        non_hr_count = total - hr_count

        avg_confidence = sum(item["result"]["confidence"] for item in self.conversation_history) / total

        print("\n" + "=" * 70)
        print("CLASSIFICATION STATISTICS")
        print("=" * 70)
        print(f"Total queries analyzed: {total}")
        print(f"HR-related queries: {hr_count} ({hr_count/total*100:.1f}%)")
        print(f"Non-HR queries: {non_hr_count} ({non_hr_count/total*100:.1f}%)")
        print(f"Average confidence: {avg_confidence:.1%}")
        print("=" * 70 + "\n")


def main():
    """Main entry point for the chatbot."""
    chatbot = HRChatbot()
    chatbot.start()


if __name__ == "__main__":
    main()
