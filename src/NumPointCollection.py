import os
import cv2
import mediapipe as mp
import sys
import pickle

# تعطيل رسائل TensorFlow
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# تغيير ترميز الإخراج إلى UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# تهيئة MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
# مسار المجلد الرئيسي
DATA_DIR = 'D:\\img_num'
data = []
labels = []
for dir_ in os.listdir(DATA_DIR):
    # i=0
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
      print('lables: ')
      print(dir_)
      print(', photo: ')
      print(img_path)
      # if(i==4000):
      #   break
      data_aux=[]
      x_ = []
      y_ = []
      img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
      img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      results = hands.process(img_rgb)
      if results.multi_hand_landmarks:
          for hand_landmarks in results.multi_hand_landmarks:
              for i in range(len(hand_landmarks.landmark)):
                x=hand_landmarks.landmark[i].x
                y=hand_landmarks.landmark[i].y
                x_.append(x)
                y_.append(y)
              for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))
  
          data.append(data_aux)
          labels.append(dir_)
         # print(f"data:{data}, label:{labels}")
      i=i+1
# print(data)
f = open('D:\\img_num\\data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()
