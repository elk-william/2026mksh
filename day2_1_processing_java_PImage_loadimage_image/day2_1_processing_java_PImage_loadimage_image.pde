//day2_1_processing_java_PImage_loadimage_image
size(640,960);//視窗大小640*960
PImage img;//宣告圖片的變數
//上網找圖片，存檔.png，再拉到程式裡
img=loadImage("chang.png");//讀入圖片
image(img,0,0,640,960);//畫出圖片，在(0,0)640*960
