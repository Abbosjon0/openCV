import cv2

for i in range(1, 6):
    rasm = cv2.imread(f"{i}_oqqora.jpg")
    rangli_rasm = cv2.applyColorMap(rasm, cv2.COLORMAP_HOT)
    cv2.imwrite(f"{i}_rangli.jpg", rangli_rasm)
