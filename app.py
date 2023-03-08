import flask
from flask import Flask ,session, render_template, request, redirect, url_for, send_from_directory
from flask import request
from flask import jsonify
import os
from webhookLine import action
from service import line
from config import token

app = Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/api/v1/appLine', methods=['POST'])
def appLine():
    try:
        json = request.json
        tokenLine = token.tokenLineBot()
        eventsLine = json['events'][0]
        replyToken = eventsLine['replyToken']
        userId = eventsLine['source']['userId']
        typeEvents = eventsLine['type']
        
        if typeEvents == 'message' :
            if eventsLine['message']['type'] == "text" :
                if eventsLine['message']['text'] == "ต้องการสอบถามโปรโมชันของสินค้าใดครับ ?" :
                    response = action.authenticateUser()
                    if response['response'] == 'OK' :
                        line.sendReplyFlexMessageLine(tokenLine, replyToken, response['data'])
                    else :
                        line.sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
                elif eventsLine['message']['text'] == "a" :
                    line.sendReplyMessageTextLine(tokenLine, replyToken, "abc")
                else :
                    if eventsLine['message']['text'].find("กรุณาระบุมูลค่าอะไหล่ก่อนหักส่วนลด") != -1 :
                        listStr = eventsLine['message']['text'].split()
                        if listStr[0] == "รถแทรกเตอร์" :
                            newStr = listStr[3]
                            response = action.promotion(newStr, listStr[0])
                            if response['response'] == 'OK' :
                                line.sendReplyStickerMessageAllMsgLine(tokenLine, replyToken, response['data'], '11537', '52002736')
                            else :
                                line.sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
                        elif listStr[0] == "รถเกี่ยวนวดข้าวไม่รวมตีนตะขาบ" :
                            newStr = listStr[3]
                            response = action.promotion(newStr, listStr[0])
                            if response['response'] == 'OK' :
                                line.sendReplyStickerMessageAllMsgLine(tokenLine, replyToken, response['data'], '11537', '52002736')
                            else :
                                line.sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
                        elif listStr[0] == "รถขุด" :
                            newStr = listStr[3]
                            response = action.promotion(newStr, listStr[0])
                            if response['response'] == 'OK' :
                                line.sendReplyStickerMessageAllMsgLine(tokenLine, replyToken, response['data'], '11537', '52002736')
                            else :
                                line.sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
                        elif listStr[0] == "รถดำนาเดินตาม" :
                            newStr = listStr[3]
                            response = action.promotion(newStr, listStr[0])
                            if response['response'] == 'OK' :
                                line.sendReplyStickerMessageAllMsgLine(tokenLine, replyToken, response['data'], '11537', '52002736')
                            else :
                                line.sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
                        elif listStr[0] == "รถดำนานั่งขับ" :
                            newStr = listStr[3]
                            response = action.promotion(newStr, listStr[0])
                            if response['response'] == 'OK' :
                                line.sendReplyStickerMessageAllMsgLine(tokenLine, replyToken, response['data'], '11537', '52002736')
                            else :
                                line.sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
                        else :
                            line.sendReplyMessageTextLine(tokenLine, replyToken, "โปรดเลือกจาก rich menu")
                    else :
                        line.sendReplyMessageTextLine(tokenLine, replyToken, "โปรดเลือกจาก rich menu")
            else :
                line.sendReplyMessageTextLine(tokenLine, replyToken, "โปรดเลือกจาก rich menu")
        elif typeEvents == 'postback' :
            if eventsLine['postback']['data'] == "test" :
                line.sendReplyMessageTextLine(tokenLine, replyToken, "กรุณาระบุมูลค่าอะไหล่ก่อนหักส่วนลดของงานบริการนี้ด้วยครับ (ใส่เฉพาะตัวเลขเท่านั้น)")
            elif eventsLine['postback']['data'] == "ไม่มีข้อมูล" :
                line.sendReplyMessageTextLine(tokenLine, replyToken, "ไม่พบข้อมูลโปรโมชันพิเศษ")
            elif eventsLine['postback']['data'] == "ไม่ใช่" :
                line.sendReplyMessageTextLine(tokenLine, replyToken, "ขอบคุณครับ")
            elif eventsLine['postback']['data'] == "แทรกเตอร์01" :
                response = action.promotionSpecial(eventsLine['postback']['data'])
                if response['response'] == 'OK' :
                    line.sendReplyMessageTextLine(tokenLine, replyToken, response['data'])
                else :
                    line.sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
            elif eventsLine['postback']['data'] == "แทรกเตอร์02" :
                response = action.promotionSpecial(eventsLine['postback']['data'])
                if response['response'] == 'OK' :
                    line.sendReplyMessageTextLine(tokenLine, replyToken, response['data'])
                else :
                    line.sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
            elif eventsLine['postback']['data'] == "เกี่ยวข้าว01" :
                response = action.promotionSpecial(eventsLine['postback']['data'])
                if response['response'] == 'OK' :
                    line.sendReplyMessageTextLine(tokenLine, replyToken, response['data'])
                else :
                    line.sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
            elif eventsLine['postback']['data'] == "ขุด01" :
                response = action.promotionSpecial(eventsLine['postback']['data'])
                if response['response'] == 'OK' :
                    line.sendReplyMessageTextLine(tokenLine, replyToken, response['data'])
                else :
                    line.sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
            elif eventsLine['postback']['data'] == "ดำนาเดินตาม01" :
                response = action.promotionSpecial(eventsLine['postback']['data'])
                if response['response'] == 'OK' :
                    line.sendReplyMessageTextLine(tokenLine, replyToken, response['data'])
                else :
                    line.sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
            elif eventsLine['postback']['data'] == "ดำนานั่งขับ01" :
                response = action.promotionSpecial(eventsLine['postback']['data'])
                if response['response'] == 'OK' :
                    line.sendReplyMessageTextLine(tokenLine, replyToken, response['data'])
                else :
                    line.sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
            else :
                line.sendReplyMessageTextLine(tokenLine, replyToken, "โปรดเลือกจาก rich menu")
        else :
            line.sendReplyMessageTextLine(tokenLine, replyToken, "โปรดเลือกจาก rich menu")
        return jsonify({ 'response':'OK'})
    except Exception as error:
        return jsonify({'response':'ER'})

if __name__ == "__main__":
    app.run()