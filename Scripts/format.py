from tkinter import Tk
while True:
    table = input('variable name: ') + ' = ['
    i = -1
    print('enter table values:\n')
    while True:
        i += 1
        a = input()
        if a == '':
            break
        else:
            if i == 0:
                table += (a + ',\n')
            elif i > 0:
                table += ('    ' + a + ',\n')
    table = table[:len(table)-2]
    table += ']'
    x = Tk()
    x.withdraw()
    x.clipboard_clear()
    x.clipboard_append(table)
    x.update()
    x.destroy()
    print(f'{i} lines copied to clipboard\n')
