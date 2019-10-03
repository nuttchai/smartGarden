#include "DHT.h"
DHT dht;

int sensorPin = A0;
int outputRead;
int output_value;
String inputString = "";
bool stringComplete = false; 

volatile int data; 


int flag;

void setup() 
{
  Serial.begin(115200);
  inputString.reserve(200); // reserve 200 bytes for the inputString
  dht.setup(8); // data pin 8.
}

void loop() { 
  
  if (inputString == "t") {
    //delay(dht.getMinimumSamplingPeriod());
    Serial.print("Temperature: ");
    Serial.print(dht.getTemperature());
    Serial.println("C");
  }
  
  else if (inputString == "h") {
    
    outputRead = analogRead(sensorPin);
    output_value = map(outputRead,550,0,50,100);

  
    Serial.print("Moisture: ");
    Serial.print(output_value);
    Serial.println("%");
  }
  
  inputString = "";
  }


void serialEvent(){
  
  while (Serial.available()) 
  {
    char inChar = (char)Serial.read();
    inputString += inChar;


//    if (inChar == "\n") {
//      stringComplete = true;
//    }
  
  }
  
}

