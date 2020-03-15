import logging
import os
import requests
import azure.functions as func


def main(req: func.HttpRequest, message: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    bot_token = os.environ['BotToken']

    post(bot_token, '', '')

    data = {
      'PartitionKey': '',
      'RowKey': '',
      'channel': '',
      'ts': ''
    }
    message.set(json.dumps(data))
    
    return func.HttpResponse(status_code=200)

# TODO: move to common class.
def post(token: str, channel: str, message: str):
    url = f'https://slack.com/api/chat.postMessage?token={token}&channel={channel}&text={message}'
    res = requests.get(url=url)
    