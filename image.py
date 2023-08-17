def getImageURL(name):
    if name.find("น้ำยาหม้อน้ำ") != -1:
        if name.find("1") != -1:
           imageId = 'น้ำยาหม้อน้ำแบบ1ลิตร.png'
        else : 
            imageId = 'น้ำยาหม้อน้ำแบบ3ลิตร.png'
    elif name.find("น้ำมันขับเคลื่อน") != -1:
        if name.find("3") != -1:
            imageId = 'น้ำมันขับเคลื่อนSAE90แบบ3ลิตร.png'
        else : 
            imageId = 'น้ำมันขับเคลื่อนSAE90แบบ6ลิตร.png'
    elif name.find("น้ำมันยูดีทีตราช้าง") != -1:
        if name.find("18") != -1:
            imageId = 'น้ำมันยูดีทีตราช้าง18ลิตร(ห้องเกียร์40ลิตร).png'
        else : 
            imageId = 'น้ำมันยูดีทีตราช้าง6ลิตร(ห้องเกียร์40ลิตร).png'
    elif name.find("น้ำมันเครื่องตราช้าง") != -1:
        if name.find("3") != -1:
            imageId = 'น้ำมันเครื่องตราช้างเกรดCF4แบบ3ลิตร.png'
        else : 
            imageId = 'น้ำมันเครื่องตราช้างเกรดCF4แบบ6ลิตร.png'
    else :
        imageId = 'น้ำมันไฮดรอลิก(ถังน้ำมันไฮดรอลิก)แบบ18ลิตร.png'
    
    return 'https://csblobfile.blob.core.windows.net/ksc2023/'+imageId

def imageLimitPart():
    return 'https://csblobfile.blob.core.windows.net/ksc2023/Maintenance_spare_parts_quota_table.png'