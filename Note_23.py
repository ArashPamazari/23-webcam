# face detection : peyda kardan chehre dar tasvir
# face recogniton : hala ke peydash kardi bgo face kie

import cv2

img = cv2.imread('spiderman.jpg')

cv2.rectangle(img,(50,120),(200,250),(0,255,0),4)  #def rectangle : mokhtasat avali : goshe bala samte chap , mokhtasat dovomi : goshe paeen samte rast , chaharomi parameter : rang ,5 omi : zekhamat rec

cv2.imshow('output', img)
cv2.waitKey()


#------------------------------------------#

# open cv yek mazhol amade dare baray tashkhis chehre

# github open cv 
# tamame library haye marof toie github sorce codeshon hast

# algo ghadimie : haarcascade_frontalface_default.xml

import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('sajjad.jpg',0)
# img = cv2.resize(img,(0,0), fx=0.5 , fy=0.5) # ax ro injori nesf kardim sizesho

img_color= cv2.imread('ronaldo.jpg')
img_gray= cv2.imread('ronaldo.jpg',0)

# faces = face_detector.detectMultiScale(img , 1.3 , minSize = (30,30)) #1.3 parameter hasasiat tashkhis , minSize= minsize = (30,30) ==> ina faceaee ke 30 pixelan noisan , tozihat ro dar real python bar dar
faces = face_detector.detectMultiScale(img_gray , 1.3 , minSize = (30,30)) #baray inke tasviro rangi betone detect kone chon defesh ba gray kar mikone

#for face in faces:
    #x,y,w,h = face #khode face shamel 4ta adade ke toie terminal didim
    #cv2.rectangle(img,(x,y),(x+w , y+h), (0,255,0) , 8) #x,y goshe bala chap , x+w,y+h goshe paeen rast , rang , zekhamat
  
for face in faces:
    x,y,w,h = face #khode face shamel 4ta adade ke toie terminal didim
    cv2.rectangle(img_color,(x,y),(x+w , y+h), (0,255,0) , 8) #x,y goshe bala chap , x+w,y+h goshe paeen rast , rang , zekhamat
    img_face= img_color[y:y+h , x:x+w] #baray inke khode face haro ham save konim

    cv2.imshow('face', img_face)
    cv2.waitKey()

cv2.imshow('output', img_color)
cv2.waitKey()



#---------------------------------

import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img_color= cv2.imread('ronaldo.jpg')
img_gray= cv2.imread('ronaldo.jpg',0)


sticker1= cv2.imread('sticker.png')
sticker2= cv2.imread('sticker2.png')
stickers=[sticker1,sticker2]


for i,face in enumerate(faces): #ham andiso mide ham khodesh
    x,y,w,h = faces[i]
    sticker1_resized = cv2.resize(stickers[i],(w,h))
    img_color[y:y+h , x:x+w] = sticker1_resized

cv2.imshow('output', img_color)
cv2.waitKey()


#---------------------------------
import random
import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img_color= cv2.imread('team.jpg')
img_gray= cv2.imread('team.jpg',0)


sticker1= cv2.imread('sticker.png')
sticker2= cv2.imread('sticker2.png')
stickers=[sticker1,sticker2]


for i,face in enumerate(faces): #ham andiso mide ham khodesh
    x,y,w,h = faces[i]
    sticker1_resized = cv2.resize(random.choice(stickers),(w,h))
    img_color[y:y+h , x:x+w] = sticker1_resized

cv2.imshow('output', img_color)
cv2.waitKey()




#----------------------------------------------#
#pardazesh video

import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#video_cap = cv2.VideoCapture('harchi.mp4')
video_cap = cv2.VideoCapture(0) # webcam shomare 1 ro baz mikone , agar bejaye 0 , 1.2 ya 3 bud baghie webcam haro baz mikard


while True:
    ret,frame= video_cap.read() # ma donbale framim , ret ya ture ya false : agar betone frame ro bekhone ret ture agar natone false (mogheie nemitone bekhone ke ya webcam ghat shode ya film tamom shode )
    if ret == False:
        break

    frame = cv2.resize(frame , (0,0), fx=0.5 , fy=0.5)
    frame_gray= cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) #convert color
    faces= face_detector.detectMultiScale(frame_gray,1.3,minSize=(100,100))

    for (x,y,w,h) in faces :
        cv2.rectangle(frame_gray,(x,y),(x+w , y+h),(0,255,0),4)
    
    #cv2.imshow("harchi",frame)
    cv2.imshow("harchi",frame_gray)
    cv2.waitKey(100) #100 mili sanie sabr kon bad boro frame badi
    cv2.waitKey(1) #real time on webcam
