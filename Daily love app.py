from tkinter import*
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk,messagebox


root=Tk()
root.title("Daily Love App")
root.geometry("900x500+300+200")
root.resizable(False,False)

#logo
original_image = Image.open("logo.png")
resized_image = original_image.resize((200, 200))  # Set the size you want (width, height)
logo_image = ImageTk.PhotoImage(resized_image)

# Place the logo in your window
logo = Label(image=logo_image)
logo.place(x=0, y=0)

# Keep a reference to avoid garbage collection
logo.image = logo_image



#name input
name_label=Label(root,text="Your name:",font=("Helvetica",14))
name_label.place(x=250,y=50)
name_entry=Entry(root,font=("Helvetica",14),width=30)
name_entry.place(x=370,y=50)


#mood vibe
mood_label = Label(root, text="How are you feeling today?", font=("Helvetica", 14))
mood_label.place(x=250, y=100)

mood_var = tk.StringVar(value="Happy")
moods = ["Happy", "Sad", "Overwhelmed", "Lonely", "I miss you"]
mood_menu = ttk.Combobox(root, textvariable=mood_var, values=moods, font=("Helvetica", 12), state="readonly")
mood_menu.place(x=550, y=100)

def generate_note():
    name = name_entry.get().strip()
    mood = mood_var.get()

    if not name:
        messagebox.showwarning("Oops!", "Please enter a name.")
        return

    if mood == "Happy":
        message = f"Hey {name}, I just wanted to remind you how incredibly lucky I feel to have you in my life. You light up my world in ways I never thought possible — like seriously, even my bad days do a little happy dance when you're around.Your smile? Magic. Your laugh? My favorite sound. Your love? The best thing that ever happened to me.So here’s a little note, just to say I’m thinking of you and smiling like an idiot because… well, it’s you.Can’t wait to make more memories, share more laughs, and love you a little more every single day.Always yours,💛"
    elif mood == "Sad":
        message = f"Hey love,I know things feel heavy right now, and I wish I could take that weight off your shoulders. But since I can't, I just want you to know — I'm here. With you. For you. Always.You don’t have to smile for me, or pretend you’re okay. Just be. I’ll sit with you in the quiet, in the mess, in the middle of it all.You are not alone in this. Even when everything feels grey, my heart is right beside yours, holding space for the light to return — and it will.Take all the time you need. I’m not going anywhere {name}."
    elif mood == "Overwhelmed":
        message = f"{name}, I know everything feels like a lot right now — like the world won’t stop spinning, and you're trying to keep up while carrying more than you should have to.But take a breath with me.You don’t have to have it all figured out today. Or tomorrow. It’s okay to pause. It’s okay to cry. It’s okay to just be.You’re doing so much better than you think, and I’m so proud of you — not just for what you do, but for who you are.Let me be your calm in the chaos. Lean on me. Rest here. We’ll get through this together — one small, steady step at a time."
    elif mood == "Lonely":
        message = f"My dearest {name}, I don’t know exactly what your heart is carrying today, but I want you to know this — you are not alone. Not really. Not with me here, loving you quietly and completely from wherever I am.Loneliness can feel so loud sometimes, like an echo that won’t stop. But I’m sending you all my warmth, wrapping it around you like a hug you can feel even in the silence.Close your eyes for a second. Picture me holding your hand, reminding you that you matter — deeply. You are seen. You are loved. And I’m not going anywhere.You’ve got me, always.."
    elif mood == "I miss you":
        message = f"Oh baby I miss you too — more than words can catch. And if I could, I’d wrap you up in the biggest hug right now, just to remind you how close you still are, even when we’re apart.I carry you with me — in the quiet moments, in the laugh I didn’t expect, in the way my heart softens every time I think of you.This space between us? It’s only physical. My thoughts, my love, my energy — they’re all already with you. Always have been.So hang in there, okay? We’ll be together soon. Until then, just know… someone out here is missing you just as much — and loving you even more.Forever yours,{name}"

    output_text.config(state="normal")
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, message)
    output_text.config(state="disabled")

generate_button = Button(root, text="Generate Love Note 💌", font=("Helvetica", 14), command=generate_note)
generate_button.place(x=350, y=150)

#output
output_text = Text(root, font=("Helvetica", 14), height=6, width=60, wrap="word", state="disabled", bg="#fff0f5")
output_text.place(x=100, y=220)
#scrollable
output_frame=Frame(root)
output_frame.place(x=100,y=220)
scrollbar = Scrollbar(output_frame)
scrollbar.pack(side=RIGHT, fill=Y)

output_text = Text(output_frame, font=("Helvetica", 14), height=6, width=60, wrap="word", state="disabled", bg="#fff0f5", yscrollcommand=scrollbar.set)
output_text.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=output_text.yview)

def export_note():
    content = output_text.get("1.0", tk.END).strip()
    if not content:
        messagebox.showwarning("Empty", "There's no note to export!")
        return
    try:
        with open("love_note.txt", "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("Success", "Love note saved as love_note.txt ❤️")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

export_button = Button(root, text="Export Note 📝", font=("Helvetica", 12), command=export_note)
export_button.place(x=390, y=400)

root.mainloop ()