int input_arr[9];
int output_arr[8];

void setup() {
  for (int i = 1; i <= 9; i++) {
    pinMode(i, INPUT);
  }

  for (int i = 1; i <= 8; i++) {
    pinMode(i, OUTPUT);
  }
  Serial.begin(9600);
}

void read() {
  for (int i = 1; i <= 9; i++) {
    input_data[i] = digitalRead(i);
  }

  for (int i = 1; i <= 9; i++) {
    Serial.print(input_data[i]);
    if (i < 8) {
      Serial.print(",");
    }
  }
  Serial.println();
  delay(500);
}

void write() {

}

void loop() {
  read();
}
