//day2_4_processing_java_for_for_array_2D
PImage img;
int [][]a={
 {1,1,1,1,1},
 {1,1,1,1,1},
 {1,1,1,1,1} };
void mousePressed() {
  int i=mouseY/100, j=mouseX/100 ;
  if (mouseButton==LEFT) a[i][j]=0;//左鍵消失
  else a[i][j]=1;//右鍵出現
}
void setup() {
  size(500, 300);
  img= loadImage("cat.jpg");
}
void draw() {
  background(255);
  for (int i=0; i<3; i++) {
    for (int j=0; j<5; j++) {
      if (a[i][j]==1) image(img, j*100, i*100, 100, 100);
    }
  }
}
