import cv2
def get_face_data():
    # 加载Haar级联数据文件，用于检测人面
    face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')
    camera = cv2.VideoCapture(0)
    count = 1
    while True:
        ret, frame = camera.read()
        print(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 人面识别。detectMultiScale参数说明：
        # gray: 进行检测的图像, 这里是转换后的。
        # scaleFactor: 官网文档说是每次图片缩小的比例, 其实可以这么理解, 距离相机不同的距离, 物体大小是不一样的, 在物体大小不一致的情况下识别一个东西是不方便的, 这就需要进行多次的缩放, 这就是这个参数的作用。
        # minNeighbors: 可以理解为每次检测时, 对检测点(Scale)周边多少有效点同时检测, 因为可能选取的检测点大小不足而导致遗漏。
        # minSize: 检测点的最小值, 或者说就是检测点的最终值。
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(5,5))
        # 画出面部位置
        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # 根据检查的位置截取图片并调整截取后的图片大小
            f = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
            # 保存图片
            cv2.imwrite('auto/alin/%s.pgm' %(str(count)),f)
            count += 1
        cv2.imshow('pic', frame)
        # 停止程序
        if cv2.waitKey(120) & 0xff == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    get_face_data()


