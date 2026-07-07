//day2_3_processing_java_for_for_image_x_y
//練習用for迴圈
PImage img;
void setup(){
  size(900,500);   
  img=loadImage("cat.jpg");
}//要記得把cat.png圖檔拉進程式裡
void draw(){
  background(255);
  for(int y=0;y<500;y+=100){//左手i對應y
    for(int x=0;x<900;x+=100){//右手j對應x
      image(img,x,y,100,100);
    }//要小心X座標是j，Y座標是i
  }
}
