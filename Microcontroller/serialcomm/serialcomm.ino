void setup() {
  pinMode(1, INPUT);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  pinMode(9, INPUT);
  pinMode(12, INPUT);
  pinMode(13, INPUT);
  pinMode(14, INPUT);
  Serial.begin(9600);
}

void loop() {
  Serial.print(String(digitalRead(1)));
  Serial.print(String(digitalRead(2)));
  Serial.print(String(digitalRead(3)));
  Serial.print(String(digitalRead(4)));
  Serial.print(String(digitalRead(5)));
  Serial.print(String(digitalRead(9)));
  Serial.print(String(digitalRead(12)));
  Serial.print(String(digitalRead(13)));
  Serial.print(String(digitalRead(14)));
  Serial.print("\n");
  delay(10);
}
