#include <WiFi.h>
#include <HardwareSerial.h>
#include <Adafruit_Fingerprint.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

#define RX_PIN 16
#define TX_PIN 17

HardwareSerial mySerial(1);
Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);

WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  mySerial.begin(57600, SERIAL_8N1, RX_PIN, TX_PIN);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("Connected to WiFi with IP: ");
  Serial.println(WiFi.localIP());

  server.begin();
  if (finger.verifyPassword()) {
    Serial.println("Fingerprint sensor not detected");
    while (1);
  }
}

void loop() {
  WiFiClient client = server.available();

  if (client) {
    String request = client.readStringUntil('\r');
    client.flush();

    String response = "Invalid request";

    if (request.indexOf("/verify") != -1) {
      response = verifyFingerprint();
    } else if (request.indexOf("/add") != -1) {
      response = addFingerprint();
    } else if (request.indexOf("/list") != -1) {
      response = listFingerprints();
    } else if (request.indexOf("/serial") != -1) {
      response = readSerialData();
    }

    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/plain");
    client.println("Connection: close");
    client.println();
    client.println(response);
    delay(1);
  }
}

String verifyFingerprint() {
  uint8_t p = finger.getImage();
  if (p != FINGERPRINT_OK) {
    return "Finger not detected";
  }
  p = finger.image2Tz();
  if (p != FINGERPRINT_OK) {
    return "Error processing image";
  }
  p = finger.fingerSearch();
  if (p != FINGERPRINT_OK) {
    return "No match found";
  }
  return "Found ID: " + String(finger.fingerID);
}
