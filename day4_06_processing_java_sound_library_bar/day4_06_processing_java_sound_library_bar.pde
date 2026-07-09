//day4_06_processing_java_sound_library_bar
import processing.sound.*;//使用sound外掛
float T;
void setup(){//設定的函式
  size(400,5);//視窗大小
  //記得，把你的sound_files目錄裡的music.mp3拉到程式裡
  SoundFile music=new SoundFile(this, "minecraft.mp3");
  music.play();//播放
  T=music.duration();
}
void draw(){
  background(128);
  fill(0);
  rect(0,0,400*(frameCount/60.0000)/T,50);
}
