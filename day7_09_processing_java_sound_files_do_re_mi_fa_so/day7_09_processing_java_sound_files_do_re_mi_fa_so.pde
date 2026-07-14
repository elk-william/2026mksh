//day7_09_processing_java_sound_files_do_re_mi_fa_so
import processing.sound.*;//使用processing的Sound外掛
SoundFile sound1, sound2, sound3, sound4, sound5;//五個檔案
void setup() {//設定
  size(500,100);
  sound1=new SoundFile(this,"do.wav");
  sound2=new SoundFile(this,"re.wav");
  sound3=new SoundFile(this,"mi.wav");
  sound4=new SoundFile(this,"fa.wav");
  sound5=new SoundFile(this,"so.wav");
     
}
void draw(){
  //...

}
void keyPressed(){
  if(key=='g')sound1.play();
  if(key=='h')sound2.play();
  if(key=='j')sound3.play();
  if(key=='k')sound4.play();
  if(key=='l')sound5.play();
}
