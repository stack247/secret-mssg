import datetime
import logging
import requests
import os
import json
import azure.functions as func


def main(mytimer: func.TimerRequest, messages) -> None:
    # TODO: Get deletion list from Azure table.
    all_messages = json.loads(messages)
    
    #print('-=====- all_messages', all_messages)
    '''
    all_messages [{'channel': '', 'ts': '', 'PartitionKey': '', 'RowKey': ''}]
    '''

    # TODO: Filter due list.


    # TODO: Delete the message
    bot_token = os.environ['BotToken']
    for m in all_messages:
      try:
        delete(bot_token, m['channel'], m['ts'])
      except:
        pass
    
    #res = delete(bot_token, '', '')
    #print('-====- res', res)
    '''
    res {"ok":true,"channel":"D0102A082CW","ts":"1584207057.001700"}
    '''

    # TODO: Delete message in table.

# TODO: move to common class.
def delete(token: str, channel: str, ts: str):
  url = f'https://slack.com/api/chat.delete?token={token}&channel={channel}&ts={ts}'
  res = requests.get(url=url)
  return res.text