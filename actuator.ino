int enablePin = 9;   // Enable pin for the H-bridge
int in1Pin = 8;      // Input 1 pin for the H-bridge
int in2Pin = 7;      // Input 2 pin for the H-bridge

void setup() {
  // Set the motor control pins as outputs
  pinMode(enablePin, OUTPUT);
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  
  // Set the motor control pins to their default state
  digitalWrite(enablePin, HIGH);
  digitalWrite(in1Pin, LOW);
  digitalWrite(in2Pin, LOW);
}

void loop() {
  // Move the actuator forward
  digitalWrite(in1Pin, HIGH);
  digitalWrite(in2Pin, LOW);
  delay(1000);
  
  // Stop the actuator
  digitalWrite(in1Pin, LOW);
  digitalWrite(in2Pin, LOW);
  delay(1000);
  
  // Move the actuator backward
  digitalWrite(in1Pin, LOW);
  digitalWrite(in2Pin, HIGH);
  delay(1000);
  
  // Stop the actuator
  digitalWrite(in1Pin, LOW);
  digitalWrite(in2Pin, LOW);
  delay(1000);
}
