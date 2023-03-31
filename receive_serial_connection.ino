int ledPin = 13;  // Pin connected to the LED

void setup() {
  // Initialize the LED pin as an output
  pinMode(ledPin, OUTPUT);
  
  // Start the serial connection
  Serial.begin(9600);
}

void loop() {
  // Check if there's any data available on the serial connection
  if (Serial.available() > 0) {
    // Read the incoming command
    char command = Serial.read();
    
    // Turn the LED on or off based on the command
    if (command == '1') {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED turned on");
    } else if (command == '0') {
      digitalWrite(ledPin, LOW);
      Serial.println("LED turned off");
    }
  }
}
