import tkinter as tk

class WidgetGenerator:
    def create_label(self,frame,image,text,fg,bg,font_size,width,height,x,y):
        label = tk.Label(frame,image = image ,text = text , fg = fg, bg = bg, font=("fixedsys",font_size),width = width , height = height)
        label.pack(padx = x,pady = y)
        return label
        
    def create_button(self,frame,text,fg,bg,font_size,width,height,x,y,command_function):
        button = tk.Button(frame,text = text,fg = fg , bg = bg ,relief = "ridge", font=("fixedsys",font_size),width = width, height = height ,command = command_function) #It can be use by Lambda
        button.pack(padx = x , pady = y)

        button.bind("<Enter>",lambda event = button: self.hover_color_enter(event,bg,text,font_size))
        button.bind("<Leave>",lambda event = button: self.hover_color_leave(event,bg,text,font_size))
        return button

    def hover_color_enter(self,event,bg,text,font_size): #Effects for Button to like like an Arcade Game
        if bg == "yellowgreen":
            event.widget["background"] = "white"
            event.widget["foreground"] = "#007FFF"
            event.widget["width"] += 5
        elif bg == "#B23AEE":
            event.widget["background"] = "#BF3EFF"
            event.widget["foreground"] = "white"
            event.widget["width"] += 5
            event.widget["height"] += 2
            event.widget["text"] = ">>" + " " + text
        elif bg == "#8FA2B3":
            event.widget["width"] +=8
            event.widget["text"] = "Thank You <3"
           
    def hover_color_leave(self,event,bg,text,font_size):
        if bg == "yellowgreen":
            event.widget["background"] = "yellowgreen"
            event.widget["foreground"] = "white"
            event.widget["width"] -= 5
        elif bg == "#B23AEE":
            event.widget["background"] = "#B23AEE"
            event.widget["foreground"] = "white"
            event.widget["width"] -= 5
            event.widget["height"] -= 2
            event.widget["text"] = text
        elif bg == "#8FA2B3":
            event.widget["width"] -=8
            event.widget["text"] = "Home"
            
    def create_entry(self,frame,font_size,bg,justify,width,height,x,y,anchor):
        entry = tk.Entry(frame,font=("fixedsys",font_size),justify = justify,width = width,height = height)
        entry.pack(padx = x,pady = y,anchor = anchor)

        return entry


    def create_frame(self,bg,side,fill,expand,x,y,width,height):
        frame = tk.Frame(bg = bg ,padx = x , pady = y ,width = width,height = height)
        frame.pack(side = side,fill = fill,expand = expand)
        return frame

    def clear_frames(self,frames):
        for frame in frames:
            frame.destroy()


    def create_background_img(self,frame,file_path):

        bg_image = tk.PhotoImage(file=file_path)
        bg_image = bg_image.subsample(8,8)
        bg_label = tk.Label(frame,image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0,y=0,relwidth = 1,relheight = 1)

        return bg_label

if __name__ == "__main__":
    widget = WidgetGenerator()