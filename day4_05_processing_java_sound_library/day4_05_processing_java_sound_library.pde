//day4_05_processing_java_sound_library
import processing.sound.*;//使用sound外掛
void setup(){//設定的函式
  size(400,400);//視窗大小
  //記得，把你的sound_files目錄裡的music.mp3拉到程式裡
  SoundFile music=new SoundFile(this, "music.mp3");
  music.play();//播放
}
void draw(){
  background(255,255,242);
}
