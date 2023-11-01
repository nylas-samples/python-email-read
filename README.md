# python-email-read

This sample will show you to easily read your email with the Nylas Python SDK.

## Setup

### System dependencies

- Python v3.x

### Gather environment variables

You'll need the following values:

```text
V3_TOKEN =
GRANT_ID =
V3_HOST = 
```

Add the above values to a new `.env` file:

```bash
$ touch .env # Then add your env variables
```

### Install dependencies

```bash
$ pip3 install nylas
$ pip3 install dotenv
```

## Usage

Run the script using the `ruby` command:

```bash
$ python3 ReadEmails.py
```

You will get a list of your emails in the following format

```text
[2023-11-22] It's Blag's birthday!
```

## Learn more

Visit our [Nylas Python SDK documentation](https://developer.nylas.com/docs/developer-tools/sdk/python-sdk/) to learn more.
