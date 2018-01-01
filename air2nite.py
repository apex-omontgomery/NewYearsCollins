
from time import sleep, localtime
import webbrowser

controller = webbrowser.get()

def convert_struct(input):
    return f"{input.tm_hour}:{input.tm_min}:{input.tm_sec}"
    
def check_time(input):    
    return str(input.tm_hour) + str(input.tm_min) + str(input.tm_sec) < '115640'
    
def loop():
    now = localtime()
    while check_time(now):
        print(convert_struct(now), end='\r')
        now = localtime()
        sleep(0.1)


if __name__ == '__main__':
    loop()
    controller.open("https://www.youtube.com/watch?v=MN3x-kAbgFU")
    
    
