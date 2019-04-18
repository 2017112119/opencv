#导入所需库
import requests
import base64
import cv2
import json

#face++ api
api_url = "https://api-cn.faceplusplus.com/imagepp/v1/mergeface"
api_key = "NX8KdroXLubyVVyOVn0bLDvl6VeqvehB"
api_secret = "4QaNZt3E2dsZABnGDaXBFiKyUU7hqKKx"

# 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值 ,opencv  人脸识别 模型加载
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')

#读取图片
img = cv2.imread('img.jpg')    #模板图
# img = cv2.resize(img,(256,480))
img1 = cv2.imread('img1.jpg')   #融合图
# img1 = cv2.resize(img1,(256,480))

# cv2.imshow('im',img1)
# cv2.imshow('im1',img)
# cv2.waitKey(0)

#转换为灰度图
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

# 探测图片中的人脸
faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.15,minNeighbors = 5,minSize = (5,5))
faces1 = face_cascade.detectMultiScale(gray1,scaleFactor = 1.15,minNeighbors = 5,minSize = (5,5))

#将 rectangle   转换为   79,79,144,144     格式
for i in faces:
    rec = list(map(str,i))
    rectangle = ','.join(rec)
    print(rectangle)
for i in faces1:
    rec1 = list(map(str,i))
    rectangle1 = ','.join(rec1)
    print(rectangle1)

#图像编码为  base64
with open('img.jpg','rb') as f:
    base_img = base64.b64encode(f.read())
    print(base_img)
with open('img1.jpg','rb') as f:
    merg_base = base64.b64encode(f.read())
    print(merg_base)

#数据传入    使用post
res = requests.post(api_url,data={'api_key':api_key,'api_secret':api_secret,'template_base64':base_img,
                                  'template_rectangle':rectangle,
                                  'merge_base64':merg_base,
                                  'merge_rectangle':rectangle1,
                                  'merge_rate':100}).text

#将返回的数据进行格式转换  str to dict
# print(res.text)
res_img = json.loads(res)
print(res_img)

#将返回的图像解码
res_img = base64.b64decode(res_img["result"])
#print(type(res_img))
# 图片数据写入 文件
with open('mer_feca1.jpg','wb') as f:
    f.write(res_img)
