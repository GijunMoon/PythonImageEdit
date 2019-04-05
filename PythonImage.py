from PIL import Image #pillow라이브러리 (설치필수)
 
# 이미지 열기
img = Image.open('python.png')
#이미지 사이즈 출력
print(img.size)
 #1. jpg로 저장
img.save('python_edit.jpg')
#----------------------------
#썸네일과 같은 작은 사이즈의 이미지
size = (32, 32)
img.thumbnail(size)  
#저장
img.save('python_thumb_edit.jpg')
#-----------------------------
#이미지를 원하는 사이즈로 크롭 (부분 크롭)
Crop = img.crop((50, 50, 100, 120))
Crop.save('python_crop_edit.jpg')
#-----------------------------
#이미지를 리사이즈 (축소 or 확대)
Resize = img.resize((100, 100))
Resize.save('python_resize_edit.jpg')
 #----------------------------
# 이미지 회전 (125도)
Rotate = img.rotate(125)
Rotate.save('python_rotate_edit.jpg')