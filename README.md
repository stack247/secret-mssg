# secret-mssg
Slack Bot to send self-destruct message.

## TODO
* Azure deploy button
* Slack bot setup
* Usage example
* Requirements
  * Python 3.6.6
  * Function core tool (running local)
    * https://github.com/Azure/azure-functions-core-tools
* Local dev
  * `py -m venv ./venv`
  * `./venv/Scripts/Activate`
  * `pip install -r requirements.txt`
  * `.venv/Scripts/activate`
  * `func host start`
  * `ngrok http 7071 --host-header="localhost:7071"`
  * `http://localhost:7071/api/send-secret`
