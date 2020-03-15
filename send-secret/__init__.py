import logging
import os
import requests
import json
import azure.functions as func


def main(req: func.HttpRequest, message: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    bot_token = os.environ['BotToken']

    # Get posted message.
    posted_message = req.get_body().decode('utf-8')
    print('-=====- posted_message', posted_message)
    
    # TODO: Parse posted message

    # Post message
    res = post(bot_token, '', 'test message')

    # TODO: parse result

    # TODO: Store secret to delete
    #data = {
    #  'PartitionKey': '',
    #  'RowKey': '',
    #  'channel': '',
    #  'ts': ''
    #}
    #message.set(json.dumps(data))
    
    return func.HttpResponse(status_code=200)

# TODO: move to common class.
def post(token: str, channel: str, message: str) -> str:
    url = f'https://slack.com/api/chat.postMessage?token={token}&channel={channel}&text={message}'
    res = requests.get(url=url)
    return res.text