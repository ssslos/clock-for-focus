import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r") # 输出到屏幕，并且不换行
        time.sleep(1)
        seconds -= 1

if __name__ == "__main__":
    minutes = 25  # 设置专注时长为25分钟
    countdown(minutes)
    print("专注结束！")
