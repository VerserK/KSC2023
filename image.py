def getImageURL(name):
    if name.find("น้ำยาหม้อน้ำ") != -1:
        if name.find("1") != -1:
           imageId = 'น้ำยาหม้อน้ำแบบ 1 ลิตร.png'
        else : 
            imageId = 'น้ำยาหม้อน้ำแบบ 3 ลิตร.png'
    elif name.find("น้ำมันขับเคลื่อน") != -1:
        if name.find("3") != -1:
            imageId = 'น้ำมันขับเคลื่อน SAE 90 แบบ 3 ลิตร.png'
        else : 
            imageId = 'น้ำมันขับเคลื่อน SAE 90 แบบ 6 ลิตร.png'
    elif name.find("น้ำมันยูดีทีตราช้าง") != -1:
        if name.find("18") != -1:
            imageId = 'น้ำมันยูดีทีตราช้าง 18 ลิตร (ห้องเกียร์ 40 ลิตร).png'
        else : 
            imageId = 'น้ำมันยูดีทีตราช้าง 6 ลิตร (ห้องเกียร์ 40 ลิตร).png'
    elif name.find("น้ำมันเครื่องตราช้าง") != -1:
        if name.find("3") != -1:
            imageId = 'น้ำมันเครื่องตราช้างเกรด CF4 แบบ 3 ลิตร.png'
        else : 
            imageId = 'น้ำมันเครื่องตราช้างเกรด CF4 แบบ 6 ลิตร.png'
    else :
        imageId = 'น้ำมันไฮดรอลิก (ถังน้ำมันไฮดรอลิก) แบบ 18 ลิตร.png'
    
    return 'https://csblobfile.blob.core.windows.net/ksc2023/'+imageId

def imageLimitPart():
    return 'https://csblobfile.blob.core.windows.net/ksc2023/ตารางโควต้า อะไหล่บำรุงรักษา.png'
        