# :rocket: SlackConnect - Python Class for Sending Messages on Slack using Webhooks

<!-- ![SlackConnect](https://yourdomain.com/path/to/slackconnect_logo.png) -->

SlackConnect is a powerful Python class that allows you to interact with Slack webhooks effortlessly and send messages to your desired channels. :speech_balloon: With SlackConnect, you can easily integrate Slack messaging capabilities into your Python projects, making communication and notifications a breeze.

## :star2: Features

- Easy-to-use Python class for interacting with Slack webhooks.
- Configure multiple Slack channels and apps using a simple JSON-based configuration file.
- Check the status of the configured webhooks and verify their reachability.
- Send text messages to Slack channels with just one function call.

## :wave: Introduction

SlackConnect is a versatile Python class designed to make sending messages to Slack channels via webhooks incredibly simple. Whether you want to notify your team about the status of a task, send automated updates, or simply have fun with Slack messaging, SlackConnect has got you covered. :tada:

## :rocket: Getting Started
### :computer: Installation

To use SlackConnect in your Python project, follow these steps:

1. Clone the SlackConnect repository to your local machine.

```bash
git clone https://github.com/yourusername/SlackConnect.git
cd SlackConnect
```

2. Import the SlackConnect class into your Python code.

```python
from slackconnect import SlackConnect
```

### :gear: Configuration
Before using SlackConnect, you need to set up your Slack configurations in the config.js file. The configuration file uses JSON format to define your Slack channels, app names, and webhook URLs.

The default configuration path is /configuration/config.js, but you can specify a custom configuration path if needed.

```json
[
    {
        "channel_name": "general",
        "app_name": "MyApp",
        "webhook_url": "https://hooks.slack.com/services/your/webhook/url"
    },
    {
        "channel_name": "random",
        "app_name": "None",
        "webhook_url": "https://hooks.slack.com/services/your/other/webhook/url"
    }
]
```

## :hammer_and_wrench: Usage
### :bulb: Basic Usage

Initialize the SlackConnect object and load the configuration data:

```python
slack = SlackConnect()
```

### :file_folder: Configurations

List all the configurations available in your config.js file:

```python
slack = slack.list_configurations()
```

Select a specific configuration for sending messages:

```python
slack.select_configuration(channel_name="general", app_name="MyApp")
```

### :white_check_mark: Checking Webhook Status

You can check the status of the current webhook URL to ensure it is active and reachable:

```python
slack.check_webhook_url()
```

### :envelope: Sending Messages

Send a text message to the selected Slack channel:

```python
message = "Hello, Slack world!"
slack.send_message(message)
```