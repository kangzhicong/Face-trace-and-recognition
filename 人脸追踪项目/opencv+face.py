from PIL import Image
import face_recognition
import cv2


# 将jpg文件加载到numpy 数组中
image = face_recognition.load_image_file("1-1.jpeg")

# 使用默认的给予HOG模型查找图像中所有人脸
# 这个方法已经相当准确了，但还是不如CNN模型那么准确，因为没有使用GPU加速
# 另请参见: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

# 使用CNN模型
# face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")

# 打印：我从图片中找到了 多少 张人脸
print("我从图片中找到了{} 张人脸".format(len(face_locations)))

# 循环找到的所有人脸
for face_location in face_locations:

        # 打印每张脸的位置信息
        top, right, bottom, left = face_location
        print("位于像素位置的:上{}, 左: {}, 下: {}, 右: {}".format(top, left, bottom, right))
# 指定人脸的位置信息，然后显示人脸图片
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()
#        pil_image.save('tt.jpg')
for top, right, bottom, left in face_locations:
    # 对人脸画框
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    rgb_img=image[:,:,::-1]
    cv2.imshow("img", rgb_img)
if cv2.waitKey(0):
    cv2.destroyAllWindows()
