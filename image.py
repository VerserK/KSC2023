def getImageURL(name):
    if name.find("น้ำยาหม้อน้ำ") != -1:
        if name.find("1") != -1:
           imageId = 'AITFw-xLWks2vSriTa5gEOM9FL6l9gPF61Z9TjxmABaNdsJV01_InllRZOTnNUAUePrXt8KCRj8g0vAithhc4R0JjCf9SCEEZw=s1600'
        else : 
            imageId = 'AITFw-xWLFnnteKmdKqDUQCMcAiiEw51W795nBHr_Q58QGE8F3lnm2qDJPEw8axUtEmue9feidSArGKJJxS4s4vYrB0FruXb=s1600'
    elif name.find("น้ำมันขับเคลื่อน") != -1:
        if name.find("3") != -1:
            imageId = 'AITFw-wsb5-CduB8C1KJ2gvP3Nmq1vFckmUEz8gWrQQpQp3yVrIfuOdql821ghJjA0OrIqivpCkiuivuv0qCySo07zXhczsK8A=s1600'
        else : 
            imageId = 'AITFw-xEHgCq5LQbpgvrmyJI5T-B9AkmxxVNRmU0v-Sbc9aRDYMofNiGZbP4dpVa92lSJ4yjDEfDdFByJ0WJnLPC0vETom3BnQ=s1600'
    elif name.find("น้ำมันยูดีทีตราช้าง") != -1:
        if name.find("18") != -1:
            imageId = 'AITFw-yn_A4bSSdsfwi7FeVH9oiOe6HejngDxzRKNd3aUxUDf54dZtoJxTKUyXKCFAEfOajBpcJz3HhegUzHPn3hZBAu2R-i_g=s1600'
        else : 
            imageId = 'AITFw-zKnkEUAW9SDWH75zFnXiAoDnLM9ZOnjMrG04SNMP6urmYpVP9e0spuSgJHOItEiM9QPGt2YcOmff-jlhQaHt07hEfK2A=s1600'
    elif name.find("น้ำมันเครื่องตราช้าง") != -1:
        if name.find("3") != -1:
            imageId = 'AITFw-z8DFa2ut16aCdzIxcvtICkV3LCCF14-Ms_uSefi17Z2DEZ8c7tXXaRVGfub8hq-6_ANqzvew-TsWqFoLOeLvSioERlWA=s1600'
        else : 
            imageId = 'AITFw-zqYaQel3aHp6O6ZaseLIigKyDSCWL_prsLlQQnYF96DClA72XcBj1etJw9MjyASCTZgG7Ro7M6ssSzLiDvFA5AqmBvTw=s1600'
    else :
        imageId = 'AITFw-y6Ro-8ltZU34JY2JN7Cvia0zG7A_k4ScgOrpHE_ZK75NxH0rrEP6DUHiYJTBY48WZAqEHgVaAcREi8UM5hVQMynxUf=s1600'
    
    return 'https://lh3.googleusercontent.com/drive-viewer/'+imageId

def imageLimitPart():
    return 'https://lh3.googleusercontent.com/drive-viewer/AITFw-wTmOG1k9ni_L0L_iIjb6P2J6peC9AGFE6dzeSMibszlJvD0IYJiXmDSOvfeFvmEKH1QHWK4qhN67d7QRwpUCEPSbKIHQ=s1600'
        