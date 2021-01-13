/*
  Group 01



// Global includes
#include <ArduinoJson.h>
#include <Ticker.h>

// wifi comms includes
#include <WiFi.h>
#include <HTTPClient.h>

// BLE Beacon Receiver

#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>


// local includes

// check device MAC table to get wifi password
#define MAN_SSID "Pineapple-2G"
#define MAN_PSWD "paphi2k18"  

// --------------------------------------------------------------------


// --------------------------------------------------------------------

static volatile bool wifiConnected = false;
String localSSID, localPSWD;
String regURL;
String postStr;

static volatile bool tog = false;
static volatile int userCount = 0;
static volatile bool BLEGetTimeout = false;

Ticker ble_scantimer;
const float blescan_period = 2; //seconds

// -------------------------------------------------------

void set_blescan() {
  BLEGetTimeout = true;
}

/*********************** SETUP ******************************/
/*void setup(){

  // configure the i/o
  Serial.begin(115200);

  delay(50);
  Serial.println("DSC190 IoT Web call example");
  
  WiFi.onEvent(WiFiEvent);
  WiFi.mode(WIFI_MODE_STA);

  scanWiFiNetworks();

  localSSID = MAN_SSID;
  localPSWD = MAN_PSWD;
  
  // setup STA mode
  WiFi.mode(WIFI_MODE_STA);
  Serial.println("Trying SSID: " + localSSID + " (" + localPSWD + ")");

  delay(50);
  // connect to the local wifi
  WiFi.begin(localSSID.c_str(), localPSWD.c_str());

  // show MAC address
  Serial.println();
  Serial.println("my MAC:"+getMacStr());

  // wait till we are connected
  while (!wifiConnected)
      ; 
      
  Serial.println("BLE Initialized");
  initBeacon();
  ble_scantimer.attach(blescan_period, set_blescan);

}*/

// ------------------------------ MAIN LOOP --------------------------------
/*void loop(){

String jStr;

    // scan beacons every period
    if (BLEGetTimeout) {
      scanBeacons();
    }

    // check if there is data to look at
    if (haveBeaconData()) {
        jStr =  buildBeaconJson();
        //Serial.println(jStr);
        
    }

    
    String url = "http://dsc-iot.ucsd.edu/api_gid01/API.py";
    String jLoad = "{\"cmd\": \"LOG\", \"gid\": \"01\", \"devmac\":\"" + getMacStr() + "\", " + jStr + "}";
    postJsonHTTP(url, jLoad);
    delay(10000);
    
}*/
