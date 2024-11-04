import tkinter as tk
from pynput import keyboard

class KeyInputApp:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.75)
        self.root.overrideredirect(True)
        self.root.geometry("+{}+{}".format(int(root.winfo_screenwidth()/2 - 100), int(root.winfo_screenheight() - 100)))
        
        self.label = tk.Label(root, text="", font=("Helvetica", 24), bg="black", fg="white")
        self.label.pack()

        self.current_keys = set()
        self.listener = keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release)
        self.listener.start()

    def on_key_press(self, key):
        try:
            self.current_keys.add(key.char)
        except AttributeError:
            self.current_keys.add(self.format_special_key(key))
        self.update_label()

    @staticmethod
    def upper(str1):
        return str1.upper()

    def on_key_release(self, key):
        try:
            self.current_keys.discard(key.char)
        except AttributeError:
            self.current_keys.discard(self.format_special_key(key))

        shift_keys = list(map(self.upper, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        for key2 in shift_keys:
            if key2 in self.current_keys:
                self.current_keys.discard(key2)
                self.current_keys.discard("⇧")

        self.update_label()

    def format_special_key(self, key):
        if key == keyboard.Key.cmd:
            return "⌘"
        elif key == keyboard.Key.cmd_r:
            return "⌘"
        elif key == keyboard.Key.shift:
            return "⇧"
        elif key == keyboard.Key.shift_r:
            return "⇧"
        elif key == keyboard.Key.ctrl:
            return "⌃"
        elif key == keyboard.Key.ctrl_r:
            return "⌃"
        elif key == keyboard.Key.alt:
            return "⌥"
        elif key == keyboard.Key.alt_r:
            return "⌥"
        elif key == keyboard.Key.backspace:
            return "⌫"
        elif key == keyboard.Key.space:
            return "␣"
        elif key == keyboard.Key.enter:
            return "⏎"
        elif key == keyboard.Key.esc:
            return "⎋"
        elif key == keyboard.Key.delete:
            return "⌦"
        elif key == keyboard.Key.tab:
            return "⇥"
        elif key == keyboard.Key.up:
            return "↑"
        elif key == keyboard.Key.down:
            return "↓"
        elif key == keyboard.Key.left:
            return "←"
        elif key == keyboard.Key.right:
            return "→"
        else:
            return str(key)

    def update_label(self):
        keys = " ".join(sorted(self.current_keys))
        self.label.config(text=keys)

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyInputApp(root)
    root.mainloop()