Obstacle Log – AI Support Desk

Project: AI Support Desk

1. API Integration Issues

Obstacle: Connecting the Python application with the Gemini API required installing the appropriate SDK and configuring API authentication.

Solution: Installed the Google GenAI SDK and configured the API key using environment variables and the python-dotenv library.

2. JSON Response Formatting

Obstacle: LLM responses may sometimes contain unexpected formatting, making them difficult to parse.

Solution: Used JSON response mode and Python’s json.loads() function to process the model response. Added validation to ensure the expected fields were returned.

3. API Errors and Failed Requests

Obstacle: Temporary API failures and unavailable model responses can interrupt ticket processing.

Solution: Implemented try-except handling and retry attempts. Tickets that repeatedly fail are marked for manual review.

4. API Key Security

Obstacle: Storing API credentials directly in Python source code can expose sensitive information.

Solution: Stored the API key in a separate .env file and added it to .gitignore to prevent accidental uploads.

5. Structured Summary Generation

Obstacle: Individual ticket classifications needed to be converted into a consolidated overview.

Solution: Used Python’s Counter module to calculate ticket counts by category and urgency.

Testing Notes

* Programming Language: Python
* LLM: Google Gemini
* Libraries: Google GenAI, python-dotenv
* Number of Sample Tickets: 7
* Output Format: JSON

Conclusion

The project demonstrates how an LLM can automate customer support ticket classification and transform unstructured customer messages into structured information. Error handling and summary generation make the application more reliable and useful.