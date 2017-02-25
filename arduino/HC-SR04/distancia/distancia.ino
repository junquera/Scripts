long distancia;
long tiempo;
void setup(){
  Serial.begin(9600);
  pinMode(8, OUTPUT);
  pinMode(9, INPUT); 
}

void loop(){
  digitalWrite(8,LOW);
  delayMicroseconds(5);
  digitalWrite(8, HIGH);
  delayMicroseconds(10);
  tiempo=pulseIn(9, HIGH); 
  distancia= int(0.017*tiempo);
  Serial.print("Distancia ");
  Serial.print(distancia/100.0);
  Serial.println(" m");
  delay(1000);
}
