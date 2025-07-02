import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import PhotoImage
root=tk.Tk()
root.title('Tic tac toe')
photo = PhotoImage(file = "./icon_t.png")
root.iconphoto(False, photo)
root.resizable(False,False)
turn='X'
results=['','','','','','','','','']
player_point=[0,0]
def clicked(btn):
    global turn,results
    btn=int(btn)
    if results[btn]=='':
        if turn=='X':
            results[btn]='X'
            buttons[btn]['text']='X'
            buttons[btn]['fg']='white'
            buttons[btn]['bg']='#ee5281'
            turn="O"    
        elif turn=="O":
            results[btn]='O'
            buttons[btn]['text']="O"
            buttons[btn]['fg']='white'
            buttons[btn]['bg']='#26bbec'

            turn='X'
    rule()
def check_draw():
    global results
    if '' not in results:
        showinfo('Game','The game was tied.')
        reset()
def reset():
    global results,turn
    results=['','','','','','','','','']
    turn='X'
    board()
def show_winer(winner):
    global player_point
    if winner=='X':
        showinfo('Game','X winner!')
        player_point[0]+=1
        point_x.config(text=player_point[0])
        reset()
    elif winner=='O':
        showinfo('Game','O winner!')
        player_point[1]+=1
        point_o.config(text=player_point[1])
        reset()
def rule():
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for a,b,c in wins:
        if results[a] == results[b] == results[c] and results[a] != '':
            show_winer(results[a])
            return
    check_draw()
def point():
    global player_point
    global point_x, point_o
    player_frame=tk.Frame(root)
    player_frame.grid(row=0)
    labelplayer_x=tk.Label(player_frame,text='بازیکن X',padx=10,font=('aviny',20,'bold')).grid(row=0,column=0)
    labelplayer_x=tk.Label(player_frame,text='بازیکن O',padx=10,font=('aviny',20,'bold')).grid(row=0,column=1)
    ####point_frames
    point_frames=tk.Frame(root)
    point_frames.grid(row=1)
    point_x=tk.Label(point_frames,text=player_point[0],padx=10,font=('aviny',20,'bold'))
    point_x.grid(row=0,column=0)
    point_o=tk.Label(point_frames,text=player_point[1],padx=10,font=('aviny',20,'bold'))
    point_o.grid(row=0,column=1)
point()
def board():
    global buttons
    buttons=[]
    counter=0
    board_frame=tk.Frame(root)
    board_frame.grid(row=2)
    for row in range(1,4):
        for column in range(1,4):
            index=counter
            buttons.append(index)
            buttons[index]=tk.Button(board_frame,cursor="hand2",command=lambda x=f"{index}":clicked(x))
            buttons[index].config(width=12,height=5)
            buttons[index].grid(row=row,column=column)
            counter+=1
board()    
root.mainloop()