import json
import requests
import os
from google import genai

VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
WHATSAPP_TOKEN = os.environ['WHATSAPP_TOKEN']
PHONE_NUMBER_ID = os.environ['PHONE_NUMBER_ID']
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

client = genai.Client(api_key=GOOGLE_API_KEY)


def generate_agent_response(prompt):
    """Generate a response using the agent"""
    # response = agent.print_response(prompt)
    response=  client.models.generate_content( 
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text

def lambda_handler(event, context):
    print("Received event:", json.dumps(event, indent=2))
    # Webhook verification (GET request)
    if "queryStringParameters" in event and "hub.mode" in event["queryStringParameters"]:
        return verify_webhook(event)

    # Handling incoming messages (POST request)
    body = json.loads(event["body"])
    if "entry" in body:
        for entry in body["entry"]:
            for change in entry["changes"]:
                if "messages" in change["value"]:
                    process_message(change["value"]["messages"][0])

    return {"statusCode": 200, "body": "Message Processed"}

def verify_webhook(event):
    """Verify the webhook"""
    params = event["queryStringParameters"]
    if params["hub.mode"] == "subscribe" and params["hub.verify_token"] == VERIFY_TOKEN:
        return {"statusCode": 200, "body": params["hub.challenge"]}
    return {"statusCode": 403, "body": "Verification failed"}

def process_message(message):
    """Process incoming WhatsApp message and send a static reply"""
    sender_id = message["from"]
    message_text = message["text"]["body"]
    reply_text = generate_agent_response(message_text)

    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"
    headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}", "Content-Type": "application/json"}
    data = {
        "messaging_product": "whatsapp",
        "to": sender_id,
        "text": {"body": reply_text}
    }
    
    response = requests.post(url, headers=headers, json=data)
    print(response.json())

