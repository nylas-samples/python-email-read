# Load your env variables
from dotenv import load_dotenv
load_dotenv()

# Import your dependencies
import os
from nylas import APIClient
import datetime

# Initialize your Nylas API client
nylas = APIClient(
    os.environ.get("CLIENT_ID"),
    os.environ.get("CLIENT_SECRET"),
    os.environ.get("ACCESS_TOKEN"),
)

# Get the first five emails
messages = nylas.messages.where(limit=5)
# Read each email
for message in messages:
# Change time to a readable format
	date = datetime.datetime.fromtimestamp(message.date)
# Print date and subject of email
	print("[{}] {}".format(date, message.subject))
