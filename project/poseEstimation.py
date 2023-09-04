import cv2
import mediapipe as mp
import os

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

filePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

cap = cv2.VideoCapture(0)

running = True
while running:
    ret,frame = cap.read()
    if not ret:
        running = False

    rgbFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = pose.process(rgbFrame)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(frame,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
    
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        running = False

cap.release()
cv2.destroyAllWindows()
