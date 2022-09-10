import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(5, 30)
test="test"

ret, frame = cap.read()
rows, cols, channels = frame.shape
print(cols, rows, channels)

while(1):
    success,img=cap.read()
    cv2.imshow("video",img)
    k=cv2.waitKey(1) & 0xFF
    if (k==ord('q')):
            break
    elif(k == ord('s')):
        cv2.imwrite("./image_1.jpg",img)
        print("success to save image_1..jpg")
cap.release()
cv2.destroyAllWindows()
