import cv2
import matplotlib.pyplot as plt

# 1. Load the original image
image = cv2.imread('yuji_itadori.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display Original RGB Image
plt.imshow(image_rgb)
plt.title("Original RGB Image")
plt.show()

# 2. Rotation (90 Degrees Clockwise)
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
rotated_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

# 3. Cropping (Using your exact slicing technique)
cropped_image = image[90:155, 115:180]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Image")
plt.show()

# 4. Brightness Adjustment 
# Increases pixel intensities safely by 50 using cv2.add
bright_image = cv2.add(image, 50)
bright_rgb = cv2.cvtColor(bright_image, cv2.COLOR_BGR2RGB)
plt.imshow(bright_rgb)
plt.title("Brightened Image")
plt.show()

# 5. Transformation (Horizontal Flip / Mirror)
flipped_image = cv2.flip(image, 1) # 1 means horizontal flip
flipped_rgb = cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB)
plt.imshow(flipped_rgb)
plt.title("Transformed (Flipped) Image")
plt.show()
