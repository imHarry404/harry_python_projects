from time import sleep
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title="Pani P lo bhai 💧😉",
            message="half hour ho gya hai to ab pani p lo,okk 🥱🐍🤪",
            app_icon="C:\\Users\\hario\\Desktop\\to_learn\\10_days_of_python_31_july\\water_drinking_remainder\\icon.ico",
            timeout=2 #it will apper for 2 seconds as notification
        )
        sleep(60*30) #means it will appear in every 30 minutes,,here sleep take args as seconds
        # 60*30= 1800 seconds


# wait for 10 seconds, it will come again, it will always notify you after every 10seconds, yourt can give time as per your choice


# from now will appear after half hour from now

# enjoy