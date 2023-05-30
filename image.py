def getImageURL(name):
    if name.find("น้ำยาหม้อน้ำ") != -1:
        if name.find("1") != -1:
           imageId = 'AFGJ81r5FoF_BGL8JCsC8_4TMQEqtiFMY1KS_TVaqVv1I6dhJJTA2dlknUyWFyRcBbjGQltkCIxTCdo7FZu_7hHl5d3ZvHaXSA=s1600'
        else : 
            imageId = 'AFGJ81qWU_hWJJP84YO9iDWF0E0HNd5kyOHh8zbpj3w5_OHZ4Dod_YjPBoPUjnZ8J8RHCkzlwYGBvd2LSNHWKDSN3_a67hIuwQ=s1600'
    elif name.find("น้ำมันขับเคลื่อน") != -1:
        if name.find("3") != -1:
            imageId = 'AFGJ81ombxOljdGJ79Ia4C1jBJxny79K8QO1kPAFMi_sp5tDt8FpyaE8myMpKMERgOVFfI1lyoCJUAMpuVnsFjsKqE3XbNHKDw=s1600'
        else : 
            imageId = 'AFGJ81rWcBK62VKuWdkej-3othORGSTETeqWf08C6eQVqJ1EAvfE06avfIcx8U6WO_3Q4JUAo8aZ1Rf7SNO9X06gGoe-KIfj=s1600'
    elif name.find("น้ำมันยูดีทีตราช้าง") != -1:
        if name.find("18") != -1:
            imageId = 'AFGJ81qKf57qJzDEvI6V9Xv-og_YTTuVPLikl4vC7PgFL0MYa-nl5BxxsQoty8RPQP3z5CiOrcKBqDErqWB2UuymSUeiB4Q66A=s1600'
        else : 
            imageId = 'AFGJ81q4GB1x-Tyd3MZTgnLEM4d4-y9EGbRXr9Y4QEimr2gwZkxFQOgvQuUrDjNS7DRAINrGB3KkbHlyq-nq8qW74Jl9iaVOuw=s1600'
    elif name.find("น้ำมันเครื่องตราช้าง") != -1:
        if name.find("3") != -1:
            imageId = 'AFGJ81ombxOljdGJ79Ia4C1jBJxny79K8QO1kPAFMi_sp5tDt8FpyaE8myMpKMERgOVFfI1lyoCJUAMpuVnsFjsKqE3XbNHKDw=s1600'
        else : 
            imageId = 'AFGJ81qrUacQNwrLt5wSJWlsljbOzjJbDIQ70HOSb-zr6OMT8v3m8tf6mQRLq7F0uJri6hqeM7n7H2tqdFb266r9wclvoQ5qKg=s1600'
    else :
        imageId = 'AFGJ81rNg7AzhOKKkdVN4jL5uA6QPtl9O8waMg5tCJ9rmmzoe1EDghCUdgqf1yMTUHwF2K-7Bi1Bj2iAaNGDFtutDCHl6b8T7g=s1600'
    
    return 'https://lh3.googleusercontent.com/drive-viewer/'+imageId
        