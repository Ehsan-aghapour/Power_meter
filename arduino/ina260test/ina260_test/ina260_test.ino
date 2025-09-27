#include <Adafruit_INA260.h>

Adafruit_INA260 ina260 = Adafruit_INA260();
int SigPin = 13;
bool val = 0;      // variable to store the read value


void setup() {
  Serial.flush();
  pinMode(SigPin, INPUT);  // sets the digital pin 13 as input
  val = digitalRead(SigPin);   // read the input pin
  Serial.begin(115200);
  //Serial.begin(2000000);
  // Wait until serial port is opened
  while (!Serial) { delay(10); }

  Serial.println("Adafruit INA260 Test");

  if (!ina260.begin()) {
    Serial.println("Couldn't find INA260 chip");
    while (1);
  }
  Serial.println("Found INA260 chip");
  delay(10);
  //Serial.read()
}
//int i=1;
//int v[10];
//int m[2];
void loop() {
  Serial.print(digitalRead(SigPin));
  Serial.print(',');
  Serial.print(millis());
  Serial.print(',');
  Serial.println(ina260.readPower());

  /* Delay test
  m[0]=millis();
  v[0]=ina260.readPower();
  

  v[1]=ina260.readPower();
  //m[1]=millis();

  v[2]=ina260.readPower();
  //m[2]=millis();

  v[3]=ina260.readPower();
  //m[3]=millis();

  v[4]=ina260.readPower();
  //m[4]=millis();

  v[5]=ina260.readPower();
  //m[5]=millis();

  v[6]=ina260.readPower();
  //m[6]=millis();

  v[7]=ina260.readPower();
  //m[7]=millis();

  v[8]=ina260.readPower();
  //m[8]=millis();

  v[9]=ina260.readPower();
  m[1]=millis();

  Serial.println(m[0]);
  Serial.println(m[1]);*/
  
  
  /*
  Serial.print(ina260.readPower());
  Serial.print(',');
  Serial.print(i);
  Serial.print(',');
  Serial.print(millis());
  Serial.print(',');
  Serial.println(digitalRead(SigPin));   // read the input pin
  
  if(val!=digitalRead(SigPin)){
    val=!val;
    Serial.println(val); 
  }
  i=i+1;
  */
  //delay(1);
  
}
/*
void loop() {
  Serial.print("Current: ");
  Serial.print(ina260.readCurrent());
  Serial.println();
  //Serial.println(" mA");
  

  Serial.print("Bus Voltage: ");
  Serial.print(ina260.readBusVoltage());
  Serial.println();
  //Serial.println(" mV");
  

  Serial.print("Power: ");
  Serial.print(ina260.readPower());
  Serial.println();
  //Serial.println(" mW");

  //Serial.println();
  delay(1000);
}*/
