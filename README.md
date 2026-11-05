AI Support Desk

An AI-powered customer support ticket classification system built using Python and Google’s Gemini API.

Project Overview

The AI Support Desk processes customer support tickets using a Large Language Model (LLM). It automatically identifies the category and urgency of each ticket and recommends an appropriate support action.

Features

* AI-powered ticket classification.
* Automatic category identification.
* Urgency detection.
* Suggested support actions.
* JSON response parsing.
* API error handling and retry mechanism.
* Automatic summary generation.
* Secure API key management using environment variables.

Technologies Used

* Python
* Google Gemini API
* Google GenAI SDK
* JSON
* python-dotenv

Project Structure

AI_Support_Desk/
│
├── main.py
├── tickets.json
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── obstacle_log.md
│
└── output/
    ├── classified_tickets.json
    └── summary.json

Ticket Categories

1. Billing
2. Technical
3. Account
4. General
5. Shipping
6. Other

Urgency Levels

* Low
* Medium
* High
* Critical

Installation

Install the required dependencies:

pip install -r requirements.txt

Create a .env file and configure your Gemini API key.

GEMINI_API_KEY=your_api_key
GEMINI_MODEL=gemini-2.5-flash

Execution

Run the following command:

python main.py

Generated Outputs

The application automatically generates:

* classified_tickets.json: Contains the classification results for individual tickets.
* summary.json: Contains ticket counts grouped by category and urgency.

Error Handling

The application includes:

* API exception handling.
* JSON parsing validation.
* Retry attempts for failed requests.
* Manual review status for unsuccessful classifications.

Security

API credentials are stored in a .env file and excluded from version control using .gitignore.

Conclusion

The AI Support Desk demonstrates the practical use of Large Language Models in automating customer support workflows through structured classification, urgency detection, and actionable recommendations.