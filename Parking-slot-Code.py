import cv2
import pickle
import cv zone
import NumPY as np
cap = cv2.VideoCapture(“file path”)
with open(‘file path’) as f:
     posList = pickle.load(f)

 width,height = 107,48

              def checkParkingSpace(imgPro):
                    spaceCounter = 0

     for pos in posList: 
        x,y=pos
        imgCrop = imgPro[y:y + height, x:x + width]
        #cv2.imshow(str(x*y),imgCrop)
        count = cv2.count NonZero(imgCrop)

         if count<900:
             color = (0,255,0)
           thickness = 5
           spaceCounter+=1
       else:
           color = (0,0,255)
           thickness = 2
       cv2.rectangle(img, pos, (pos[0] + width,pos[1] + height) ,color, thickness)
       cv2zone.putTextRect(img,str(count),(x,y + height-3), scale=1, thickness=2, offset=0, colorR=color)
       cv2zone.putTextRect(img.f’Free: {spaceCounter}/{len(posList)}’,(100,50), scale=3,
              thickness=5,offset=20,colorR=(0,200,0)
while True:
if		cap.get(cv2.CAP_PROP_POS_FRAMES)
cap.get(cv2.CAP_PROP_FRAME_COUNT);
       cap.set(cv2.CAP_PROP_POS_FRAMES,0)
     success,img=cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY
     imgBlur = cv2.GuassianBlur(imgGray,(3,3),1)
     imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GUASSIAN_C,cv2.THRSH_BINARY_INV,25,16)
     imgMedian = cv2.medianBlurring(imgThreshold,5)
     kernel = np.ones((3,3),np.unit8)
     imgDilate(imgMedian,kernel,iterations=1)
     checkParkingSpace(imgDialte)
     cv2.imshow(“Image”,img)
      cv2.waitKey(10)
