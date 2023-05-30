#!/usr/bin/python
# -*- coding: utf-8 -*-

from flex import *
from image import *
from database import *
import pandas
import math


def authenticateUser():
    try:
        flex = selectTypeCar()
        return {'response':'OK', 'data':flex}
    except Exception as error:
        return {'response':'ER', 'data':None}
    
def promotion(amount, typeCar):
    try:
        newAmount = int(amount)
        if typeCar == 'รถแทรกเตอร์':
            if newAmount < 1000:
                yesData = 'ไม่มีข้อมูล'
                flex = yesData
                dataResponse = {
                    'msg':'ยังไม่ถึงเกณฑ์ที่จะได้รับโปรโมชัน',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
            elif newAmount >= 1000 and newAmount < 2000:
                yesData = 'ไม่มีข้อมูล'
                flex = yesData
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 10% ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
            elif newAmount >= 2000 and newAmount < 5000:
                yesData = 'โปรโมชันพิเศษรถแทรกเตอร์(1)'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 10% ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
            elif newAmount >= 5000:
                yesData = 'โปรโมชันพิเศษรถแทรกเตอร์(2)'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 15% ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
        elif typeCar == 'รถเกี่ยวนวดข้าวไม่รวมตีนตะขาบ':
            if newAmount < 5000:
                yesData = 'ไม่มีข้อมูล'
                flex = yesData
                dataResponse = {
                    'msg':'ยังไม่ถึงเกณฑ์ที่จะได้รับโปรโมชัน',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
            elif newAmount >= 5000:
                yesData = 'โปรโมชันพิเศษรถเกี่ยวข้าว'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 15% ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
        elif typeCar == 'รถขุด':
            if newAmount >= 3000 and newAmount < 5000:
                yesData = 'โปรโมชันพิเศษรถขุด'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ยังไม่ถึงเกณฑ์ที่จะได้รับโปรโมชัน',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
            elif newAmount >= 5000:
                yesData = 'ไม่มีข้อมูล'
                flex = yesData
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 15% ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
            else :
                yesData = 'ไม่มีข้อมูล'
                flex = yesData
                dataResponse = {
                    'msg':'ยังไม่ถึงเกณฑ์ที่จะได้รับโปรโมชัน',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
        elif typeCar == 'รถดำนาเดินตาม':
            if newAmount > 1 and newAmount < 10000:
                yesData = 'ไม่มีข้อมูล'
                flex = yesData
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 15% (ชุดส้อมหัวปักดำและยางลด 10%) ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
            elif newAmount >= 10000:
                yesData = 'โปรโมชันพิเศษรถดำนาเดินตาม'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 15% (ชุดส้อมหัวปักดำและยางลด 10%) ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
            else :
                yesData = 'ไม่มีข้อมูล'
                flex = yesData
                dataResponse = {
                    'msg':'ยังไม่ถึงเกณฑ์ที่จะได้รับโปรโมชัน',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
        elif typeCar == 'รถดำนานั่งขับ':
            if newAmount >= 1000 and newAmount < 5000:
                yesData = 'ไม่มีข้อมูล'
                flex = yesData
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 10% ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
            elif newAmount >= 5000 and newAmount < 10000:
                yesData = 'ไม่มีข้อมูล'
                flex = yesData
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 15% (ชุดส้อมหัวปักดำและยางลด 10%) ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
            elif newAmount >= 10000:
                yesData = 'โปรโมชันพิเศษรถดำนานั่งขับ'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 15% (ชุดส้อมหัวปักดำและยางลด 10%) ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
            else :
                yesData = 'ไม่มีข้อมูล'
                flex = yesData
                dataResponse = {
                    'msg':'ยังไม่ถึงเกณฑ์ที่จะได้รับโปรโมชัน',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg'], 'yes':dataResponse['flex']}
    except Exception as error:
        return {'response':'ER', 'data':None}
    
def promotionSpecial(param, vin):
    try:
        checkType = ''
        messageResponseER = ''
        connect = conn()
        cursor = connect.cursor(as_dict=True)
        cursor.execute("SELECT * FROM [Remaining_Promotion] WHERE [VIN] = %s", (vin))
        if param == 'โปรโมชันพิเศษรถแทรกเตอร์(1)':
            checkType = 'TRACTOR'
            messageResponseER = 'ไม่พบข้อมูล เนื่องจากไม่ใช่หมายเลขของรถแทรกเตอร์'
            text = 'ได้รับส่วนลดค่าแรงช่าง 200 บาท (2 สิทธิ์ ต่อ 1 หมายเลขรถ)'
        elif param == 'โปรโมชันพิเศษรถแทรกเตอร์(2)':
            checkType = 'TRACTOR'
            messageResponseER = 'ไม่พบข้อมูล เนื่องจากไม่ใช่หมายเลขของรถแทรกเตอร์'
            text = 'ได้รับส่วนลดค่าแรงช่าง 500 บาท (2 สิทธิ์ ต่อ 1 หมายเลขรถ)'
        elif param == 'โปรโมชันพิเศษรถเกี่ยวข้าว':
            checkType = 'COMBINE HARVESTER'
            messageResponseER = 'ไม่พบข้อมูล เนื่องจากไม่ใช่หมายเลขของรถเกี่ยวนวดข้าว'
            text = 'ได้รับส่วนลดค่าแรงช่าง 500 บาท (1 สิทธิ์ ต่อ 1 หมายเลขรถ)'
        elif param == 'โปรโมชันพิเศษรถขุด':
            checkType = 'MINI EXCAVATOR'
            messageResponseER = 'ไม่พบข้อมูล เนื่องจากไม่ใช่หมายเลขของรถขุด'
            text = 'ได้รับส่วนลดค่าอะไหล่ 10% (1 สิทธิ์ ต่อ 1 หมายเลขรถ)'
        elif param == 'โปรโมชันพิเศษรถดำนาเดินตาม':
            checkType = 'RICE TRANSPLANTER'
            messageResponseER = 'ไม่พบข้อมูล เนื่องจากไม่ใช่หมายเลขของรถดำนาเดินตาม'
            text = 'ได้รับส่วนลดค่าอะไหล่ 20% (ชุดส้อมหัวปักดำและยางลด 10% / 1 สิทธิ์ ต่อ 1 หมายเลขรถ)'
        elif param == 'โปรโมชันพิเศษรถดำนานั่งขับ':
            checkType = 'RICE TRANSPLANTER'
            messageResponseER = 'ไม่พบข้อมูล เนื่องจากไม่ใช่หมายเลขของรถดำนานั่งขับ'
            text = 'ได้รับส่วนลดค่าอะไหล่ 20% (ชุดส้อมหัวปักดำและยางลด 10% / 1 สิทธิ์ ต่อ 1 หมายเลขรถ)'
        
        dataPromotion = cursor.fetchone()
        connect.close()
        if dataPromotion == None :
            return {'response':'ER', 'data':[]}
        else :
            if checkType != dataPromotion['Product Type']:
                return {'response':'ER', 'data':messageResponseER}
            
            amountAll = str(dataPromotion['Maximum Limit'])
            amountUse = str(dataPromotion['จำนวนสิทธิ์ที่ใช้ไปแล้ว'])
            amountRemaining = int(amountAll) - int(amountUse)
            
            if amountRemaining == 0 :
                return {'response':'OK', 'data':0}
            else :
                flex = flexPromotionSpecial(text, amountAll, amountUse, str(amountRemaining), vin)
                return {'response':'OK', 'data':flex}
    except Exception as error:
        print(error)
        return {'response':'ER', 'data':None}
    
def checkEligibility(typeData) :
    try:
        flex = flecCheckEligibility(typeData)
        return {'response':'OK', 'data':flex}
    except Exception as error:
        print(error)
        return {'response':'ER', 'data':None}
    
def welcomeHome(vin) :
    try:
        connect = conn()
        cursor = connect.cursor(as_dict=True)
        cursor.execute("SELECT * FROM [Welcome_Home_Status_for_LineOA] WHERE [VIN] = %s", (vin))
        
        dataWelcome = cursor.fetchone()
        connect.close()
        
        if dataWelcome == None:
            return {'response':'OK', 'data':'ลูกค้าไม่มีสิทธิ์ Welcome Home'}
        else :
            status = 'ลูกค้า'+dataWelcome['Status']
            return {'response':'OK', 'data':status}
    except Exception as error:
        print(error)
        return {'response':'ER', 'data':None} 
    
def limitParts(vin) :
    try:
        connect = conn()
        cursor = connect.cursor(as_dict=True)
        cursor.execute("SELECT * FROM [Remaining_Parts] WHERE [VIN] = %s", (vin))
        
        dataLimit = cursor.fetchall()
        connect.close()
        
        if dataLimit == []:
            return {'response':'OK', 'list1':[], 'list2':[]}
        else :
            listData1 = []
            listData2 = []
            countDataLimit = len(dataLimit)
            for i in dataLimit :
                imageURL = getImageURL(i['Material Group'])
                flex = flexLimitParts(i, imageURL)
                if countDataLimit > 5 :
                    if len(listData1) < 5 :
                        listData1.append(flex)
                    else :
                        listData2.append(flex)
                else :
                    listData1.append(flex)

            return {'response':'OK', 'list1':listData1, 'list2':listData2}
    except Exception as error:
        print(error)
        return {'response':'ER', 'data':None} 