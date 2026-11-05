# Obstacle Log – AI Support Desk

## Project Overview

The AI Support Desk project uses Python and Google’s Gemini API to classify customer support tickets based on category, urgency, and suggested actions.

During development and testing, I encountered the following challenges.

## 1. Gemini API Configuration

Obstacle:

Initially, connecting the Python application to the Gemini API required configuring the API key and setting up the appropriate SDK.

Solution:

Installed the Google GenAI SDK and python-dotenv package. Stored the API key in a .env file and loaded it using load_dotenv().

Created a separate test_gemini.py script to verify the API connection before running the main application.

## 2. Structured JSON Responses

Obstacle:

The application needed consistent responses from the LLM instead of ordinary descriptive text. Unstructured responses could create difficulties during JSON parsing.

Solution:

Designed a specific prompt that instructed Gemini to return JSON containing exactly three fields:

* category
* urgency
* suggested_action

Used JSON response configuration and Python’s json.loads() to parse the response.

Added validation to ensure the returned category, urgency, and suggested action followed the expected structure.

## 3. API Rate Limit Exceeded

Obstacle:

While processing seven sample tickets, the Gemini API returned a 429 RESOURCE_EXHAUSTED error after processing five tickets successfully.

The error occurred because the free-tier request-per-minute quota had been exceeded.

Solution:

Implemented a try/except mechanism with retry attempts to prevent API failures from crashing the application.

Tickets that could not be processed after the retry attempts were marked as failed and assigned a manual review status.

A longer retry delay and request spacing were identified as improvements for handling rate limits more effectively.

## 4. Handling Failed Classifications

Obstacle:

The application needed to continue processing even when an individual ticket failed because of an API error or an invalid response.

Solution:

Implemented exception handling and returned a fallback result for unsuccessful classifications.

Failed tickets were assigned:

* Category: Unclassified
* Urgency: Unknown
* Suggested Action: Manual review required.
* Status: Failed

This allowed the remaining application workflow and summary generation to continue.

## 5. Generating Classification Summaries

Obstacle:

After processing the tickets, the results needed to be organized into a summary showing the number of tickets in each category and urgency level.

Solution:

Used Python’s Counter from the collections module to calculate ticket counts.

Generated separate JSON files for classified ticket results and the overall summary.

## 6. API Key Security

Obstacle:

The Gemini API key needed to be protected when publishing the project to GitHub.

Solution:

Stored the API key in a local .env file and configured .gitignore to exclude it from version control.

Created a .env.example file containing placeholder configuration for other developers.

## Testing Results

The application was tested using seven sample customer support tickets.

Metric	Result
Total Tickets	7
Successfully Classified	5
Failed Tickets	2

The five successful classifications demonstrated the expected category and urgency identification.

The remaining two tickets demonstrated the application’s API error-handling and failure-management functionality.

## Conclusion

The development process provided practical experience in integrating an LLM with Python, generating structured JSON responses, handling API exceptions, managing API credentials, and producing automated summaries.

The project also highlighted the importance of understanding API rate limits and implementing appropriate retry strategies.
