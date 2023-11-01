# Import dependencies
from nylas import Client
from dotenv import load_dotenv
import os
from nylas.models.messages import ListMessagesQueryParams

# Load our .env file
load_dotenv()

# Initialize Nylas client
nylas = Client(
    api_key = os.environ.get("V3_API_KEY")
)

# Create query parameters
query_params = ListMessagesQueryParams(
	{'in' : "inbox",
	'limit': 5}
)

# Read emails
messages, _, _ = nylas.messages.list(os.environ.get("GRANT_ID"), query_params)

# Print emails information
for message in messages:
    print(f"[{message.date}] {message.subject}")
