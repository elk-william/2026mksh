//day7_10a_processing_java_sound_files_do_re_mi_fa_so_keyReleased_mousePressed
int[]a={0, 0, 0, 0, 0};
//int[]b={'do','re','mi','fa','so'};
String [] b = {"do", "re", "mi", "fa", "so"};
import processing.sound.*;//使用processing的Sound外掛
SoundFile sound1, sound2, sound3, sound4, sound5;//五個檔案
void setup() {//設定
  size(500, 100);
  sound1=new SoundFile(this, "do.wav");
  sound2=new SoundFile(this, "re.wav");
  sound3=new SoundFile(this, "mi.wav");
  sound4=new SoundFile(this, "fa.wav");
  sound5=new SoundFile(this, "so.wav");
}
void draw() {
  for (int i=0; i<5; i++) {//迴圈跑五次
    fill(255, 255, 242);//米色
    rect(i*100, 0, 100, 100);//畫格子
    fill(0);//紅色的字
    textSize(80);
    text(b[i], (i*100)+10, 80);
  }//畫出a[i]
  for (int i=0; i<5; i++) {
    if (a[i]==1) fill(128);
    else fill(255);
    rect(i*100, 0, 100, 0);
  }
}
void keyReleased() {
  if (key=='g')a[0]=0;
  if (key=='h')a[1]=0;
  if (key=='j')a[2]=0;
  if (key=='k')a[3]=0;
  if (key=='l')a[4]=0;
}
void keyPressed() {
  if (key=='g') {
    a[0]=1;
    sound1.play();
  }
  if (key=='h') {
    a[1]=1;
    sound2.play();
  }
  if (key=='j') {
    a[2]=1;
    sound3.play();
  }
  if (key=='k') {
    a[3]=1;
    sound4.play();
  }
  if (key=='l') {
    a[4]=1;
    sound5.play();
  }
}
void mousePressed(){
  if (mouseX<100) {
    a[0]=1;
    sound1.play();
  }else  if (mouseX<200) {
    a[1]=1;
    sound2.play();
  }else  if (mouseX<300) {
    a[2]=1;
    sound3.play();
  }else  if (mouseX<400) {
    a[3]=1;
    sound4.play();
  }else  if (mouseX<500) {
    a[4]=1;
    sound5.play();
  } 
}
