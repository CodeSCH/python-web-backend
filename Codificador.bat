@echo off
set /p nombre=Ingrese su nombre:
echo %nombre%
cd C:\Users\j_seb\Desktop\BACKEND\face_recognition_and_liveness\face_recognition
python encode_faces.py -i dataset\%nombre% -e encoded_faces.pickle -d cnn
exit


