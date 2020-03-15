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
    '''
    posted_message b'token=432wf4w3f4wf&team_id=w4t3t34t34t&team_domain=g345g34tg&channel_id=srget4&channel_name=directmessage&user_id=324gf343g&user_name=wsr43f4&command=%2Fsecrets&text=fdsfds&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FT6F1027EH%2F1000622595557%2FwefverwgfdsgfdgG&trigger_id=234324234.324324234.32523534e8185421340aaba6b868b2e4c30'
    '''
    
    # TODO: Parse posted message

    # Post message
    res = post(bot_token, '', 'test message')
    '''
    res {"ok":true,"channel":"D0102A082CW","ts":"1584207296.001900","message":{"bot_id":"BV2KGBB0B","type":"message","text":"yopp","user":"U01004CQ5EH","ts":"1584207296.001900","team":"T6F1027EH","bot_profile":{"id":"BV2KGBB0B","deleted":false,"name":"TestApp","updated":1584151423,"app_id":"AVDKKESG4","icons":{"image_36":"https:\/\/a.slack-edge.com\/80588\/img\/plugins\/app\/bot_36.png","image_48":"https:\/\/a.slack-edge.com\/80588\/img\/plugins\/app\/bot_48.png","image_72":"https:\/\/a.slack-edge.com\/80588\/img\/plugins\/app\/service_72.png"},"team_id":"T6F1027EH"}}}
    '''

    # TODO: parse result

    # TODO: Store secret to delete
    #data = {
    #  'PartitionKey': '',
    #  'RowKey': '',
    #  'channel': '',
    #  'ts': '',
    #  'due': ''
    #}
    #message.set(json.dumps(data))
    
    return func.HttpResponse(status_code=200)

# TODO: move to common class.
def post(token: str, channel: str, message: str) -> str:
    url = f'https://slack.com/api/chat.postMessage?token={token}&channel={channel}&text={message}'
    res = requests.get(url=url)
    return res.text