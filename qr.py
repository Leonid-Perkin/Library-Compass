import cv2
cap = cv2.VideoCapture(1)
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
    if bbox is not None:
        bb_pts = bbox.astype(int).reshape(-1, 2)
        num_bb_pts = len(bb_pts)
        for i in range(num_bb_pts):
            cv2.line(img,
                     tuple(bb_pts[i]),
                     tuple(bb_pts[(i+1) % num_bb_pts]),
                     color=(255, 0, 255), thickness=2)
        cv2.putText(img, data,
                    (bb_pts[0][0], bb_pts[0][1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)
        if data:
            print("data found: ", data)
            break