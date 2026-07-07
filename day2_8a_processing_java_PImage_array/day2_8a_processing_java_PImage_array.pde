//day2_8a_processing_java_PImage_array
//修改自day2_5_processing_java_for_for_array_2d_mousePressed_cat_cat
PImage img,img2;
int [][]a={//陣列的宣告
  {1,1,1,1,1},
  {1,1,1,1,1},
  {1,1,1,1,1} };
void mousePressed(){
  int i=mouseY/100,j=mouseX/100 ;
  a[i][j]=(a[i][j]+1)%3;//取餘數就1 2 3 會變成1 2 0 1 2 0 ...
}
void setup(){
  size(500,300);
  img= loadImage("cat.jpg");
  img2= loadImage("cat2.jpg");
}
void draw(){
  background(255);
  for(int i=0;i<3;i++){
    for(int j=0;j<5;j++){
      if(a[i][j]==1) image(img,j*100,i*100,100,100);
      if(a[i][j]==2) image(img2,j*100,i*100,100,100);
    }
  }
}
