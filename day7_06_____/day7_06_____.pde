//day7_06_老師做的
void setup(){
  size(500,500,P3D);
}
color [] c = {#FF0000, #00FF00, #0000FF};
void draw() {
  background(0);
  translate(width/2, height/2);
  rotateX(radians(frameCount/2));
  rotateY(radians(frameCount/3));
  beginShape();
  for (int i=0; i<3; i++) {
    float a = radians(frameCount)+i*PI*2/3;
    fill(c[i]);
    vertex(cos(a)*200, sin(a)*200);
  }
  endShape();
}
