#include "SPI.h"
#include "MFRC522.h"

#define SS_PIN 10
#define RST_PIN 9
#define LED_PIN A0 
#define LED_PIN A1

MFRC522 rfid(SS_PIN, RST_PIN);

MFRC522::MIFARE_Key key;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  Serial.println("I am waiting for card...");
}

void loop() {
  // put your main code here, to run repeatedly:
  if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial())
    return;

  Serial.print(F("PICC type: "));
  MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);
  Serial.println(rfid.PICC_GetTypeName(piccType));

  String strID = "";
  for (byte i = 0; i < 4; i++) {
    strID +=
      (rfid.uid.uidByte[i] < 0x10 ? "0" : "") +
      String(rfid.uid.uidByte[i], HEX) +
      (i != 3 ? ":" : "");
  }

  strID.toUpperCase();
  Serial.print("Tap card key: ");
  Serial.println(strID);
  delay(1000);

  if (strID.indexOf("75:34:17:A3") >= 0) {  //put your own tap card key;
    Serial.println("********************");
    Serial.println("**Authorised access**");
    Serial.println("********************");
    digitalWrite(A0, HIGH);
    delay (5000);
    digitalWrite(A0, LOW);
    return;
  }
  else {
    Serial.println("****************");
    Serial.println("**Access denied**");
    Serial.println("****************");
    digitalWrite(A1, HIGH);
    delay (5000);
    digitalWrite(A1, LOW);
    return;
  }
  
}
