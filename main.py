from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage
import json

app = Flask(__name__)

# 初始化 LINE Bot API
line_bot_api = LineBotApi('你的 Channel Access Token')
handler = WebhookHandler('你的 Channel Secret')

@app.route("/", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    reply_token = json_data['events'][0]['replyToken']
    user_message = json_data['events'][0]['message']['text']

    # 回應訊息
    response_message = f"你說了：{user_message}"  # 可替換為 API 回應的結果
    line_bot_api.reply_message(reply_token, TextSendMessage(text=response_message))
    
    return 'OK'

if __name__ == "__main__":
    app.run()
