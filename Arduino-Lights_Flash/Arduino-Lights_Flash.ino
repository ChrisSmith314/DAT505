void setup()
{
  Serial.begin(9600);
  pinMode(2,OUTPUT);
}

void loop()
{
  if(Serial.available() > 0) {
    if(Serial.readStringUntil('\n') == "ON"){
      digitalWrite(2, HIGH);
     // Serial.println("Light On");
    } else {
      digitalWrite(2, LOW);
     // Serial.println("Light Off");
    }
    //digitalWrite(1, LOW);
   // String value = Serial.readStringUntil('\n');
   // Serial.println(" Bonjourno Simon ");
  }
}
