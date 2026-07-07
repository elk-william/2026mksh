//day2_7a_processing_java_PImage_for
PImage img;
void setup(){
  size(500,100);
  img= loadImage("cat.jpg");
}
void draw(){
  for(int x=0;x<500;x+=100)
  image(img,x,0,100,100);
}
