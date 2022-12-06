import tkinter as tk
import maze_maker

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my, maze_list
    if key == "Up" and maze_list[mx][my - 1] == 0:      #上が入力されかつ、移動先が道なら
        my -= 1
    if key == "Down" and maze_list[mx][my + 1] == 0:        #下が入力されかつ、移動先が道なら
        my += 1           
    if key == "Left" and maze_list[mx - 1][my] == 0:        #左が入力されかつ、移動先が道なら
        mx -= 1
    if key == "Right" and maze_list[mx + 1][my] == 0:       #右が入力され、移動先が道なら
        mx += 1

    #ゴールに到着したかの確認
    if mx == 13 and my == 7:
        finish()

#クリア表示
def finish():
    label.place(x = 670, y = 370)    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()
    #クリア表示
    label = tk.Label(root, text = "クリア", font = ("", 80), bg = "#00ffff")

    #画像関連
    kokaton = tk.PhotoImage(file = "fig/3.png")
    mx, my = 1, 1
    cx, cy = mx * 100 + 50, my * 100 + 50
    canvas.create_image(cx, cy, image = kokaton, tag = "kokaton")

    #キー入力関連
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    

    root.mainloop()