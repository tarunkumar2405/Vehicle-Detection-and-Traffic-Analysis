import cv2
import imutils  # To Resize

cascade_src = 'cars.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)  # Loading XML file

cam = cv2.VideoCapture("http://192.168.1.34:8080/video")  # Initialize Mobile Camera

while True:
    _, img = cam.read()  # Reading frame from the camera
    
    img = imutils.resize(img, width=1000)  # Resizing the frame
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Converting bgr to gray
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)  # Getting Coordinates
    
    # Initialize counts for each direction
    north_count, south_count, east_count, west_count = 0, 0, 0, 0

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Drawing a rectangle
        
        # Check position of detected cars for each direction
        if y < img.shape[0] // 2 and x < img.shape[1] // 2:  # Top-left
            north_count += 1
        elif y >= img.shape[0] // 2 and x < img.shape[1] // 2:  # Bottom-left
            south_count += 1
        elif y < img.shape[0] // 2 and x >= img.shape[1] // 2:  # Top-right
            east_count += 1
        elif y >= img.shape[0] // 2 and x >= img.shape[1] // 2:  # Bottom-right
            west_count += 1

    # Display the frame
    cv2.imshow("Frame", img)

    # Print traffic for all directions
    print("------------------------------------------------")
    print(f"North: {north_count}")
    print(f"South: {south_count}")
    print(f"East: {east_count}")
    print(f"West: {west_count}")
    
    # Example conditions for each direction
    if north_count >= 8:
        print("North More Traffic, Please on the RED Signal")
    else:
        print("North No Traffic")

    if south_count >= 8:
        print("South More Traffic, Please on the RED Signal")
    else:
        print("South No Traffic")

    if east_count >= 8:
        print("East More Traffic, Please on the RED Signal")
    else:
        print("East No Traffic")

    if west_count >= 8:
        print("West More Traffic, Please on the RED Signal")
    else:
        print("West No Traffic")

    if cv2.waitKey(33) == 27:
        break

cam.release()
cv2.destroyAllWindows()
