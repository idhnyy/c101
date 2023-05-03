import time

def counting(timeSec):
    while timeSec >0:
        minutes = int(timeSec/60)
        seconds = int(timeSec%60)
        resp = f"{minutes}:{seconds}"
        
        print(resp,end="\r")
        time.sleep(1)
        timeSec -=1
    print("Tempo esgotado")


timeSec = input("Digite o tempo em segundos:")
counting(int(timeSec))