//init counter, send it every 500ms, increment counter every 500ms
//when receive reset counter cmd, reset counter

int counter = 0;
unsigned long lastTimeCountSent = millis();
unsigned long countSentDelay = 500;

void setup() {
  Serial.begin(115200);
  while(!Serial) {}
}

void loop() {
  unsigned long timeNow = millis();
  if (timeNow - lastTimeCountSent >= countSentDelay) {
    lastTimeCountSent = timeNow;
    Serial.println(counter);
    counter ++;
    }
  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    if (cmd == "reset") {
      counter = 0;
    }
  }
}
