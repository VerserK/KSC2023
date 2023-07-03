from flask import Flask, abort, session, render_template, request, redirect, url_for, send_from_directory, jsonify
from flask_cors import CORS, cross_origin
import os
from action import *
from line import *
from tokenLine import *
from image import *
# from database import *

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

DOMAIN = "https://ksc2023.azurewebsites.net/api/v1/appLine"
   

@app.route('/api/v1/appLine', methods=['POST'])
@cross_origin()
def appLine():
    try:
        req = request.json
        tokenLine = tokenLineBot()
        eventsLine = req['events'][0]
        replyToken = eventsLine['replyToken']
        userId = eventsLine['source']['userId']
        typeEvents = eventsLine['type']
        
        if typeEvents == 'message' :
            if eventsLine['message']['type'] == "text" :
                if eventsLine['message']['text'] == "ต้องการสอบถามโปรโมชันของสินค้าใดครับ ?" :
                    response = authenticateUser()
                    if response['response'] == 'OK' :
                        sendReplyFlexMessageLine(tokenLine, replyToken, response['data'], 'เลือกประเภท')
                    else :
                        sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
                elif eventsLine['message']['text'] == "a" :
                    sendReplyMessageTextLine(tokenLine, replyToken, "abc")
                elif  eventsLine['message']['text'] == "ตรวจสอบสิทธิ์ Welcome Home" :
                    response = checkEligibility("Welcome Home")
                    if response['response'] == 'OK' :
                        sendReplyFlexMessageLine(tokenLine, replyToken, response['data'], 'ตรวจสอบสิทธิ์ Welcome Home')
                    else :
                        sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
                elif  eventsLine['message']['text'] == "ตรวจสอบสิทธิ์ Limit Parts" :
                    response = checkEligibility("Limit Parts")
                    if response['response'] == 'OK' :
                        sendReplyFlexMessageLine(tokenLine, replyToken, response['data'], 'ตรวจสอบสิทธิ์ Limit Parts')
                    else :
                        sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
                else :
                    if eventsLine['message']['text'].find("กรุณาระบุมูลค่าอะไหล่ก่อนหักส่วนลด") != -1 :
                        listStr = eventsLine['message']['text'].split()
                        if listStr[0] == "รถแทรกเตอร์" :
                            newStr = listStr[3]
                            response = promotion(newStr, listStr[0])
                            if response['response'] == 'OK' :
                                sendReplyStickerMessageAllMsgLine(tokenLine, replyToken, response['data'], response['packageId'], response['stickerId'], response['yes'])
                            else :
                                sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
                        elif listStr[0] == "รถเกี่ยวนวดข้าวไม่รวมตีนตะขาบ" :
                            newStr = listStr[3]
                            response = promotion(newStr, listStr[0])
                            if response['response'] == 'OK' :
                                sendReplyStickerMessageAllMsgLine(tokenLine, replyToken, response['data'], response['packageId'], response['stickerId'], response['yes'])
                            else :
                                sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
                        elif listStr[0] == "รถขุด" :
                            newStr = listStr[3]
                            response = promotion(newStr, listStr[0])
                            if response['response'] == 'OK' :
                                sendReplyStickerMessageAllMsgLine(tokenLine, replyToken, response['data'], response['packageId'], response['stickerId'], response['yes'])
                            else :
                                sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
                        elif listStr[0] == "รถดำนาเดินตาม" :
                            newStr = listStr[3]
                            response = promotion(newStr, listStr[0])
                            if response['response'] == 'OK' :
                                sendReplyStickerMessageAllMsgLine(tokenLine, replyToken, response['data'], response['packageId'], response['stickerId'], response['yes'])
                            else :
                                sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
                        elif listStr[0] == "รถดำนานั่งขับ" :
                            newStr = listStr[3]
                            response = promotion(newStr, listStr[0])
                            if response['response'] == 'OK' :
                                sendReplyStickerMessageAllMsgLine(tokenLine, replyToken, response['data'], response['packageId'], response['stickerId'], response['yes'])
                            else :
                                sendReplyMessageTextLine(tokenLine, replyToken, "ไม่สำเร็จ")
                        else :
                            sendReplyMessageTextLine(tokenLine, replyToken, "โปรดเลือกจาก rich menu")
                    elif eventsLine['message']['text'].find("สอบถามสิทธิ์คงเหลือของ") != -1 :
                        listStr = eventsLine['message']['text'].split()
                        if listStr[1] in ['โปรโมชันพิเศษรถแทรกเตอร์(1)', 'โปรโมชันพิเศษรถแทรกเตอร์(2)', 'โปรโมชันพิเศษรถเกี่ยวข้าว', 'โปรโมชันพิเศษรถขุด', 'โปรโมชันพิเศษรถดำนาเดินตาม', 'โปรโมชันพิเศษรถดำนานั่งขับ'] :
                            newStr = listStr[4]
                            response = promotionSpecial(listStr[1], newStr)
                            if response['response'] == 'OK' :
                                if response['data'] == 0 :
                                    sendReplyMessageTextLine(tokenLine, replyToken, "หมายเลขรถนี้รับสิทธิ์ครบจำนวนที่กำหนดแล้ว")
                                else :
                                    sendReplyFlexMessageLine(tokenLine, replyToken, response['data'], 'โปรโมชันพิเศษ')
                            else :
                                if response['data'] != [] :
                                    sendReplyMessageTextLine(tokenLine, replyToken, response['data'])
                                else :
                                    sendReplyMessageTextLine(tokenLine, replyToken, "ไม่พบโปรโมชันพิเศษ")
                    elif eventsLine['message']['text'].find("กรุณาระบุหมายเลขรถเพื่อตรวจสอบสิทธิ์") != -1 :
                        listStr = eventsLine['message']['text'].split()
                        if listStr[1] == 'Welcome' :
                            response = welcomeHome(listStr[4])
                            if response['response'] == 'OK' :
                                sendReplyMessageTextLine(tokenLine, replyToken, response['data'])
                            else :
                                sendReplyMessageTextLine(tokenLine, replyToken, "เกิดข้อผิดพลาด")
                        else :
                            response = limitParts(listStr[4])
                            if response['response'] == 'OK' :
                                if response['list1'] == [] :
                                    sendReplyImageMessageAllMsgLine(tokenLine, replyToken, "รถคันนี้ยังไม่ได้ใช้อะไหล่ในช่วงที่จำกัดเวลา และมีอะไหล่คงเหลือตามตารางนี้ครับ", imageLimitPart())
                                else :
                                    sendReplyFlexListMessageLine(tokenLine, replyToken, response['list1'], response['list2'], 'Limit Parts')
                            else :
                                sendReplyMessageTextLine(tokenLine, replyToken, "เกิดข้อผิดพลาด")
                    else :
                        sendReplyMessageTextLine(tokenLine, replyToken, "โปรดเลือกจาก rich menu")
            else :
                sendReplyMessageTextLine(tokenLine, replyToken, "โปรดเลือกจาก rich menu")
        elif typeEvents == 'postback' :
            if eventsLine['postback']['data'] == "test" :
                sendReplyMessageTextLine(tokenLine, replyToken, "กรุณาระบุมูลค่าอะไหล่ก่อนหักส่วนลดของงานบริการนี้ด้วยครับ (ใส่เฉพาะตัวเลขเท่านั้น)")
            elif eventsLine['postback']['data'] == "ไม่มีข้อมูล" :
                sendReplyMessageTextLine(tokenLine, replyToken, "ไม่พบข้อมูลโปรโมชันพิเศษ")
            elif eventsLine['postback']['data'] == "ไม่ใช่" :
                sendReplyMessageTextLine(tokenLine, replyToken, "ขอบคุณครับ")
            elif eventsLine['postback']['data'] == "มีข้อมูล" :
                sendReplyMessageTextLine(tokenLine, replyToken, "กรุณาระบุหมายเลขรถของคุณเพื่อสอบถามโปรโมชันพิเศษ")
            elif eventsLine['postback']['data'] == "เช็คสิทธิ์" :
                sendReplyMessageTextLine(tokenLine, replyToken, "กรุณาระบุหมายเลขรถของคุณเพื่อตรวจสอบสิทธิ์")
            elif eventsLine['postback']['data'].find("โปรโมชันพิเศษ") != -1 :
                listStr = eventsLine['postback']['data'].split('.')
                model = str(listStr[1])
                fileName = checkImage(model)
                if fileName == 'not':
                    sendReplyMessageTextLine(tokenLine, replyToken, "ขออภัยครับ ในไตรมาสนี้ไม่มีโปรโมชันพิเศษของรถดำนาครับ")
                else :
                    pathImage = DOMAIN+'/image/'+fileName
                    sendReplyImageMessageAllMsgLine(tokenLine, replyToken, "โปรโมชันพิเศษประจำไตรมาสนี้", pathImage)
            else :
                sendReplyMessageTextLine(tokenLine, replyToken, "โปรดเลือกจาก rich menu")
        else :
            sendReplyMessageTextLine(tokenLine, replyToken, "โปรดเลือกจาก rich menu")
        return jsonify({ 'response':'OK'})
    except Exception as error:
        return jsonify({'response':'ER'})
    
@app.route('/image/<path:fileName>')
def openImage(fileName):
    return send_from_directory(os.path.join(app.root_path, 'image'), fileName+'.png')

if __name__ == "__main__":
    app.run()