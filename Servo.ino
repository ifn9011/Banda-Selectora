 // Incluímos la librería para poder controlar el servo
#include <Servo.h>
 
// Declaramos la variable para controlar el servo
Servo servoMotor;
Servo servo2;
char option = ' ';
 
void setup() {

  Serial.begin(9600);
  servoMotor.attach(7);
  servoMotor.write(150);
  servo2.attach(8);
  servo2.write(150);
}
 
void loop() {

  if(Serial.available() != 0){
    option = Serial.read();
    //Serial.println(option);
    if(option == 'a'){
      delay(800);
      servoMotor.write(0);  
    }
    else if(option == 'v'){
      delay(1400);
      servo2.write(0);
    }
    if(option == 'n'){
      delay(750);
      servoMotor.write(150);
    }
    else if(option == 'i'){
      delay(750);
      servo2.write(150);
    }
    Serial.flush();
    /*if(option == 'b'){
      servoMotor.write(150);
      delay(5000);
      Serial.println("Ya");
  }*/
}
}
