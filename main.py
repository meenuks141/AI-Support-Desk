import os
import json
import time
from pathlib import Path
from collections import Counter
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
if not API_KEY:
    raise SystemExit(
        "Error: GEMINI_API_KEY not found. "
        "Please add your API key to the .env file."
    )
client = genai.Client(api_key=API_KEY)
BASE_DIR = Path(__file__).resolve().parent
TICKETS_FILE = BASE_DIR / "tickets.json"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)
CATEGORIES = [
    "Billing",
    "Technical",
    "Account",
    "General",
    "Shipping",
    "Other"
]
URGENCIES = [
    "Low",
    "Medium",
    "High",
    "Critical"
]
def load_tickets():
    with open(TICKETS_FILE, "r", encoding="utf-8") as file:
        tickets = json.load(file)
    if not isinstance(tickets, list):
        raise ValueError("Tickets must be stored as a JSON list.")
    return tickets
def classify_ticket(ticket):

    prompt = f"""
You are an AI customer support ticket classifier.

Analyze the following customer support ticket.

Return ONLY a valid JSON object with this exact structure:

{{
    "category": "Billing",
    "urgency": "High",
    "suggested_action": "Contact the billing team and investigate the duplicate payment."
}}

CATEGORY OPTIONS:
- Billing
- Technical
- Account
- General
- Shipping
- Other

URGENCY OPTIONS:
- Low
- Medium
- High
- Critical

CLASSIFICATION RULES:

1. Billing: Payment, refund, subscription or invoice issues.
2. Technical: Software bugs, application crashes or technical errors.
3. Account: Login, password or account-related problems.
4. General: General questions and information requests.
5. Shipping: Delivery, tracking or package issues.
6. Other: Issues that do not fit the above categories.

Urgency:
- Low: Ordinary questions or minor requests.
- Medium: Issues requiring attention but not immediately urgent.
- High: Significant problems affecting the customer's ability to use the service.
- Critical: Serious security, safety or widespread service incidents.

Do not add explanations outside the JSON.

CUSTOMER TICKET:

Ticket ID: {ticket["id"]}
Message: {ticket["message"]}
"""
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    temperature=0.1
                )
            )
            if not response.text:
                raise ValueError("Empty response from Gemini.")
            result = json.loads(response.text)
            category = result.get("category")
            urgency = result.get("urgency")
            action = result.get("suggested_action")
            if category not in CATEGORIES:
                raise ValueError("Invalid category returned.")
            if urgency not in URGENCIES:
                raise ValueError("Invalid urgency returned.")
            if not isinstance(action, str) or not action.strip():
                raise ValueError("Invalid suggested action.")
            return {
                "ticket_id": ticket["id"],
                "customer_message": ticket["message"],
                "category": category,
                "urgency": urgency,
                "suggested_action": action.strip(),
                "status": "success"
            }
        except Exception as error:
            print(f"Error processing {ticket['id']}: {error}")
            if attempt < 2:
                wait_time = 2 ** attempt
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
    return {
        "ticket_id": ticket["id"],
        "customer_message": ticket["message"],
        "category": "Unclassified",
        "urgency": "Unknown",
        "suggested_action": "Manual review required.",
        "status": "failed"
    }
def generate_summary(results):
    successful_results = [
        ticket for ticket in results
        if ticket["status"] == "success"
    ]
    category_counts = Counter(
        ticket["category"]
        for ticket in successful_results
    )
    urgency_counts = Counter(
        ticket["urgency"]
        for ticket in successful_results
    )
    summary = {
        "total_tickets": len(results),
        "successfully_classified": len(successful_results),
        "failed_tickets": len(results) - len(successful_results),
        "tickets_by_category": dict(category_counts),
        "tickets_by_urgency": dict(urgency_counts)
    }
    return summary
def save_results(results, summary):
    results_file = OUTPUT_DIR / "classified_tickets.json"
    summary_file = OUTPUT_DIR / "summary.json"
    with open(results_file, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)
    with open(summary_file, "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4, ensure_ascii=False)
    print("\nResults saved successfully!")
def main():
    print("=" * 50)
    print("          AI SUPPORT DESK")
    print("=" * 50)
    try:
        tickets = load_tickets()
    except Exception as error:
        print(f"Unable to load tickets: {error}")
        return
    if not tickets:
        print("No tickets found.")
        return
    results = []
    print(f"\nTotal tickets: {len(tickets)}")
    print("Starting AI classification...\n")
    for index, ticket in enumerate(tickets, start=1):
        print(
            f"Processing ticket {index}/{len(tickets)}: "
            f"{ticket['id']}"
        )
        result = classify_ticket(ticket)
        results.append(result)
        print(f"Category: {result['category']}")
        print(f"Urgency: {result['urgency']}")
        print(f"Status: {result['status']}")
        print("-" * 40)
    summary = generate_summary(results)
    save_results(results, summary)
    print("\n--- FINAL SUMMARY ---")
    print("\nTotal Tickets:", summary["total_tickets"])
    print(
        "Successfully Classified:",
        summary["successfully_classified"]
    )
    print("Failed Tickets:", summary["failed_tickets"])
    print("\nTickets by Category:")
    for category, count in summary["tickets_by_category"].items():
        print(f"{category}: {count}")
    print("\nTickets by Urgency:")
    for urgency, count in summary["tickets_by_urgency"].items():
        print(f"{urgency}: {count}")
    print("\nAI Support Desk execution completed!")
if __name__ == "__main__":
    main()