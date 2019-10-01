#include "DHT.h"

DHT dht;

void setup()
{
  Serial.begin(9600);

  dht.setup(8); // data pin 8
}

void loop()
{
  delay(dht.getMinimumSamplingPeriod());
  Serial.print("Humidity is ");
  Serial.print(dht.getHumidity());
  Serial.print("\n");
  Serial.print("Temperature is ");
  Serial.print(dht.getTemperature());
  Serial.print("\n");
}
 
