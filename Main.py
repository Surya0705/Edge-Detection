import cv2 # Importing OpenCV.
from tkinter import filedialog # Importing tkinter filedialog for choosing image.

Path = filedialog.askopenfilename(title="Select Image") # Giving the Path.
Img = cv2.imread(Path) # Defining the Image.
Window_Name = "Image" # Giving a Window Name

cv2.imshow(Window_Name, Img) # Displaying the Image.
cv2.waitKey(0)
cv2.destroyAllWindows()