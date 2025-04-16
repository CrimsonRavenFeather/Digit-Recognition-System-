import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import cv2

# Set up canvas size
CANVAS_SIZE = 280  # 10x bigger than 28x28 for easier drawing
IMG_SIZE = 28

class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=CANVAS_SIZE, height=CANVAS_SIZE, bg='white')
        self.canvas.pack()
        
        self.image = Image.new("L", (CANVAS_SIZE, CANVAS_SIZE), "white")  # 'L' = 8-bit grayscale
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)
        
        self.btn_save = tk.Button(master, text="Convert to 28x28", command=self.convert)
        self.btn_save.pack()

    def paint(self, event):
        x1, y1 = (event.x - 8), (event.y - 8)
        x2, y2 = (event.x + 8), (event.y + 8)
        self.canvas.create_oval(x1, y1, x2, y2, fill='black')
        self.draw.ellipse([x1, y1, x2, y2], fill='black')  # Also draw to PIL image

    def convert(self):
        # Resize to 28x28 and invert
        img = self.image.resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)
        img = ImageOps.invert(img)

        # Convert to NumPy array and normalize
        img_np = np.array(img) / 255.0
        img_np = img_np.reshape(1, 28, 28, 1)

        # ✅ Store image in a class variable
        self.processed_image = img_np

        # (Optional) show or print
        print("Image shape:", img_np.shape)
        cv2.imshow("28x28 Image", img_np[0].reshape(28, 28))
        cv2.waitKey(0)
        cv2.destroyAllWindows()


# Launch the app
root = tk.Tk()
app = DrawingApp(root)
root.mainloop()
 # type: ignore

your_image = app.processed_image
# prediction = model.predict(your_image)


