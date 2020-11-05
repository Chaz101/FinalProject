#include "SPI.h"
#include "MFRC522.h"

#define SS_PIN 10
#define RST_PIN 9
#define LED_PIN_B A0 // Blue LED
#define LED_PIN_R A1 // Red LED

MFRC522 rfid(SS_PIN, RST_PIN);

MFRC522::MIFARE_Key key;

void setup() {
  // put your setup code here, to run once:
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  Serial.begin(9600);
  while (!Serial);
  SPI.begin();
  rfid.PCD_Init();
 // Serial.println("I am waiting for card...");
} 

void loop() {
  // put your main code here, to run repeatedly:
  if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial())
    return;
    
  String strID = "";
  for (byte i = 0; i < 4; i++) {
    strID +=
      (rfid.uid.uidByte[i] < 0x10 ? "0" : "") + // https://arduino.stackexchange.com/questions/55455/what-does-this-lines-mean-in-rfid-uid-card-reader-code
      String(rfid.uid.uidByte[i], HEX) +
      (i != 3 ? ":" : "");
  }
  
  strID.toUpperCase();
  Serial.println(strID);
  delay(1000);

  if (Serial.available())
  {
    char state = Serial.read(); // read serial monitor that is written by web database, if it says B, go blue, if R, go red
    if (state == 'B')
    {
      digitalWrite(A0, HIGH);
      delay(2000);
      digitalWrite(A0, LOW);
      return;
    }
    else if (state == 'R')
    {
      digitalWrite(A1, HIGH);
      delay(2000);
      digitalWrite(A1, LOW);  
      return;       
    }
  }
  
}
