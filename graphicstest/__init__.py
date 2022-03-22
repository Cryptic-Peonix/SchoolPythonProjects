import graphics as gr
import tkinter as tk


def main():
    win = gr.GraphWin("test", 200, 100)
    p = gr.Point(50, 50)
    t = gr.Text(p, "Python", gr.TextJustify.RIGHT)
    t.draw(win)
    b = gr.Rectangle(gr.Point(100, 50), gr.Point(150, 100))
    b.draw(win)
    win.getMouse()


def test():
    win = tk.Tk()
    win.geometry("750x280")
    canvas = tk.Canvas(win, width=1000, height=750, bg="SpringGreen2")
    canvas.create_text(300, 40, text="hello world", fill="black", anchor="w", font='Helvetica 15 bold')
    canvas.pack()
    win.mainloop()


main()
