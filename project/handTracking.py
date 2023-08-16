import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

hand = mp.solutions.hands
hands = hand.Hands()
draw = mp.solutions.drawing_utils

prevTime = 0
currTime = 0

running = True
while running:
    ret,frame = cap.read()
    if not ret:
        running = False

    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for each in results.multi_hand_landmarks:
            for id,lm in enumerate(each.landmark):
                height,width,channels = frame.shape
                cx,cy = int(lm.x*width),int(lm.y*height)
                print(id,cx,cy)
                if id == 0:
                    cv2.circle(frame,(cx,cy),15,(255,0,255),-1)

            draw.draw_landmarks(frame,each,hand.HAND_CONNECTIONS)

    currTime = time.time()
    fps = 1/(currTime-prevTime)
    prevTime = currTime

    cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,3,(0,255,0),3)

    cv2.imshow("Live",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        running = False

cap.release()
cv2.destroyAllWindows()

