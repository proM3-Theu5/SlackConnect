from distutils.command.config import config
import os
import json
import requests
from urllib.parse import urlparse
import socket


class SlackConnect:

    config_path = '/configuration/config.js'
    config_status = False
    config_load = False
    configuration = []
    current_config = {}

    def set_configuration_path(self, configPath = ''):
        '''
        Set Configuration Path for the object
        '''
        if configPath != '':
            self.config_path = configPath
        else:
            self.config_path = self.config_path

    def check_config(self):
        '''
        Checking the configuration file
        '''
        try:
            with open(os.getcwd() + self.config_path, 'r') as file:
                content = file.read()
            print('Configuration file Found!')

            # Check if the file is not empty
            if not content.strip():
                print("Configuration file empty.")
                self.configuration_setup = []
                self.config_status = False

            try:
                json_data = json.loads(content)
                print("File content is in correct JSON format.")
                self.configuration_setup = json_data
                self.config_status = True

            except json.JSONDecodeError as e:
                print("Error: Invalid Configuration JSON format.")
                self.configuration_setup = []
                self.config_status = False

        except FileNotFoundError:
            print("Error: Configuration File not found.")
            self.configuration_setup = []
            self.config_status = False
    
    def get_configuration(self):

        if self.config_status:
            with open(os.getcwd() + self.config_path, 'r') as file:
                content = file.read()
                json_data = json.loads(content)
                self.configuration = json_data
                self.config_load = True
            print('Configuration loading completed!')
        else:
            print('No configuration found!')
            print('Configuration Load Error!')
            self.config_load = False

    def list_configurations(self):

        config_values = self.configuration
        config_string = '''
        Channel : {channel_name}
        App Name : {app_name}
        WebHook URL : {url_status}
        '''
        for value in config_values:
            webhook_url = value['webhook_url']
            parsed_url = urlparse(webhook_url)
            webhook_url_status = all([parsed_url.scheme, parsed_url.netloc])
            print(config_string.format(channel_name = value['channel_name']
                                            ,app_name = value['app_name']
                                            ,url_status = webhook_url_status))

    def initialize_current_config(self):

        self.current_config = self.configuration[0]

    def select_configuration(self, channel_name, app_name = 'none'):

        config_values = self.configuration
        config_set = False
        for value in config_values:
            if value['channel_name'] == channel_name and value['app_name'] == app_name:
                self.current_config = value
                config_set = True 

        if config_set == False:
            print('Configuration setup Failed!')
    
    def __init__(self):

        self.set_configuration_path()
        self.check_config()
        self.get_configuration()

    @classmethod
    def is_webhook_url_active(cls,url):
        url_parts = url.split("://")[1].split("/", 1)
        host = url_parts[0]
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Set a timeout for the connection attempt (in seconds)
            s.settimeout(3)

            # Connect to the server (without sending any data)
            s.connect((host, 80))

            # Close the socket
            s.close()

            return True  # The URL is active and reachable
        except (socket.timeout, socket.error):
            return False  # The URL is not reachable or not active

    def check_webhook_url(self):

        webhook_config = self.current_config
        webhook_url = webhook_config['webhook_url']
        print('Webhook Active : ',self.is_webhook_url_active(webhook_url) )
        return True
    
    def send_message(self, message_string):

        payload = '{{"text":"{message_value}"}}'.format(message_value = message_string)

        if self.check_webhook_url():
            try:
                print(self.current_config['webhook_url'])
                print(payload)
                response = requests.post(
                                            self.current_config['webhook_url'],
                                            data = payload
                                        )
                print(response)
                print('Message Sending completed!')
            except:
                print('Message Sending failed!')
        else:
            print('Webhook Inactive!')

