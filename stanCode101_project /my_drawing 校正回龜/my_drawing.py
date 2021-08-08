"""
File: my_drawing.py
Name: fanny
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    covid-19 new case number need to use '校正回歸'
    """
    window = GWindow(width=800, height=600, title='pixel')

    circle = GOval(500, 180)
    circle.color = 'black'
    circle.filled = True
    circle.fill_color = 'coral'
    window.add(circle, 150, 100)

    label = GLabel('校正回ㄍㄨㄟ', x=200, y=230)
    label.font ='-70'
    window.add(label)



    floor = GRect(250, 10)
    floor.filled = True
    floor.fill_color = 'black'
    window.add(floor, 200, 490)

    shell_1 = GRect(10, 50)
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 200, 380)
    shell_1 = GRect(10, 50)
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 210, 430)
    shell_1 = GRect(10, 10)
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 220, 480)
    shell_1 = GRect(10, 10)
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 260, 480)
    shell_1 = GRect(110, 10)
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 250, 470)
    shell_1 = GRect(10, 10)
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 360, 480)
    shell_1 = GRect(10, 10)
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 400, 480)
    shell_1 = GRect(10, 20) #前腳
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 390, 460)
    shell_1 = GRect(20, 10)
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 400, 450)
    shell_1 = GRect(10, 10)
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 420, 440)
    shell_1 = GRect(10, 20)
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 430, 420)
    shell_1 = GRect(20, 10) #下嘴巴
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 440, 410)
    shell_1 = GRect(10, 10)  # 下嘴巴
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 460, 400)
    shell_1 = GRect(10, 40)  # 下嘴巴
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 470, 360)
    shell_1 = GRect(10, 10)
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 460, 350)
    shell_1 = GRect(40, 10)  # 下嘴巴
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 420, 340)
    shell_1 = GRect(10, 10)  # 下嘴巴
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 410, 350)
    shell_1 = GRect(10, 20)
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 400, 360)
    shell_1 = GRect(10, 50)
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 390, 380)
    # colored flash
    lightgreen = GRect(30, 10)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 230, 480)
    lightgreen = GRect(30, 10)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 220, 470)
    lightgreen = GRect(170, 10)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 220, 460)
    lightgreen = GRect(20, 10)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 220, 450)

    lightgreen = GRect(40, 10)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 360, 450)

    lightgreen = GRect(30, 10)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 360, 470)

    lightgreen = GRect(30, 10)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 370, 480)

    lightgreen = GRect(40, 10)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 380, 440)

    lightgreen = GRect(40, 10)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 390, 430)

    lightgreen = GRect(30, 20)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 400, 420)

    lightgreen = GRect(40, 10)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 400, 410)

    lightgreen = GRect(60, 10)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 400, 400)

    lightgreen = GRect(70, 20)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 400, 380)

    lightgreen = GRect(60, 10)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 410, 370)
    lightgreen = GRect(60, 10)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 410, 360)
    lightgreen = GRect(40, 10)
    lightgreen.color = 'limegreen'
    lightgreen.filled = True
    lightgreen.fill_color = 'limegreen'
    window.add(lightgreen, 420, 350)


    # Shell color
    shell = GRect(170, 10)
    shell.color = 'darkgreen'
    shell.filled = True
    shell.fill_color = 'darkgreen'
    window.add(shell, 220, 430)

    shell = GRect(130, 10)
    shell.color = 'darkgreen'
    shell.filled = True
    shell.fill_color = 'darkgreen'
    window.add(shell, 240, 440)

    shell = GRect(180, 50)
    shell.color = 'darkgreen'
    shell.filled = True
    shell.fill_color = 'darkgreen'
    window.add(shell, 210, 380)

    shell = GRect(160, 10)
    shell.color = 'darkgreen'
    shell.filled = True
    shell.fill_color = 'darkgreen'
    window.add(shell, 220, 370)

    shell = GRect(140, 10)
    shell.color = 'darkgreen'
    shell.filled = True
    shell.fill_color = 'darkgreen'
    window.add(shell, 230, 360)

    shell = GRect(120, 10)
    shell.color = 'darkgreen'
    shell.filled = True
    shell.fill_color = 'darkgreen'
    window.add(shell, 240, 350)






    shell_1 = GRect(10, 10) # 下龜殼
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 380, 430)
    shell_1 = GRect(20, 10)  # 下龜殼
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 360, 440)
    shell_1 = GRect(120, 10)  # 下龜殼
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 240, 450)
    shell_1 = GRect(20, 10)  # 下龜殼
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 220, 440)
    shell_1 = GRect(10, 10)  # 上龜殼 左
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 210, 370)
    shell_1 = GRect(10, 10)  # 上龜殼 左
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 220, 360)
    shell_1 = GRect(20, 10)  # 上龜殼 左
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 230, 350)
    shell_1 = GRect(100, 10)  # 上龜殼 中
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 250, 340)
    shell_1 = GRect(20, 10)  # 上龜殼 右
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 350, 350)
    shell_1 = GRect(10, 10)  # 上龜殼 右
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 370, 360)
    shell_1 = GRect(10, 10)  # 上龜殼 右
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 380, 370)
    shell_1 = GRect(20, 20)  # eye
    shell_1.filled = True
    shell_1.fill_color = 'black'
    window.add(shell_1, 430, 370)






if __name__ == '__main__':
    main()
