//day1_processing_java_eraser_mouseButton_LEFT_RIGHT_stroke_ellipse
void setup(){//設定的函式
  size(500,500);//視窗500*500
  background(255);//白色背景
}
void draw(){//畫圖的函式
  if(mousePressed&&mouseButton==LEFT){//如果mouse按下去
   stroke(0,0,0);//畫黑色的線
    line(mouseX,mouseY,pmouseX,pmouseY);//mouse左鍵按下去
//畫線從mouse座標到pmouse座標
  }
  if(mousePressed&&mouseButton==RIGHT){//mouse右鍵按下去
    noStroke();//不要畫線
    ellipse(mouseX,mouseY,40,40);//20*20的圓，蓋掉畫錯的線
}
}
