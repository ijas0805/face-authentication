import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle

def pose_angle_verifier(angle, upper_limit, lower_limit):
    if angle <= upper_limit and angle >= lower_limit :
        return True
    return False

def hand_pose_verify(image, goal_count):
  with mp_hands.Hands(
      model_complexity=0,
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5) as hands:
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      image = cv2.flip(image, 1)
      results = hands.process(image)

      # Draw the hand annotations on the image.
      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
      if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
          
          INDEX_FINGER_MCP = [round(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x, 2),round(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y, 2)]
          INDEX_FINGER_PIP = [round(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x, 2),round(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y, 2)]
          INDEX_FINGER_DIP = [round(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x, 2),round(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y, 2)]
          MIDDLE_FINGER_MCP = [round(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x, 2),round(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y, 2)]
          MIDDLE_FINGER_PIP = [round(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x, 2),round(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y, 2)]
          MIDDLE_FINGER_DIP = [round(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x, 2),round(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y, 2)]
          RING_FINGER_MCP = [round(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x, 2),round(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y, 2)]
          RING_FINGER_PIP = [round(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x, 2),round(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y, 2)]
          RING_FINGER_DIP = [round(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x, 2),round(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y, 2)]
          PINKY_MCP = [round(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x, 2),round(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y, 2)]
          PINKY_PIP = [round(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x, 2),round(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y, 2)]
          PINKY_DIP = [round(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x, 2),round(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y, 2)]
          THUMB_TIP = [round(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x, 2),round(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y, 2)]
          THUMB_IP = [round(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x, 2),round(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y, 2)]
          THUMB_MCP = [round(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x, 2),round(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y, 2)]
          
          count = 0
          if pose_angle_verifier(calculate_angle(INDEX_FINGER_MCP, INDEX_FINGER_PIP, INDEX_FINGER_DIP), 180, 150):
            count += 1
          if pose_angle_verifier(calculate_angle(MIDDLE_FINGER_MCP, MIDDLE_FINGER_PIP, MIDDLE_FINGER_DIP), 180, 150):
            count += 1
          if pose_angle_verifier(calculate_angle(RING_FINGER_MCP, RING_FINGER_PIP, RING_FINGER_DIP), 180, 150):
            count += 1
          if pose_angle_verifier(calculate_angle(PINKY_MCP, PINKY_PIP, PINKY_DIP), 180, 150):
            count += 1
          if pose_angle_verifier(calculate_angle(THUMB_TIP, THUMB_IP, THUMB_MCP), 180, 170):
            count += 1

          # mp_drawing.draw_landmarks(
          #     image,
          #     hand_landmarks,
          #     mp_hands.HAND_CONNECTIONS,
          #     mp_drawing_styles.get_default_hand_landmarks_style(),
          #     mp_drawing_styles.get_default_hand_connections_style())
        # msg = f'count is : {count} '
        if goal_count == count:
          return True
        return False
      #   cv2.putText(image, msg, 
      #                   (50, 100), 
      #                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3, cv2.LINE_AA)
      # # Flip the image horizontally for a selfie-view display.
      # cv2.imshow('MediaPipe Hands', image)