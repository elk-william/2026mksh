//day1_processing_java_painter_mouseX_mouseY_pmousseX_pmouseY
//簡單的小家(Painter)
void setup(){//設定的函式
  size(500,500);//視窗500*500
}
void draw(){//畫圖的函式
  if(mousePressed)//如果mouse按下去
    line(mouseX,mouseY,pmouseX,pmouseY);
//畫線從mouse座標到pmouse座標
}
