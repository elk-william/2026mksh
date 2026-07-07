//day2_2_processing_java_void_steup_void_draw_image
PImage img;
void setup(){//設定的函式
  size(500,300);
  img=loadImage("cat.jpg");//要拉入圖片
  imageMode(CENTER);//圖片的座標設在正中心
}
void draw(){//畫圖的函式
  background(255);//白色背景
  image(img,mouseX,mouseY,100,100);//秀圖片，放在mouse座標
}
