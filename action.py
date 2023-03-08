from flex import *

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
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ยังไม่ถึงเกณฑ์ที่จะได้รับโปรโมชัน',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
            elif newAmount >= 1000 and newAmount < 2000:
                yesData = 'ไม่มีข้อมูล'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 10% ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
            elif newAmount >= 2000 and newAmount < 5000:
                yesData = 'แทรกเตอร์01'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 10% ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
            elif newAmount >= 5000:
                yesData = 'แทรกเตอร์02'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 15% ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
        elif typeCar == 'รถเกี่ยวนวดข้าวไม่รวมตีนตะขาบ':
            if newAmount < 5000:
                yesData = 'ไม่มีข้อมูล'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ยังไม่ถึงเกณฑ์ที่จะได้รับโปรโมชัน',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
            elif newAmount >= 5000:
                yesData = 'เกี่ยวข้าว01'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 15% ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
        elif typeCar == 'รถขุด':
            if newAmount >= 3000 and newAmount < 5000:
                yesData = 'ขุด01'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ยังไม่ถึงเกณฑ์ที่จะได้รับโปรโมชัน',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
            elif newAmount >= 5000:
                yesData = 'ไม่มีข้อมูล'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 15% ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
            else :
                yesData = 'ไม่มีข้อมูล'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ยังไม่ถึงเกณฑ์ที่จะได้รับโปรโมชัน',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
        elif typeCar == 'รถดำนาเดินตาม':
            if newAmount > 1 and newAmount < 10000:
                yesData = 'ไม่มีข้อมูล'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 15% (ชุดส้อมหัวปักดำและยางลด 10%) ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
            elif newAmount >= 10000:
                yesData = 'ดำนาเดินตาม01'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 15% (ชุดส้อมหัวปักดำและยางลด 10%) ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
            else :
                yesData = 'ไม่มีข้อมูล'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ยังไม่ถึงเกณฑ์ที่จะได้รับโปรโมชัน',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
        elif typeCar == 'รถดำนานั่งขับ':
            if newAmount >= 1000 and newAmount < 5000:
                yesData = 'ไม่มีข้อมูล'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 10% ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
            elif newAmount >= 5000 and newAmount < 10000:
                yesData = 'ไม่มีข้อมูล'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 15% (ชุดส้อมหัวปักดำและยางลด 10%) ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
            elif newAmount >= 10000:
                yesData = 'ดำนานั่งขับ01'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ลูกค้าได้รับส่วนลดอะไหล่ 15% (ชุดส้อมหัวปักดำและยางลด 10%) ครับ',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
            else :
                yesData = 'ไม่มีข้อมูล'
                flex = promotionFlex(yesData)
                dataResponse = {
                    'msg':'ยังไม่ถึงเกณฑ์ที่จะได้รับโปรโมชัน',
                    'flex':flex
                }
                return {'response':'OK', 'data':dataResponse['msg']}
    except Exception as error:
        return {'response':'ER', 'data':None}
    
def promotionSpecial(param):
    try:
        if param == 'แทรกเตอร์01':
            return {'response':'OK', 'data':'ได้รับส่วนลดค่าแรงช่าง 200 บาท \n(2 สิทธิ์ ต่อ 1 หมายเลขรถ)'}
        elif param == 'แทรกเตอร์02':
            return {'response':'OK', 'data':'ได้รับส่วนลดค่าแรงช่าง 500 บาท \n(2 สิทธิ์ ต่อ 1 หมายเลขรถ)'}
        elif param == 'เกี่ยวข้าว01':
            return {'response':'OK', 'data':'ได้รับส่วนลดค่าแรงช่าง 500 บาท \n(1 สิทธิ์ ต่อ 1 หมายเลขรถ)'}
        elif param == 'ขุด01':
            return {'response':'OK', 'data':'ได้รับส่วนลดค่าอะไหล่ 10% \n(1 สิทธิ์ ต่อ 1 หมายเลขรถ)'}
        elif param == 'ดำนาเดินตาม01':
            return {'response':'OK', 'data':'ได้รับส่วนลดค่าอะไหล่ 20% \n(ชุดส้อมหัวปักดำและยางลด 10% / 1 สิทธิ์ ต่อ 1 หมายเลขรถ)'}
        elif param == 'ดำนานั่งขับ01':
            return {'response':'OK', 'data':'ได้รับส่วนลดค่าอะไหล่ 20% \n(ชุดส้อมหัวปักดำและยางลด 10% / 1 สิทธิ์ ต่อ 1 หมายเลขรถ)'}
    except Exception as error:
        return {'response':'ER', 'data':None}