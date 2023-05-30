def test():
    data = {
            "type": "bubble",
            "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip7.jpg",
                    "size": "5xl",
                    "aspectMode": "cover",
                    "aspectRatio": "150:196",
                    "gravity": "center",
                    "flex": 1
                    },
                    {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                        "type": "image",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip8.jpg",
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "150:98",
                        "gravity": "center"
                        },
                        {
                        "type": "image",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip9.jpg",
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "150:98",
                        "gravity": "center"
                        }
                    ],
                    "flex": 1
                    }
                ]
                },
                {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                        "type": "image",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip13.jpg",
                        "aspectMode": "cover",
                        "size": "full"
                        }
                    ],
                    "cornerRadius": "100px",
                    "width": "72px",
                    "height": "72px"
                    },
                    {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                        "type": "text",
                        "contents": [
                            {
                            "type": "span",
                            "text": "brown_05",
                            "weight": "bold",
                            "color": "#000000"
                            },
                            {
                            "type": "span",
                            "text": "     "
                            },
                            {
                            "type": "span",
                            "text": "I went to the Brown&Cony cafe in Tokyo and took a picture"
                            }
                        ],
                        "size": "sm",
                        "wrap": True
                        },
                        {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                            "type": "text",
                            "text": "1,140,753 Like",
                            "size": "sm",
                            "color": "#bcbcbc"
                            }
                        ],
                        "spacing": "sm",
                        "margin": "md"
                        }
                    ]
                    }
                ],
                "spacing": "xl",
                "paddingAll": "20px"
                }
            ],
            "paddingAll": "0px"
            },
            "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "button",
                "action": {
                    "type": "postback",
                    "label": "รถแทรกเตอร์",
                    "data": "test",
                    "displayText": "รถแทรกเตอร์",
                    "inputOption": "openKeyboard",
                    "fillInText": "รถแทรกเตอร์ : "
                },
                "style": "primary"
                }
            ]
            }
        }
    return data

def selectTypeCar():
    data = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://sv1.picz.in.th/images/2023/02/19/LpJTIk.png",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
            "type": "uri",
            "uri": "http://linecorp.com/"
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "โปรดเลือกสินค้าที่ต้องการ",
                "size": "lg",
                "weight": "bold"
            },
            {
                "type": "text",
                "text": "สอบถามโปรโมชันได้เลยครับ",
                "color": "#aaaaaa",
                "size": "sm",
                "margin": "sm"
            },
            {
                "type": "separator",
                "margin": "xxl"
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "postback",
                    "label": "รถแทรกเตอร์",
                    "data": "test",
                    "displayText": "รถแทรกเตอร์",
                    "inputOption": "openKeyboard",
                    "fillInText": "รถแทรกเตอร์ กรุณาระบุมูลค่าอะไหล่ก่อนหักส่วนลด : "
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "postback",
                    "label": "รถเกี่ยวนวดข้าว",
                    "data": "test",
                    "displayText": "รถเกี่ยวนวดข้าว",
                    "inputOption": "openKeyboard",
                    "fillInText": "รถเกี่ยวนวดข้าวไม่รวมตีนตะขาบ กรุณาระบุมูลค่าอะไหล่ก่อนหักส่วนลด : "
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "postback",
                    "label": "รถขุด",
                    "data": "test",
                    "displayText": "รถขุด",
                    "inputOption": "openKeyboard",
                    "fillInText": "รถขุด กรุณาระบุมูลค่าอะไหล่ก่อนหักส่วนลด : "
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "postback",
                    "label": "รถดำนาเดินตาม",
                    "data": "test",
                    "displayText": "รถดำนาเดินตาม",
                    "inputOption": "openKeyboard",
                    "fillInText": "รถดำนาเดินตาม กรุณาระบุมูลค่าอะไหล่ก่อนหักส่วนลด : "
                    }
                },
                 {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "postback",
                    "label": "รถดำนานั่งขับ",
                    "data": "test",
                    "displayText": "รถดำนานั่งขับ",
                    "inputOption": "openKeyboard",
                    "fillInText": "รถดำนานั่งขับ กรุณาระบุมูลค่าอะไหล่ก่อนหักส่วนลด : "
                    }
                }
            ],
            "flex": 0
        }
    }
    return data

def promotionFlex(yesData):
    if yesData == 'ไม่มีข้อมูล' :
        data = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "ลูกค้ามีสิทธิ์รับโปรโมชันพิเศษ ต้องการสอบถามโปรโมชันพิเศษด้วยหรือไม่ครับ",
                    "wrap": True
                }
                ],
                "position": "relative"
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "postback",
                    "label": "ใช่",
                    "data": yesData,
                    "displayText": "โปรโมชันพิเศษ",
                    "inputOption": "openKeyboard"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "postback",
                    "label": "ไม่ใช่",
                    "data": "ไม่ใช่"
                    }
                }
                ],
                "flex": 0
            }
            }
    else :
        data = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "ลูกค้ามีสิทธิ์รับโปรโมชันพิเศษ ต้องการสอบถามโปรโมชันพิเศษด้วยหรือไม่ครับ",
                    "wrap": True
                }
                ],
                "position": "relative"
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "postback",
                    "label": "ใช่",
                    "data": "มีข้อมูล",
                    "displayText": "โปรโมชันพิเศษ",
                    "inputOption": "openKeyboard",
                    "fillInText": "สอบถามสิทธิ์คงเหลือของ "+yesData+" กรุณาระบุหมายเลขรถ : "
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "postback",
                    "label": "ไม่ใช่",
                    "data": "ไม่ใช่"
                    }
                }
                ],
                "flex": 0
            }
            }
    
    return data

def flexPromotionSpecial(textPromotion, amountAll, amountUse, amountRemaining, VIN) :
    return {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "โปรโมชันพิเศษ",
                "weight": "bold",
                "color": "#1DB446",
                "size": "xl"
            },
            {
                "type": "text",
                "text": textPromotion,
                "weight": "bold",
                "size": "lg",
                "margin": "md",
                "wrap": True
            },
            {
                "type": "separator",
                "margin": "xxl"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "สิทธิ์ทั้งหมด",
                        "size": "sm",
                        "color": "#555555",
                        "flex": 0,
                        "weight": "regular"
                    },
                    {
                        "type": "text",
                        "text": amountAll,
                        "size": "sm",
                        "color": "#111111",
                        "align": "end",
                        "weight": "bold"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "สิทธิ์ที่ใช้ไปแล้ว",
                        "size": "sm",
                        "color": "#555555",
                        "flex": 0,
                        "weight": "regular"
                    },
                    {
                        "type": "text",
                        "text": amountUse,
                        "size": "sm",
                        "color": "#111111",
                        "align": "end",
                        "weight": "bold"
                    }
                    ]
                },
                {
                    "type": "separator",
                    "margin": "xxl"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "xxl",
                    "contents": [
                    {
                        "type": "text",
                        "text": "สิทธิ์คงเหลือ",
                        "size": "sm",
                        "color": "#555555"
                    },
                    {
                        "type": "text",
                        "text": amountRemaining,
                        "size": "sm",
                        "color": "#111111",
                        "align": "end",
                        "weight": "bold"
                    }
                    ]
                }
                ]
            },
            {
                "type": "separator",
                "margin": "xxl"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "margin": "md",
                "contents": [
                {
                    "type": "text",
                    "text": "หมายเลขรถ",
                    "size": "xs",
                    "color": "#aaaaaa",
                    "flex": 0
                },
                {
                    "type": "text",
                    "text": VIN,
                    "color": "#aaaaaa",
                    "size": "xs",
                    "align": "end",
                    "wrap": True
                }
                ]
            }
            ]
        },
        "styles": {
            "footer": {
            "separator": True
            }
        }
}
    
def flecCheckEligibility(typeData) :
    return {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "ตรวจสอบสิทธิ์ "+typeData,
                        "wrap": True,
                        "weight": "bold",
                        "size": "md",
                        "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello"
                        }
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "action": {
                            "type": "postback",
                            "label": "คลิกที่นี่",
                            "data": "เช็คสิทธิ์",
                            "inputOption": "openKeyboard",
                            "fillInText": "กรุณาระบุหมายเลขรถเพื่อตรวจสอบสิทธิ์ "+typeData+" : "
                            }
                        }
                    ]
                }
                }
            ]
        }
    
def flexLimitParts(data, img) :
    return {
        "type": "bubble",
        "size": "micro",
        "hero": {
            "type": "image",
            "url": img,
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "320:213"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": data['Material Group'],
                "weight": "bold",
                "size": "xs",
                "wrap": True,
                "color": "#72716d"
            },
            {
                "type": "separator",
                "margin": "sm"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": "โควต้าทั้งหมด",
                    "flex": 0,
                    "color": "#555555",
                    "size": "xs",
                    "weight": "regular",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": str(data['Maximum Limit']),
                    "color": "#111111",
                    "size": "xs",
                    "weight": "bold",
                    "align": "end",
                    "wrap": True
                }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": "ใช้ไปแล้ว",
                    "flex": 0,
                    "size": "xs",
                    "color": "#555555",
                    "weight": "regular",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": str(data['Quantity']),
                    "size": "xs",
                    "color": "#111111",
                    "weight": "bold",
                    "align": "end",
                    "wrap": True
                }
                ]
            },
            {
                "type": "separator",
                "margin": "sm"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": "คงเหลือ",
                    "flex": 0,
                    "size": "xs",
                    "color": "#006633",
                    "weight": "regular",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": str(data['Remain Volume']),
                    "size": "xs",
                    "color": "#006633",
                    "weight": "bold",
                    "align": "end",
                    "wrap": True
                }
                ]
            }
            ],
            "spacing": "sm",
            "paddingAll": "13px"
        }
    }