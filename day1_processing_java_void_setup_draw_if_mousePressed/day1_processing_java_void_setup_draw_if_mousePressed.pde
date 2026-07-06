//day1_processing_java_void_setup_draw_if_mousePressed
//互動的版本
void setup(){//設定的函式
  size(500,500);//視窗大小
}
void draw(){
  //如果 mouse按下去，就將背景設成紅色
  if(mousePressed) background(255,0,0);//紅色
  else background(0,255,0);//綠色
  //否則(沒有按下去)，就將背景設成綠色


}
