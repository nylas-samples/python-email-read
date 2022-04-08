# python-email-read

This sample will show you to easily read your email with the Nylas Python SDK.

You can follow along step-by-step in our blog post ["How to Read Emails with the Nylas Python SDK"](https://www.nylas.com/blog/how-to-read-email-inbox-data-with-nylas-python-sdk/).

## Setup

### System dependencies

- Python v3.x

### Gather environment variables

You'll need the following values:

```text
ACCESS_TOKEN = ""
CLIENT_ID = ""
CLIENT_SECRET = ""
RECIPIENT_ADDRESS = ""
```

Add the above values to a new `.env` file:

```bash
$ touch .env # Then add your env variables
```

### Install dependencies

```bash
$ pip3 install nylas
```

## Usage

Run the script using the `python3` command:

```bash
$ python3 SendEmail.py
```

When your message is successfully sent, you'll get the following output in your terminal:

```text
[4/7/YYYY] Here's an email subject
[4/6/YYYY] Another subject
```

## Learn more

Visit our [Nylas Python SDK documentation](https://developer.nylas.com/docs/developer-tools/sdk/python-sdk/) to learn more.
