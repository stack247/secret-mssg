import datetime
import logging
import requests
import os
import azure.functions as func


def main(mytimer: func.TimerRequest, message) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    bot_token = os.environ['BotToken']
    #delete(bot_token, '', '')

# TODO: move to common class.
def delete(token: str, channel: str, ts: str):
  url = f'https://slack.com/api/chat.delete?token={token}&channel={channel}&ts={ts}'
  res = requests.get(url=url)