# WhatsApp Chatbot with AWS Lambda and Google Gemini API

This project implements a WhatsApp chatbot using AWS Lambda, integrated with the WhatsApp Business API and Google's Gemini API for generating responses. The chatbot processes incoming messages and sends automated replies.

## Overview

The code is a Python-based AWS Lambda function that:
1. Verifies webhook subscriptions from WhatsApp
2. Processes incoming WhatsApp messages
3. Integrates with Google's Gemini API for potential response generation
4. Sends replies back to users via the WhatsApp Business API

## Prerequisites

- AWS account with Lambda configured
- WhatsApp Business API access
- Google Cloud account with Gemini API enabled
- Environment variables configured in AWS Lambda

## Environment Variables

The following environment variables must be set in AWS Lambda:

- `VERIFY_TOKEN`: Webhook verification token from WhatsApp
- `WHATSAPP_TOKEN`: Access token for WhatsApp Business API
- `PHONE_NUMBER_ID`: WhatsApp Business phone number ID
- `GOOGLE_API_KEY`: API key for Google Gemini API

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-folder>
```

2. Install dependencies:
```bash
pip install requests google-genai -t .
```

3. Package the code for Lambda:
```bash
zip -r lambda_function.zip .
```

4. Upload the zip file to AWS Lambda

## Code Structure

- `lambda_function.py`: Main Lambda handler and supporting functions
  - `lambda_handler`: Entry point for AWS Lambda
  - `verify_webhook`: Handles webhook verification
  - `process_message`: Processes incoming messages
  - `generate_agent_response`: Integrates with Gemini API

## Functionality

### Webhook Verification
- Handles GET requests from WhatsApp for webhook verification
- Validates the verification token and returns the challenge

### Message Processing
- Handles POST requests containing WhatsApp messages
- Extracts sender information
- Currently sends a static response (customizable)
- Includes capability to generate responses using Gemini API

### API Integration
- WhatsApp Business API for sending/receiving messages
- Google Gemini API for response generation (partially implemented)

## Usage

1. Deploy the Lambda function
2. Configure the WhatsApp webhook to point to your Lambda URL
3. Set up environment variables in AWS Lambda
4. Test by sending a WhatsApp message to your registered number

## Current Features
- Webhook verification
- Basic message processing
- Static automated responses
- Google Gemini API integration (stubbed)

## TODO
- Implement dynamic responses using Gemini API
- Add error handling for API failures
- Support for different message types (media, location, etc.)
- Add conversation context management

## Dependencies
- `requests`: For making HTTP requests to WhatsApp API
- `google-genai`: Google Gemini API client library
- `json`: For parsing webhook payloads
- `os`: For accessing environment variables

## License
[Specify your license here]

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing-feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a pull request
```

This README provides a comprehensive overview of the project, including setup instructions, functionality description, and future improvement suggestions. You can customize the License section and add any additional details specific to your deployment or requirements.

Note: The code provided has some commented-out sections and appears to be a work in progress (e.g., the `generate_agent_response` function isn't fully utilized). The README reflects both the current state and potential future development directions.