import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch Timer")
        self.time_elapsed = 0
        self.running = False

        self.label = tk.Label(root, text="00:00:00", font=("Arial", 30))
        self.label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Start", command=self.start, width=10)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop, width=10)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset, width=10)
        self.reset_button.pack(side=tk.LEFT, padx=5)
    
    def update(self):
        if self.running:
            self.time_elapsed += 1
            self.label.config(text=self.format_time(self.time_elapsed))
            self.root.after(1000, self.update)
    
    def format_time(self, seconds):
        h, m, s = seconds // 3600, (seconds % 3600) // 60, seconds % 60
        return f"{h:02}:{m:02}:{s:02}"
    
    def start(self):
        if not self.running:
            self.running = True
            self.update()
    
    def stop(self):
        self.running = False
    
    def reset(self):
        self.running = False
        self.time_elapsed = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
