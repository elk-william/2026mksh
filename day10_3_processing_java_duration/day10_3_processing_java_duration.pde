//day10_3_processing_java_duration
int[]a={0,0};
String []b={"happycat","unknow"};
import processing.sound.*;
SoundFile sound1, sound2;
void setup(){
  size(400,200);
  sound1=new SoundFile(this,"happycat.mp3");
  sound2=new SoundFile(this,"unknow.mp3");
}
void draw(){
  for(int i=0;i<2;i++){
    fill(255,255,242);
    rect(i*200,0,200,100);
    fill(#AAAAAA);
    rect(i*200,100,200,100);
    fill(0);
    textSize(40);
    text(b[i],(i*200)+25,60);
  }     
  drawProgressBar(sound1,0,150,180,15);
  drawProgressBar(sound2,200,150,180,15);
  
}
void mousePressed(){
  if(mouseX<200 && mouseY<100){
    if(a[0]==0){
      a[0]=1;
      sound1.play();
    }else{
      a[0]=0;
      sound1.stop();
    }
  }
  else if(mouseX<400 && mouseY<100){
    if(a[1]==0){
      a[1]=1;
      sound2.play();
    }else{
      a[1]=0;
      sound2.stop();
    }
  }
}
void drawProgressBar(SoundFile sound, float x, float y, float w, float h) {
  float totalDuration = sound.duration();
  float currentPos = sound.position();
  float ratio = currentPos / totalDuration;
  fill(200);
  noStroke();
  rect(x, y, w, h, 5);
  fill(#FF4D4D); 
  rect(x, y, w * ratio, h, 5);
}
