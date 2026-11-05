# AI Support Desk

An AI-powered customer support ticket classification system built using Python and Google’s Gemini API.

## Project Overview

AI Support Desk is a Python-based application that processes customer support tickets using a Large Language Model (LLM).

It analyzes customer messages and automatically identifies their category, urgency level, and suggested support action.

The application converts unstructured customer complaints and questions into structured JSON data, making support-ticket management easier and more efficient.

## Features

* AI-powered customer support ticket classification.
* Automatic category identification.
* Urgency detection.
* AI-generated suggested support actions.
* Structured JSON response generation.
* JSON parsing and validation.
* API error handling and retry mechanism.
* Graceful handling of failed classifications.
* Automatic summary generation by category and urgency.
* Secure API key management using environment variables.

## Technologies Used

* Python
* Google Gemini API
* Google GenAI SDK
* JSON
* python-dotenv

## Project Structure

AI-Support-Desk/
│
├── main.py
├── tickets.json
├── test_gemini.py
├── list_models.py
│
├── requirements.txt
├── .env.example
├── .gitignore
│
├── README.md
├── obstacle_log.md
│
└── output/
    ├── classified_tickets.json
    └── summary.json

## Ticket Categories

The application classifies tickets into six categories:

1. Billing
2. Technical
3. Account
4. General
5. Shipping
6. Other

## Urgency Levels

Each ticket is assigned one of four urgency levels:

* Low: Ordinary questions or minor requests.
* Medium: Issues requiring attention but not immediately urgent.
* High: Significant problems affecting the customer’s ability to use the service.
* Critical: Serious security, safety, or widespread service incidents.

## Installation and Setup

1. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_LINK

Navigate into the project directory:

cd AI-Support-Desk

2. Create a Virtual Environment

python -m venv .venv

Activate it on macOS/Linux:

source .venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure the Gemini API Key

Create a .env file in the project directory.

Add the following configuration:

GEMINI_API_KEY=your_actual_api_key
GEMINI_MODEL=gemini-3.6-flash

Replace the placeholder with your own Gemini API key.

Note: Never upload your .env file or expose your API key publicly.

5. Run the Application

python main.py

## Generated Outputs

After execution, the application automatically creates an output directory containing two JSON files.

1. classified_tickets.json

Contains the classification results for individual tickets, including:

* Ticket ID
* Customer message
* Category
* Urgency
* Suggested action
* Processing status

2. summary.json

Contains the overall processing summary:

* Total number of tickets.
* Successfully classified tickets.
* Failed tickets.
* Ticket counts by category.
* Ticket counts by urgency.

## Error Handling

The application includes error handling for:

* Gemini API request failures.
* Empty API responses.
* Invalid JSON responses.
* Unexpected classification values.
* Failed ticket processing.

Unsuccessful classifications are marked as failed and assigned a manual review status.

## Security

API credentials are stored in environment variables using a .env file.

The .gitignore file excludes sensitive files and unnecessary development folders, including:

* .env
* .venv/
* venv/
* __pycache__/

## Conclusion

The AI Support Desk demonstrates the practical application of Large Language Models in customer support automation.

By combining Python, the Gemini API, and structured JSON processing, the project transforms customer support messages into actionable information through automated classification, urgency detection, and suggested support actions.
