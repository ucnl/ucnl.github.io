
[Main](/) ❯ [Educational projects](/educational_projects_en) ❯ **ACubes: User's manual**

<details>
  <summary><b>ℹ Recommendations for printing / saving as PDF</b></summary>
  <br>
  <ol>
    <li>Press <b>Ctrl+P</b> (macOS: <b>Cmd+P</b>)</li>
    <li>Select <b>"Save as PDF"</b> (Microsoft Print to PDF) as the printer</li>
    <li>In <b>"Pages"</b>, enter a range that excludes the first and the last page</li>
    <li>Disable <b>headers and footers</b> (title, URL, page numbers)</li>
    <li>In <b>Chrome/Edge</b>: More settings → "Margins" → <b>None</b> | in <b>Firefox</b>: "Margins & Header/Footer" → <b>None</b></li>
    <li>Click <b>Print</b> and choose where to save the PDF</li>
  </ol>
</details>

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![image](https://github.com/user-attachments/assets/f9be473c-561b-4536-8c0b-7ab44e6598aa) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **A<sup>3</sup>S** **ACubes** <br/> User's manual |


# **A<sup>3</sup>S** device family <br/> User's manual

<div style="page-break-after: always;"></div>

## Contents

* [0. Who is this box of cubes for, and why?](#0-who-is-this-box-of-cubes-for-and-why)
* [1. A³T and A³R](#1-a3t-and-a3r)
  * [Transmitter A³T](#transmitter-a3t)
  * [Receiver A³R](#receiver-a3r)
  * [Operating principles](#operating-principles)
  * [Scaling options](#scaling-options)
  * [1.1. About underwater acoustic transducers](#11-about-underwater-acoustic-transducers)
    * [Choosing transducers](#choosing-transducers)
    * [Dedicated receiving transducers](#dedicated-receiving-transducers)
    * [Transceiving transducers](#transceiving-transducers)
    * [Operating rules](#operating-rules)
  * [1.2. Project 1 - Transmitting and receiving](#12-project-1---transmitting-and-receiving)
    * [1.2.1. Required equipment](#121-required-equipment)
    * [Connecting the transducers](#connecting-the-transducers)
    * [1.2.2. Transmitter setup](#122-transmitter-setup)
    * [1.2.3. Receiver setup](#123-receiver-setup)
    * [1.2.4. Testing the system](#124-testing-the-system)
  * [1.3. A brief look at multipath propagation and lockout intervals](#13-a-brief-look-at-multipath-propagation-and-lockout-intervals)
    * [1.3.1. The nature of multipath propagation](#131-the-nature-of-multipath-propagation)
    * [1.3.2. Problems caused by multipath propagation](#132-problems-caused-by-multipath-propagation)
    * [1.3.3. Mitigation methods (using ACubes as an example)](#133-mitigation-methods-using-acubes-as-an-example)
  * [1.4. Project 2 - Assembling a transceiver and measuring slant range](#14-project-2---assembling-a-transceiver-and-measuring-slant-range)
    * [1.4.1. Required equipment](#141-required-equipment)
    * [1.4.2. Interrogating device](#142-interrogating-device)
      * [1.4.2.1. Sketch - Initiating transmission and measuring the time between request and response](#1421-sketch---initiating-transmission-and-measuring-the-time-between-request-and-response)
    * [1.4.3. Responder-beacon. Option 1 - without Arduino](#143-responder-beacon-option-1---without-arduino)
    * [1.4.4. Responder-beacon. Option 2 - with Arduino and a fixed delay](#144-responder-beacon-option-2---with-arduino-and-a-fixed-delay)
      * [1.4.4.1. Sketch - Fixed response delay](#1441-sketch---fixed-response-delay)
    * [1.4.5. Experiments](#145-experiments)
      * [1.4.5.1. On the bench](#1451-on-the-bench)
      * [1.4.5.2. In a basin](#1452-in-a-basin)
      * [1.4.5.3. Swimming pool](#1453-swimming-pool)
      * [1.4.5.4. Body of water](#1454-body-of-water)
  * [1.5. Project 3 - Underwater acoustic modem](#15-project-3---underwater-acoustic-modem)
    * [1.5.1. Required equipment](#151-required-equipment)
    * [1.5.2. Connection](#152-connection)
    * [1.5.3. Modem sketch](#153-modem-sketch)
  * [1.6. Project 4 - Transducer array: measuring the angle of arrival](#16-project-4---transducer-array-measuring-the-angle-of-arrival)
    * [1.6.1. Required equipment](#161-required-equipment)
    * [1.6.2. Pinger](#162-pinger)
    * [1.6.3. Receiver](#163-receiver)
      * [1.6.3.1. Sketch for transducer array processing](#1631-sketch-for-transducer-array-processing)
    * [1.6.4. Experiment to determine the spread of arrival times](#164-experiment-to-determine-the-spread-of-arrival-times)
    * [1.6.5. Transducer array](#165-transducer-array)
    * [1.6.6. Swimming pool experiment](#166-swimming-pool-experiment)
    * [1.6.7. Processing the experimental results](#167-processing-the-experimental-results)

  * [1.7. (Planned) Project 5 - Positioning a responder using a virtual long baseline](#17-in-progress-project-5---positioning-a-responder-using-a-virtual-long-baseline)
    * [1.7.1. (Planned) Required equipment](#171-required-equipment)
  * [1.8. (Planned) Project 6 - Long baseline navigation system](#18-planned-project-6---long-baseline-navigation-system)
    * [1.8.1. (Planned) Required equipment](#181-planned-required-equipment)
    * [1.8.2. (Planned) Navigation receiver buoy](#182-planned-navigation-receiver-buoy)
* [2. (Planned) A<sup>3</sup>TC and A<sup>3</sup>RC](#2-planned-a3tc-and-a3rc)
* [3. (Planned) A<sup>3</sup>T2 and A<sup>3</sup>R2](#3-planned-a3t2-and-a3r2)
* [4. (Planned) A<sup>3</sup>AM](#4-planned-a3am)



<div style="page-break-after: always;"></div>

## 0. Who is this box of cubes for, and why?
ACubes was conceived primarily for use in education and engineering training.

A³S (or ACubes, "Acoustic Cubes") is a construction kit, a set of basic functional elements that can be used to build prototypes of almost any type of underwater acoustic navigation or communication system:

- simple digital data transmission systems — underwater acoustic modems;
- wireless voice transmission systems;
- phased arrays and, based on them, ultra-short baseline (USBL) navigation systems with responder-beacons;
- long baseline, short baseline and synthetic baseline systems;
- remote control systems;
- network monitoring systems.

The "cubes" handle the conversion of digital signals into underwater acoustic signals and back, allowing the user to focus on practical tasks: developing original navigation algorithms, error-correcting coding algorithms, network protocols and interaction schemes.

These purposes generally require neither extreme miniaturization, nor high power, nor record-breaking range — what matters is simplicity, reliability and affordability. These are the principles on which we based this line of devices.

We deliberately leave the list of "cubes" open-ended, as it was intended to be expandable from the outset. It will grow according to application scenarios — for example, assembling a transducer array or a transceiver for measuring slant range.

<div style="page-break-after: always;"></div>

## 1. A<sup>3</sup>T and A<sup>3</sup>R
These are a single-channel (single-frequency) pulse transmitter and a single-frequency receiver.

### Transmitter A<sup>3</sup>T
The [A³T](A3T_Datasheet_en.md) transmitter emits pulses of a fixed frequency and duration when the state of its user-controlled digital input changes.

### Receiver A<sup>3</sup>R
The [A³R](A3R_Datasheet_en.md) receiver can detect these pulses and convey information to the user by changing the state of its digital output.

### Operating principles
These two devices are designed to be stacked and share a single transceiving transducer, for example, the [RT-1.332820-1](https://docs.unavlab.com/documentation/EN/Transducers/RT_1_332820_1_Specification_en.html). This configuration forms a transceiver.

Connecting the receiver output to the transmitter input produces a responder-beacon: the received signal is passed immediately to the transmitter input, causing it to emit a response acoustic signal. The whole assembly works on the "echo" principle. This arrangement allows measurement of, for example, the round-trip signal propagation time between the interrogating device and the responder-beacon, and therefore the slant range.

### Scaling options
The connectors mounted along the long edges of the boards form a bus that allows one transmitter and up to 12 receivers to be combined. The outputs of all receivers are then available on the free connector.

This makes it possible to build and study various transducer array configurations. If a 12-element array is insufficient, any number of stacks can be used, each containing up to 12 [A³R](A3R_Datasheet_en.md) modules.

A dedicated [A³R-CB2]() backplane is available for conveniently combining up to 24 receivers. Naturally, any number of these boards can be used.

### 1.1. About underwater acoustic transducers

Two types of transducers are available for use with **A³S** modules:
1. **Transceiving** - compatible with both [A³R](A3R_Datasheet_en.md) and [A³T](A3T_Datasheet_en.md) modules
2. **Receiving** - intended exclusively for use with [A³R](A3R_Datasheet_en.md) modules

#### Choosing transducers
For receive-only operation, receiving transducers are recommended because they:
- cost less
- are smaller and lighter

#### Dedicated receiving transducers
[R-1.d3505-1](/documentation/EN/Transducers/R_1.d3505_1_Specification_en) series transducers:
- are designed specifically for A³R modules
- have dedicated mounts
- are optimal for building transducer arrays for multichannel reception

| <img src="https://github.com/user-attachments/assets/850006dd-7430-472e-9dc8-82bf3dfe48e2" width="480" /> |
| :---: |
| _The transducers are designed to be easily joined together_ |

#### Transceiving transducers
Underwater Communication & Navigation Laboratory offers several models:

| Model | Characteristics |
|--------|----------------|
| [RT-1.332820-1](/documentation/EN/Transducers/RT_1_332820_1_Specification_en.html) | The most affordable and compact solution |
| [RT-2.332820-1](/documentation/EN/Transducers/RT_2_332820_1_specification_en.html) | Suspended transducer for surface equipment (2 piezoelectric elements) |
| [RT-1.524525-1](/documentation/EN/Transducers/RT-1.524525-1_specification_en.html) | Model with enhanced sensitivity |

#### Operating rules
1. **Mechanical protection**:
   - Avoid impact loads
   - Avoid uneven loading
   - Transducers with a mounting groove must be secured only by that groove
   - Do not obstruct the active surface of the transducer

2. **Electrical safety**:
   - Discharge any accumulated charge before connecting (short the terminals)

3. **Care and maintenance**:
   - Do not use aggressive solvents (acetone, isopropanol)
   - Handle polyurethane coatings with particular care

When these rules are followed, the transducers are durable and easy to maintain.

### 1.2. Project 1 - Transmitting and receiving
The simplest scenario, using one receiver and one transmitter.

#### 1.2.1. Required equipment

| No. | Name | Quantity | Note |
|---|--------------|------------|------------|
| 1 | Module [A³R](A3R_Datasheet_en.md) | 1 | |
| 2 | Module [A³T](A3T_Datasheet_en.md) | 1 | |
| 3 | Receiving transducer [R-1.d3505-1](/documentation/EN/Transducers/R_1.d3505_1_Specification_en) | 1 | |
| 4 | Transceiving transducer [RT-1.332820-1](/documentation/EN/Transducers/RT_1_332820_1_Specification_en) | 1 | |
| 5 | Microcontroller board (for example, Arduino Nano) | 2 | Can be replaced with a button to trigger transmission |
| 6 | Dupont Female-Female or Male-Female wires, 25+ cm | 4 | |

#### Connecting the transducers
1. Connect the [R-1.d3505-1](/documentation/EN/Transducers/R_1.d3505_1_Specification_en) receiving transducer to the [A³R](A3R_Datasheet_en.md) module:

| <img src="https://github.com/user-attachments/assets/bf67aad3-81d2-4186-aa74-c13dac7334d2" width="480"  /> |
| :---: |
| _Connecting the receiving transducer_ |

2. Connect the [RT-1.332820-1](/documentation/EN/Transducers/RT_1_332820_1_Specification_en) transceiving transducer to the [A³T](A3T_Datasheet_en.md) module:

| <img src="https://github.com/user-attachments/assets/899591f9-cf9d-46a4-bc6c-e9853faeea05" width="480" /> |
| :---: |
| _Connecting the transceiving transducer_ |

#### 1.2.2. Transmitter setup

##### Operating principle:
- Transmission is triggered by changing the logic level on pin 4 (connector XS2)
- Switch the pin from HIGH to LOW
- To do this, connect pin 4 to any odd-numbered GND pin on the same connector

##### Wiring diagram for Arduino Nano:

| Pin on XS2 | Pin on Arduino Nano |
|----------------|-------------------------|
| 1 (GND) | GND |
| 4 (Transmission trigger) | 10 (D10) |

##### Transmit sketch (1 pulse per second):

```c
#define TX_PIN 10      // Transmission trigger pin
#define LED_PIN 13     // Indicator LED

void setup() {
  pinMode(TX_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(TX_PIN, HIGH); // Initial state
}

void loop() {
  digitalWrite(TX_PIN, LOW);  // Start of transmission
  digitalWrite(LED_PIN, HIGH);
  delay(10);                 // Pulse duration 10 ms
  
  digitalWrite(TX_PIN, HIGH); // End of transmission
  digitalWrite(LED_PIN, LOW);
  delay(990);                // Total period 1 second
}
```

*Note: the minimum interval between transmissions is 40 ms*

#### 1.2.3. Receiver setup

##### Operating principle:
- When a signal is detected, the module switches pin 1 (XS3) to LOW for 2 ms
- An Arduino or an oscilloscope can be used for detection

##### Wiring diagram for Arduino Nano:

| Pin on XS3 | Pin on Arduino Nano |
|----------------|-------------------------|
| 2 (GND) | GND |
| 1 (Receive strobe) | 2 (D2) |

##### Receive sketch:

```c
#define RX_PIN 2       // Reception detection pin
#define LED_PIN 13     // Indicator LED

void setup() {
  pinMode(RX_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(RX_PIN), rxDetected, FALLING);
}

void rxDetected() {
  digitalWrite(LED_PIN, HIGH);
  delay(100);         // LED stays on for 100 ms upon reception
  digitalWrite(LED_PIN, LOW);
}

void loop() {
  // No main loop is needed
}
```

#### 1.2.4. Testing the system

1. **In air**:
   - Place the transducers 10–15 cm apart
   - If transmission is successful, the LEDs on both Arduino boards will blink in sync

2. **In water**:
   - Submerge the transducers at least 1 meter below the surface
   - Avoid air bubbles near the active surfaces of the transducers

| <img src="https://github.com/user-attachments/assets/76dd271a-f87e-45c2-bbad-dad94bc4ccd2" width="480" /> |
| :---: |
| _Laboratory setup_ |

### 1.3. A brief look at multipath propagation and lockout intervals

Multipath propagation and methods of mitigating it are an extensive field of research. This section covers only the basic principles.

#### 1.3.1. The nature of multipath propagation

Multipath propagation can be compared to an acoustic echo. A sound signal propagates from its source as a spherical wavefront, with:

1. **Direct path** - the shortest path from the source to the receiver
2. **Reflected paths** - signals reflected from:
   - The bottom of the body of water
   - The water surface
   - Underwater objects
3. **Refracted paths** - signals whose direction changes because of:
   - Inhomogeneities in the water
   - Changes in the speed of sound at different depths

#### 1.3.2. Problems caused by multipath propagation

1. **Measurement errors**:
   - Incorrect slant range determination

2. **"Echo loop" effect**:
   - Responder-beacon systems may enter an endless "request-response" loop
   - This is especially critical when the same frequency is used for transmission and reception

#### 1.3.3. Mitigation methods (using ACubes as an example)

For simple signaling systems, the most effective solution is a **lockout interval**:

| Parameter | Description |
|----------|----------|
| Operating principle | After detecting a signal, the receiver temporarily stops processing incoming signals |
| Duration | Determined experimentally for the specific conditions |
| Influencing factors | Depth, bottom topography, presence of objects, properties of the water |

**Setup recommendations:**
1. Start with an interval of 50–100 ms for small bodies of water
2. Gradually increase the interval until false detections disappear
3. Accurate measurements may require static error calibration

*Note: professional systems use more sophisticated methods (separate frequencies, signal coding, adaptive algorithms), but these are beyond the scope of this manual.*

### 1.4. Project 2 - Assembling a transceiver and measuring slant range

In this project, we will assemble two transceivers: one will act as a responder-beacon, while the other will emit a request signal, wait for a response and determine the slant range between the subscribers from the signal propagation time and the speed of sound.

#### 1.4.1. Required equipment

| No.    | Name | Quantity | Note |
| :--- | :--- | :--- | :--- |
| 1    | Module [A<sup>3</sup>R](A3R_Datasheet_en.md) | 2 |  |
| 2    | Module [A<sup>3</sup>T](A3T_Datasheet_en.md) | 2 |  |
| 3    | Transceiving transducer [RT-1.332820-1](/documentation/EN/Transducers/RT_1_332820_1_Specification_en) | 2 |  |
| 4    | Any microcontroller board, for example, Arduino Nano | 2 |  |
| 5    | LCD display, for example MT-204S | 1 | For displaying the measured time and range; these can also be output to the COM port |
| 6    | Dupont Female-Female or Male-Female wires, 25+ cm | 15 | |

This scenario actually includes at least two different subscenarios:  
The **first** involves installing jumper **P0** on the responder-beacon so that the receiver output is connected to the transmitter input. The responder-beacon will then emit a response signal with zero delay. This may seem the most convenient and simplest arrangement, but it imposes certain limitations. The receiver modules have a so-called lockout interval that determines how long after reception the next reception is possible. This means the system has a minimum range below which distances cannot be measured: when a response signal arrives from a distance below this minimum, the receiver will still be waiting for the lockout interval to end and will be unresponsive.

In the **second** subscenario, we introduce a fixed delay between receiving the request signal and emitting the response. This delay is known to the interrogating device and can easily be accounted for. Although this arrangement is more complex, it allows distances down to almost zero to be measured. The most convenient way to generate this delay is to use a microcontroller, such as an Arduino.

Let us start with the interrogating device. Again, we have prepared two options of different complexity: with a display, or without one, sending the necessary information over UART.

#### 1.4.2. Interrogating device
First, assemble a "sandwich" of A<sup>3</sup>R and A<sup>3</sup>T modules. Set the receiver bus address by installing jumper P1. This places all connections to the Arduino board on connector XS2. Solder the transducer braid and negative lead together. Connect the receiver and transmitter boards with short wire jumpers through their XS1 connectors.

| <img src="https://github.com/user-attachments/assets/c9a55a56-d37e-4aa6-8229-81f800377083" width="480" /> |
| :---: |
| _Connecting a shared transducer to the receiver and transmitter modules_ |

Next, connect the cube assembly to the Arduino board. This requires 4 male-female wires.

| <img src="https://github.com/user-attachments/assets/af9ca034-c4bb-451c-ab49-99c504a420cf" width="480" />  |
| :---: |
| _Connecting the "sandwich" to the Arduino Nano board_ |

| Pin number/name on XS2 | Pin number/name on Arduino Nano |
| :--- | :--- |
| 1 / GND  | GND |
| 2 / Transmission start strobe | 3 / INT1 |
| 4 / Pulse transmission trigger | 10 |
| 6 / Receiver No. 1 strobe | 2 / INT0 |

If you plan to use a MELT MT-20S4S LCD display or a compatible one, connect the pins as follows:

| Pin number on the display | Pin number/name on Arduino Nano|
| :--- | :--- |
| 1 | GND |
| 2 | 5V |
| 4 | 8 (D8) |
| 5 | 9 (D9) |
| 10 | 4 (D4) |
| 11 | 5 (D5) |
| 12 | 6 (D6) |
| 13 | 7 (D7) |

In addition, connect pins 1 and 5, pins 2 and 18, and pins 2 and 3 on the display board. The resistance between pins 2 and 3 sets the display contrast, and simply shorting them may not be sufficient in some cases.

The sketch for the Arduino control board is shown below:

##### 1.4.2.1. Sketch - Initiating transmission and measuring the time between request and response
If you do not plan to use a display, comment out the line `#define USE_LCD`. The speed of sound is set to a constant of 1500.0; for a more accurate value, use our online speed of sound in water calculator: [Proper speed of sound in water calculator](https://docs.unavlab.com/online_utils/proper_speed_of_sound_calculator.html)

```c
#define USE_LCD

#ifdef USE_LCD
#include "LiquidCrystal.h"
LiquidCrystal lcd(8, 9, 4, 5, 6, 7); // RS, E, D4-D7
#define X_MAX              (20) // Number of characters per display line
#define MSG_LINE           (3)  // Message line number
#define W_LINE             (0)  // Line number for displaying progress
#endif

// Pin assignments
#define TX_CONTROL_PIN     10   // Transmitter control pin (active HIGH)
#define TX_STROBE_PIN      3    // Transmitter strobe pin (expecting FALLING edge)
#define RX_STROBE_PIN      2    // Receiver strobe pin (expecting FALLING edge)

// System parameters
#define ANSWER_DELAY_MS    500    // Fixed beacon response delay [ms]
#define SOS_MPS            1500   // Speed of sound in water [m/s]
#define MAX_DISTANCE_M     500    // Maximum measured range [m]
#define PULSE_WIDTH_MS     10     // Control pulse duration [ms]

#define PAUSE_MS           (1000) // Pause between measurements
#define TIMEOUT            (2 * 1000000L * MAX_DISTANCE_M / SOS_MPS + ANSWER_DELAY_MS * 1000L)

#ifdef USE_LCD
#define TKS_PER_CHAR       ((TIMEOUT - ANSWER_DELAY_MS * 1000L) / X_MAX)
#endif


// Global variables
volatile uint32_t tor = 0;  // Signal emission time
volatile uint32_t toa = 0;   // Response signal reception time
volatile bool rx_strobe = false; // Strobe received flag

// Transmitter strobe interrupt handler
void txStrobeISR() {
  tor = micros();
}

// Receiver strobe interrupt handler
void rxStrobeISR() {
  toa = micros();
  rx_strobe = true;
}

void setup() {
  
#ifdef USE_LCD
  lcd.begin(20, 4);
  lcd.clear();
  lcd.print(F("Starting..."));  
#endif

  Serial.begin(9600);
  Serial.println(F("Starting..."));
  
  // Pin setup
  pinMode(TX_CONTROL_PIN, OUTPUT);
  digitalWrite(TX_CONTROL_PIN, HIGH);
 
  pinMode(TX_STROBE_PIN, INPUT);
  pinMode(RX_STROBE_PIN, INPUT);

  // Interrupt setup
  attachInterrupt(digitalPinToInterrupt(TX_STROBE_PIN), txStrobeISR, FALLING);
  attachInterrupt(digitalPinToInterrupt(RX_STROBE_PIN), rxStrobeISR, FALLING);

  delay(1000);
}

void loop() {

#ifdef USE_LCD
  lcd.setCursor(0, W_LINE);
  lcd.print("                    ");
#endif

  // 0. Reset
  tor = 0;

  // 1. Initiate transmission
  digitalWrite(TX_CONTROL_PIN, LOW);
  
  // 2. Wait for the transmitter strobe (the interrupt will set tor)
  while (tor == 0) {
    // Waiting...
  }

  // 3. Restore the transmission control pin state
  digitalWrite(TX_CONTROL_PIN, HIGH);
  
  // 4. Do not process the receiver during the fixed response delay
  delay(ANSWER_DELAY_MS);

  toa = 0;
  rx_strobe = false;

  // 5. Wait for the receiver strobe with a timeout
#ifdef USE_LCD
  int c_idx = 0;
  uint32_t tks = micros();
#endif

  while (!rx_strobe && (micros() - tor < TIMEOUT)) {
    // Waiting...

#ifdef USE_LCD
    
    if ((micros() - tks) >= TKS_PER_CHAR) {
      
      lcd.setCursor(c_idx, W_LINE);
      lcd.print(")");

      if (c_idx < X_MAX) c_idx++;
      tks = micros();
    }
    
#endif
  }
  
  // 6. If a signal was received, calculate the range
  if (rx_strobe) {
    // Handle micros() overflow correctly
    uint32_t tof;
    if (toa > tor) {
      tof = toa - tor;
    } else {
      tof = (0xFFFFFFFF - tor) + toa;
    }
    
    // Subtract the fixed beacon delay and divide by 2 (round trip)
    tof = (tof - ANSWER_DELAY_MS * 1000L) / 2;
    
    // Calculate the range
    float srn = tof * 1e-6 * SOS_MPS;
    
#ifdef USE_LCD
    lcd.setCursor(0, MSG_LINE);
    lcd.print("                    ");
    lcd.setCursor(0, MSG_LINE);
    lcd.print(srn, 1);    
    lcd.print(" m");
#endif

    Serial.println(srn, 1);

  } else {

#ifdef USE_LCD
    lcd.setCursor(0, MSG_LINE);
    lcd.print("      TIMEOUT       ");
#endif

    Serial.println("TIMEOUT");
  }
  
  // Pause between measurements
  delay(1000);
}
```

#### 1.4.3. Responder-beacon. Option 1 - without Arduino

We should say up front that this option is almost never used in practice because of the risk of entering a loop in which the beacon "interrogates itself" with its own response signal.

Here we need to assemble the same "sandwich" as for the interrogating device, with the sole difference that we install jumper **P0**, which connects the receiver output to the transmitter input. The receiver strobe generated upon signal reception becomes the transmission trigger strobe. Also remember to install the jumper that sets the receiver bus address, making its output available on connector XS2.

| <img src="https://github.com/user-attachments/assets/3fc329de-5cd5-4d8a-b8c5-af15bb9d1237" width="480" /> |
| :---: |
| _Jumper P0 connects the receiver output to the transmitter input_ |

Connect the transducer in the same way as for the interrogating device: solder the braid and negative lead together and join the receiver and transmitter XS1 connectors with jumpers.
Note that for both the interrogating device and the responder-beacon, power must be supplied to the transmitter module to prevent substantial currents from flowing through the bus during transmission.

#### 1.4.4. Responder-beacon. Option 2 - with Arduino and a fixed delay
In this case, set `ANSWER_DELAY_MS` to a nonzero value in the interrogating device's Arduino sketch. Both the receiver board and the transmitter board have a lockout interval of 40 ms. Accordingly, the fixed delay you select must exceed this value. In our example, we set it to 500 ms, which is suitable for most small bodies of water with a long "tail" of reflections.

No changes other than the `ANSWER_DELAY_MS` value are needed in the interrogating device sketch. On the responder-beacon, remove jumper **P0** and connect a second Arduino Nano board according to the following table:

| Pin number/name on XS2 | Pin number/name on Arduino Nano |
| :--- | :--- |
| 1 / GND  | GND |
| 4 / Pulse transmission trigger | 10 |
| 6 / Receiver No. 1 strobe | 2 / INT0 |

A simple sketch that waits for signal reception, pauses and emits a response signal could look like this:

##### 1.4.4.1. Sketch - Fixed response delay
  
```c
#define A3R_STATE_PIN     (2)
#define A3T_TX_ENGAGE_PIN (10)
#define LED_PIN           (13)

#define ANSWER_DELAY_MS    (500L) // Fixed response delay at the responder, [ms]
#define DEAD_TIME_MS       (500L) // Lockout interval after transmission

#define TX_STROBE_DURATION_MS  (10L)

void setup() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  pinMode(A3T_TX_ENGAGE_PIN, OUTPUT);
  digitalWrite(A3T_TX_ENGAGE_PIN, HIGH);

  pinMode(A3R_STATE_PIN, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(A3R_STATE_PIN) == LOW) {
    delay(ANSWER_DELAY_MS);
    digitalWrite(A3T_TX_ENGAGE_PIN, LOW);
    digitalWrite(LED_PIN, HIGH);
    delay(TX_STROBE_DURATION_MS);
    digitalWrite(A3T_TX_ENGAGE_PIN, HIGH);
    delay(DEAD_TIME_MS);
    digitalWrite(LED_PIN, LOW);    
  }
}
```

#### 1.4.5. Experiments

##### 1.4.5.1. On the bench
When working with piezoceramic transducers, always keep in mind that they are typically driven at tens to hundreds of volts, at frequencies of kilohertz to tens of kilohertz. This combination can mean that, on the bench or more generally in air, underwater acoustic systems operate electromagnetically rather than acoustically. In actual air tests, we encounter both effects: acoustic and electromagnetic.

Why, then, might we need a bench test, a "bench" test, or even a "bench test"? Besides verifying all connections and confirming that the prototype works as a whole, it makes sense to determine the static error and its statistical parameters. Its causes may vary: clock inaccuracy, hardware limitations, limitations associated with the signal type and processing methods, or perhaps something we forgot or estimated incorrectly, and so on.

For example, our test prototype produces the following propagation times when the transducers are in air and touching each other, i.e., when the actual distance is zero:

| No.  | T<sub>OF</sub>, s |
|---|---|
|1|0.001054|
|2|0.001182|
|3|0.001024|
|4|0.001052|
|5|0.001148|
|6|0.001174|
|7|0.000966|
|8|0.001154|
|9|0.001004|
|10|0.001044|
|11|0.001282|
|12|0.001170|

The mean propagation time over 150 measurements is **0.001096** s, equivalent to a distance of **1.64** m at a speed of sound of 1500 m/s. T<sub>OF</sub> varies from 0.000886 to 0.001308 s, or from 1.33 to 1.96 m, respectively.

The distribution of the static error is interesting: it closely resembles a so-called Gaussian mixture, i.e., a mixture of normal (Gaussian) distributions. Multimodality may indicate that the process follows several different scenarios.

| <img src="https://github.com/user-attachments/assets/e5c24575-9e79-4ffc-ba5a-975b0160dac2" width="480" /> |
| :---: |
| _Multimodality in the static error distribution_ |

> FOR INDEPENDENT STUDY:
> Identifying and eliminating the causes of this static error is an interesting and engaging task, and we cannot deprive the reader of the pleasure of doing it independently.

For simplicity, we will account for the measured static error by subtracting its mean value: introduce `#define MAGIC_STATIC_S    (0.001096253)` and subtract this value when calculating slant range:

```c
    float srn = ((tof * 1e-6) - MAGIC_STATIC_S) * SOS_MPS;
```

To summarize, our "bench" experiments have:
 - confirmed that the system works;
 - revealed a static error and allowed us to examine its distribution a little;
 - compensated for the static error in the simplest way: by subtraction.

We can now move on to experiments in water.

##### 1.4.5.2. In a basin

After debugging the prototype on the bench, you can try any container of water or body of water. You can even start with a plastic bucket, as long as it can hold water and two transducers.

Here, for example, is one possible "laboratory setup". Its transducers are 40 cm apart.

| <img src="https://github.com/user-attachments/assets/7755d3fe-a204-4de5-9fc4-3b5e7d4adb9b" width="480" /> |
| :---: |
| _"Laboratory setup"_ |

The distribution of the measured range now looks somewhat different:

| <img src="https://github.com/user-attachments/assets/f5c483a0-cf5e-4b02-9d85-a20963b448d6" width="480" /> |
| :---: |
| _Distribution of the measured propagation time_ |

The sample size does not allow definite conclusions, but there is a hint of a normal distribution. We suggest that users test this hypothesis themselves by increasing the sample size.
If this hypothesis is confirmed, it will cast the multimodality of the distribution obtained from measurements in air in a somewhat different light.

Converting time to range gives a range for this experiment from effectively zero, -0.08 m, to 2.07 m. The mean and mode are 0.58 m and 0.52 m, respectively.
This differs somewhat from the actual distance of 0.4 m between the transducers, but high accuracy and repeatability should not be expected in such a small volume.

To summarize:
- experiments in a small volume are worthwhile and even allow rough quantitative estimates.

##### 1.4.5.3. Swimming pool

Even a small swimming pool with a volume of ~100 m<sup>3</sup> offers an opportunity for more thorough quantitative evaluation of the prototype equipment.

| <img src="https://github.com/user-attachments/assets/48787fd3-9d36-44a1-bd74-63f6947c40aa" width="480" /> <img src="https://github.com/user-attachments/assets/412a6042-161b-4f3c-a7bf-ee49d5d3244f" width="480" /> |
| :---: |
| _Good agreement between direct and acoustic measurements_ |

The transducers can be placed along the same wall. Clearly, larger pools with a soft polymer lining are more favorable for acoustic experiments.
During the experiments, measurements were taken from 0.8 to 8 meters at fixed intervals of 0.8 m, corresponding to the width of the coping tiles around the pool.

| <img src="https://github.com/user-attachments/assets/e8027ce3-7874-4e0c-9629-c9dac71965a0" width="480" /> |
| :---: |
| _Range measurement result at an actual distance of 8 meters between the transducers_|

The distribution of the measured propagation time, based on 150 measurements, looks like this:

| <img src="https://github.com/user-attachments/assets/571e1107-8c12-44ec-963c-3c8a01af741e" width="480" /> |
| :---: |
| _Presumably bimodal distribution of the measured propagation time. Sample size 150_ |

Again, the distribution appears multimodal, or even bimodal. All measurements fall between 7.8 and 8.9 m, and the mean of 8.2 agrees well with the actual distance of 8 m.

> FOR INDEPENDENT STUDY:
> Note that with a multimodal distribution, discussing the mean of the entire sample is not entirely appropriate. We also suggest that the user explore this issue independently.

To summarize:
- the prototype performed well even in a small (~100 m<sup>3</sup>) pool: measurements correspond to the actual distances, with a sample spread of about 1 m.


##### 1.4.5.4. Body of water

Recall that the maximum practical range of the [A³R](A3R_Datasheet_en.md) and [A³T](A3T_Datasheet_en.md) cubes is 300 m according to the specifications. Naturally, this does not mean that the equipment will achieve its stated performance in any conditions, even the most unfavorable ones; nor does it mean that a previously stable link will suddenly stop working at 301 m.

For example, during a maximum-range test, a transmitter emitting 1 signal per second was placed on an anchored raft, while the receiver was gradually moved away in a rowboat. Noticeable reception interruptions began at a distance of 350–370 meters. The experimental conditions were neither ideal nor very difficult. The body of water was a backwater of the Volga River, about 3 km long and between 400 and 200 meters wide at different locations. It had a sandy bottom, moderate vessel traffic and a substantial amount of metal structures on the bottom.

Experiments with the prototype discussed here were conducted in the same body of water. The responder-beacon was placed on an anchored raft of dense foam, initially about 80 meters from the boat landing, and then moved to a distance of 156 meters. In both cases, the distance was measured with a laser rangefinder.

| <img src="https://github.com/user-attachments/assets/b6e0cfac-675d-47b5-9c78-6c2ca1135ffb" width="480" /> <img src="https://github.com/user-attachments/assets/4342aed6-f203-4b7d-b750-91f8be2b23ff" width="480" /> |
| :---: |
| _Range 80 m. Good agreement between direct and acoustic measurements_ |

| <img src="https://github.com/user-attachments/assets/7892fc1c-cb70-4ec2-b445-5d2ed1002eff" width="480" /> <img src="https://github.com/user-attachments/assets/24f3f6ab-b904-4735-b621-0decf85a8260" width="480" /> |
| :---: |
| _Range 156 m. Good agreement between direct and acoustic measurements_ |

It is useful to record signals during experiments in bodies of water. For example, in these tests, the recording hydrophone was placed very close to the interrogating device's transducer. Below are the recordings and screenshots showing randomly selected fragments containing one "request-response" cycle, for ranges of 80 and 156.

> FOR INDEPENDENT STUDY: Readers who wish to do so can analyze the recordings themselves:

[10-06-2025, Krasnoarmeysky backwater, Volgograd. A³S slant range, 80 m](https://github.com/user-attachments/assets/8c01bb6a-d6d2-4ab9-8276-31cbac882f3e)

[10-06-2025, Krasnoarmeysky backwater, Volgograd. A³S slant range, 156 m](https://github.com/user-attachments/assets/5a3092e3-a290-4727-81cf-9193621417a8)


| <img src="https://github.com/user-attachments/assets/aac68173-1779-454e-aa46-c7b138221c94" width="480" /> |
| :---: |
| _Range 80 m. Recording fragment from the interrogating system's position_ |

| <img src="https://github.com/user-attachments/assets/706ab1b1-e68b-4366-ab5c-3b4ba7a5e06d" width="480" /> |
| :---: |
| _Range 156 m. Recording fragment from the interrogating system's position_ |

First, a recording gives an idea of the acoustic conditions: the presence of noise and its frequency distribution, reverberation duration, etc. Second, it allows the results to be checked.
In these two fragments, the intervals between the leading edges of the request and response signals were 610 and 711 ms, respectively.

Accounting for the fixed response delay of 500 ms, dividing the remainder by two for the round trip, and also accounting for the static error of 1.096 ms determined in [section 1.4.5.1.](#1451-on-the-bench) and the speed of sound of 1500 m/s gives the following slant ranges:

`((0.610-0.500) / 2 - 0.001096) * 1500 = 80.86 m`, and  
`((0.711-0.500) / 2 - 0.001096) * 1500 = 156.6 m`

These agree very well with both the laser rangefinder measurements and the prototype's display.

The reverberation duration, about a quarter of a second, is also noteworthy:

| <img src="https://github.com/user-attachments/assets/3b3d379f-6ee7-4697-bacf-fdecfad4b3ed" width="480" /> |
| :---: |
| _A 4-millisecond signal continues to "wander" around the body of water for another 250 milliseconds_ |

If the fixed delay were shorter than this, the interrogating device could easily mistake its own signal for the responder-beacon's signal.

> FOR INDEPENDENT STUDY:
> As for statistical analysis of the slant range measurements, we suggest that the user carry it out independently. It would be interesting to compare experiments in different bodies of water and under different conditions: the error, the percentage of successful measurements, the effect of the speed of sound, etc.
> For example, under ice conditions it is much easier to keep the interrogating device and responder-beacon stationary and to measure the actual distance between them more accurately.

To summarize:
- the devices proved functional in a real body of water
- checks by three independent methods — a laser rangefinder, the recording and the prototype under test — agreed well with one another

### 1.5. Project 3 - Underwater acoustic modem

There is some confusion surrounding the word "modem", especially when underwater acoustic modems are involved. The term "modem" itself derives from **MODulator** and **DEModulator**. Today it is more commonly understood to mean a device for transmitting and receiving _digital_ data. The poor English translation "sonar modem" is also often encountered. This is, of course, incorrect, since sonar literally means "sound(sonic) navigation and ranging", which refers more to sonar detection or echolocation.

Clearly, we will use the "cubes" to build a very simple device for receiving and transmitting digital data. Our signal manipulation capabilities are severely limited: essentially, all we can control is the instant at which a pulse is transmitted. We will base our transmission protocol on that capability.

The transmitted data will be encoded by the delay between two successive pulses. From the previous experiments, we know that a lockout interval is needed; otherwise, the receiver will keep triggering until all reverberation in the body of water has died away. In [section 1.4.5.4.](#1454-body-of-water), we established experimentally that it takes about 200–250 milliseconds for the signal to decay below the receiver's detection threshold.

Let us start with a minimum interval of 300 milliseconds between two pulses. This means that after receiving the first pulse, the receiver records the time and does not check the line state for 300 milliseconds.
For example, to transmit in 8-bit chunks, we need to choose an interval and divide it into 256 values. Zero corresponds to the minimum delay of 300 ms, and the value 256 to the maximum possible delay. After the second, "stop" pulse, another lockout interval is required, and it is highly desirable for it to differ from the first interval.
The transmitter module specifications also tell us that one pulse lasts 4 milliseconds, so it makes sense to choose a difference between adjacent values greater than 4 ms. In our experiment, we will use 8 ms, twice the pulse duration.

Let us leave the modem algorithm for a moment and check the equipment.

#### 1.5.1. Required equipment

| No.    | Name | Quantity | Note |
| :--- | :--- | :--- | :--- |
| 1    | Module [A<sup>3</sup>R](A3R_Datasheet_en.md) | 2 |  |
| 2    | Module [A<sup>3</sup>T](A3T_Datasheet_en.md) | 2 |  |
| 3    | Transceiving transducer [RT-1.332820-1](/documentation/EN/Transducers/RT_1_332820_1_Specification_en) | 2 |  |
| 4    | Any microcontroller board, for example, Arduino Nano | 2 |  |
| 5    | Dupont Male-Female or Female-Female wires, 15+ cm | 6 | |

As in the previous experiments, power supplies for the "cubes" are also required. A 3S pack of Li-Ion or LiFePO4 batteries makes a convenient power source.
You will also need two PCs, or one PC that can connect to two Arduino boards.
Some terminal software is also needed to send data to the serial port and display data received from it.
For example, the 'Serial monitor' utility in the Arduino IDE is suitable, but using the same PC to connect both modems will make this difficult.
For Windows, you can use our simple [uConsole](https://github.com/ucnl/uConsole/releases/download/1.0/uConsole.zip) utility.

#### 1.5.2. Connection
Since the same capabilities are needed as in the previous experiments, the modem wiring is essentially identical to that of the responder-beacon in [section 1.4.4.](#144-responder-beacon-option-2---with-arduino-and-a-fixed-delay).

For convenience, here is that information again:

| Pin number/name on XS2 | Pin number/name on Arduino Nano |
| :--- | :--- |
| 1 / GND  | GND |
| 4 / Pulse transmission trigger | 10 |
| 6 / Receiver No. 1 strobe | 2 / INT0 |

Our experimental setup looks like this:

| <img src="https://github.com/user-attachments/assets/7b36dc8f-328f-4138-a94d-69edd4b696dd" width="480" /> |
| :---: |
| _Two underwater acoustic modems_ |

#### 1.5.3. Modem sketch

As the code shows, the sketch is not very complicated. We set the zero-value interval to 300 ms, the "postfix" lockout interval after the second pulse to 420 ms, and the spacing between adjacent values to exactly twice the pulse duration: 8 ms.

```c

#define A3R_STATE_PIN          (2)
#define A3T_TX_ENGAGE_PIN      (10)
#define LED_PIN                (13)

#define TX_STROBE_DURATION_MS  (10L)

#define SS_PRE_DEAD_TIME_MS    (300L)
#define SS_POS_DEAD_TIME_MS    (420L)
#define SS_TIME_SLOTS          (256L)
#define SS_TIME_SLOT_MS        (8L)
#define SS_MAX_TIME_MS         (SS_TIME_SLOTS * SS_TIME_SLOT_MS + SS_PRE_DEAD_TIME_MS + TX_STROBE_DURATION_MS)

bool receiving = false;
uint32_t r_str_time = 0;
uint32_t r_stp_time = 0;
float r_byte = 256;

void strobe() {
  digitalWrite(A3T_TX_ENGAGE_PIN, LOW);
  digitalWrite(LED_PIN, HIGH);
  delay(TX_STROBE_DURATION_MS);
  digitalWrite(A3T_TX_ENGAGE_PIN, HIGH);
  digitalWrite(LED_PIN, LOW);
}

void setup() {

  Serial.begin(9600);

  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  pinMode(A3T_TX_ENGAGE_PIN, OUTPUT);
  digitalWrite(A3T_TX_ENGAGE_PIN, HIGH);

  pinMode(A3R_STATE_PIN, INPUT_PULLUP);

}

void loop() {

  while (Serial.available()) {

    receiving = false;
    
    uint8_t b = Serial.read();
    uint32_t ss_time = SS_PRE_DEAD_TIME_MS + SS_TIME_SLOT_MS * b - TX_STROBE_DURATION_MS;

    strobe();
    delay(ss_time);

    strobe();
    delay(SS_POS_DEAD_TIME_MS);
  }

  int r_state = digitalRead(A3R_STATE_PIN);
  if ((r_state == LOW) && !receiving) {

    r_str_time = millis();
    receiving = true;
    delay(SS_PRE_DEAD_TIME_MS);

    bool is_timeout = false;
    while ((digitalRead(A3R_STATE_PIN) != LOW) && (!is_timeout)) {
      is_timeout = millis() - r_str_time > SS_MAX_TIME_MS;
    }

    if (!is_timeout)
    {
      r_stp_time = millis();

      float duration_ms = r_stp_time - r_str_time - SS_PRE_DEAD_TIME_MS;
      r_byte = duration_ms / SS_TIME_SLOT_MS;

      if ((duration_ms >= 0) && (r_byte <= 255)) {
        Serial.write((uint8_t)round(r_byte));
        delay(SS_POS_DEAD_TIME_MS);
      } 
    }

    delay(10);

    receiving = false; 
  }
}

```

The sketch operates very simply: while bytes are available from the serial interface, it reads them and generates the corresponding signal:

1. a start pulse is emitted
2. a pause is observed, consisting of the minimum ("zero") delay
3. and the delay encoding the value of the transmitted byte
4. a stop pulse follows
5. a "postfix" delay is observed

The receiver works as follows:

1. the receiver strobe state is checked
2. if it is active (the pin is at logic 0), the current time is recorded from the built-in clock
3. a lockout interval of 300 ms is observed
4. the arrival of the second (stop) pulse is awaited, while checking for a timeout
5. if the second pulse arrives in time, its arrival time is recorded
6. the received byte value is calculated by dividing the difference between the second and first pulse arrival times by 8 ms

Here is the result we obtained in air, with the transducers about 70 cm apart:

| <img src="https://github.com/user-attachments/assets/90311d52-16f3-44df-a0d1-0cfce6aef984" width="480" /> |
| :---: |
| _Communication log between two modems_ |

The signal can easily be "demodulated" "by hand" from a recording. Here, for example, is a recording made in air:

| <img width="480" src="https://github.com/user-attachments/assets/e4d0ea71-b5b7-44c8-99f8-6fe8dad4025f" /> |
| :---: |
| _Communication log between two modems_ |

The interval between the pulse edges in the recording is 686 milliseconds. Subtract the fixed 300-millisecond delay and divide by 8: `(686 - 300) / 8 = 48.25`. Rounding 48.25 gives the transmitted byte value, 48, which is the ASCII code for the digit **0**.

> FOR INDEPENDENT STUDY:  
> 1. Try changing the various timing values to reduce transmission duration and thus increase the data rate.
> 2. It would also be useful to calculate and experimentally determine the resulting data rate.
> 3. In the example above, we obtained a fractional value of 48.25. What would happen to the receiver if only integer operations were used? What if the resulting value were 48.52 instead of 48.25?

To summarize:
- we learned what an underwater acoustic modem is and how to build one with even minimal signal manipulation capabilities
- we built an underwater acoustic modem that transmits data in 8-bit chunks, encoding a value by the delay between two pulses of the same frequency and fixed duration

### 1.6. Project 4 - Transducer array: measuring the angle of arrival

> _If you do not know what sample size to use, you can take the number 216_  
> O. V. Verkhodanov, astrophysicist

Human ears form an array, as do those of other living creatures with hearing. Formally, it is a simple array of just two elements, but the reality is more interesting: the brain performs highly complex, multilevel processing that includes the perception of body dimensions, sound intensity, different frequencies and the Doppler effect, not to mention experience.

Our aim here is not so much to fully understand, but to get a small taste of the principles underlying angle-measuring underwater acoustic direction-finding systems. Through a practical approach, of course.

We will build an angle-measuring system based on an array of 4 (four) receivers. Two would suffice in the limiting case, but as already mentioned, achieving an acceptable result with two "ears" requires at least a reptilian brain, and we have no brain at all. So we will make up for quality with quantity, a common practice in nature, social life and engineering.

Let us outline our plan. First, to determine an acceptable spacing for our "ears", the transducers, we need to determine how much the signal detection time fluctuates between receivers. Since we are building a ULA (uniform linear array), the spacing between receiving elements must be no less than the fluctuation amplitude. Put simply, if different receivers with transducers placed side by side detect arrival times that differ by about 1 millisecond, spacing the elements less than 1.5 meters apart makes no sense.
Second, we need to determine whether the Arduino Nano can read the states of four receiver pins with sufficient speed and accuracy, or whether a more powerful platform is needed.

Now let us determine the equipment required.

### 1.6.1. Required equipment

| No.    | Name | Quantity | Note |
| :--- | :--- | :--- | :--- |
| 1    | Module [A<sup>3</sup>R](A3R_Datasheet_en.md) | 4 |  |
| 2    | Module [A<sup>3</sup>T](A3T_Datasheet_en.md) | 1 |  |
| 3    | Transceiving transducer [RT-1.332820-1](/documentation/EN/Transducers/RT_1_332820_1_Specification_en) | 1 |  |
| 4    | Receiving transducer [R-1.d3505-1](/documentation/EN/Transducers/R_1.d3505_1_Specification_en) | 4 | |
| 5    | Any microcontroller board, for example, Arduino Nano | 2 |  |
| 6    | Dupont Male-Female or Female-Female wires, 15+ cm | 8 | |

Naturally, two power supplies and a cable for programming the Arduino and receiving its data will also be needed.

In this project, we will build receiving and transmitting sections. The receiving section will be noticeably more complex, while the transmitting section will be very simple. The transmitter is needed to test and debug the receiver, so we will start with it.

#### 1.6.2. Pinger

This will probably be the simplest device we build in this course. Its only task is to trigger transmission at a certain time interval.
Connect the transmitter board to the Arduino Nano according to the table:

| Pin number/name on XS2 | Pin number/name on Arduino Nano |
| :--- | :--- |
| 1 / GND  | GND |
| 4 / Pulse transmission trigger | 10 |
| 20 / VCC | Vin |

> VERY IMPORTANT! The table above shows the supply voltage output from the transmitter board connected to the Arduino Nano's Vin pin. Do this **only after** the board has been programmed and disconnected from the PC!!! Otherwise, it will most likely fail!

Also remember to connect a transceiving transducer to the transmitter board.

The sketch is so simple that we will show it here rather than give it a separate section:

```

#define A3T_TX_ENGAGE_PIN      (10)
#define LED_PIN                (13)
#define PING_HALF_PERIOD_MS    (2000L) 
#define TX_STROBE_DURATION_MS  (10L)

void setup() {

  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  pinMode(A3T_TX_ENGAGE_PIN, OUTPUT);
  digitalWrite(A3T_TX_ENGAGE_PIN, HIGH);
}

void loop() {

    delay(PING_HALF_PERIOD_MS);
    digitalWrite(A3T_TX_ENGAGE_PIN, LOW);
    digitalWrite(LED_PIN, HIGH);
    delay(TX_STROBE_DURATION_MS);
    digitalWrite(A3T_TX_ENGAGE_PIN, HIGH);
    delay(PING_HALF_PERIOD_MS);    
    digitalWrite(LED_PIN, LOW);    

}

```

Its only task is to pull the transmitter control pin to ground for 10 milliseconds at a specified interval, thereby triggering signal transmission.


#### 1.6.3. Receiver

We will combine four receiver boards in a stack, doing exactly what they were designed for. Before that, connect the transducers and set the addresses so that the signals from different receivers are routed to separate bus lines.

| <img src="https://github.com/user-attachments/assets/8eaacc7e-516a-4180-8df2-056bf69282f8" width="480" /> |
| :---: |
| _Setting receiver addresses with jumpers_ |

We recommend stacking the boards in forward or reverse order: address 1 at the bottom, then 2 and 3, with address 4 at the top. This makes it easier to avoid mixing up the transducers. We also strongly recommend numbering the transducers, using tags on the cables or writing numbers directly on the transducers with a wax pencil (the marks will rub off in water). Never use a permanent marker: during prolonged contact, the dye may diffuse into the polymer and become extremely difficult to remove.

Next, connect the receiver stack to the Arduino Nano according to the table:

| Pin number/name on XS2 | Pin number/name on Arduino Nano |
| :--- | :--- |
| 1 / GND  | GND |
| 6 / Receiver No. 1 strobe | 2 |
| 8 / Receiver No. 2 strobe | 3 |
| 10 / Receiver No. 3 strobe | 4 |
| 12 / Receiver No. 4 strobe | 5 |

Here is how ours turned out:

| <img src="https://github.com/user-attachments/assets/bfb02dac-9c5a-4650-8cd3-424ec85962d5" width="480" /> |
| :---: |
| _A stack of four receivers connected to the Arduino Nano board_ |

##### 1.6.3.1. Sketch for transducer array processing

The sketch is intended to send four signal arrival times to the PC, one for each receiver. It is important to detect various false triggers. The main criterion for recognizing our signal is that all arrival times fall within a certain window determined by the dimensions of our transducer array.

```

#include "Limits.h"

#define A3R1_STATE_PIN (2)
#define A3R2_STATE_PIN (3)
#define A3R3_STATE_PIN (4)
#define A3R4_STATE_PIN (5)

#define LED_PIN (13)

const uint8_t inputPinsMasks[] = { B00100000,
                                   B00010000,
                                   B00001000,
                                   B00000100 };

const uint8_t inputPins[] = { A3R1_STATE_PIN, A3R2_STATE_PIN, A3R3_STATE_PIN, A3R4_STATE_PIN };
const int numPins = 4;

bool lastPinState[numPins];
bool pinFallen[numPins];  
unsigned long fallTime[numPins];

const unsigned long DETECTION_WINDOW = 2000;

bool is_any_pin = false;
unsigned long pin_minTime = 0;
unsigned long pin_maxTime = 0;
uint8_t fallen_pins = 0;

void checkPinTimes() {

  is_any_pin = false;
  fallen_pins = 0;

  for (int i = 0; i < numPins; i++) {
    if (pinFallen[i]) {
      fallen_pins++;

      if (!is_any_pin) {
        is_any_pin = true;
        pin_minTime = fallTime[i];
        pin_maxTime = pin_minTime;
      }
    }
  }

  if (is_any_pin) {

    for (int i = 0; i < numPins; i++) {

      if (pinFallen[i]) {
        if (fallTime[i] > pin_maxTime)
          pin_maxTime = fallTime[i];
        if (fallTime[i] < pin_minTime)
          pin_minTime = fallTime[i];
      }
    }
  }  
}

void resetAllFlags() {

  for (int i = 0; i < numPins; i++) {
    pinFallen[i] = false;
  }
}

void setup() {

  Serial.begin(9600);

  for (int i = 0; i < numPins; i++) {
    pinMode(inputPins[i], INPUT_PULLUP);

    // lastPinState[i] = digitalRead(inputPins[i]);
    lastPinState[i] = (PIND & inputPinsMasks[i]) > 0;
    pinFallen[i] = false;
    fallTime[i] = 0;
  }
}

void loop() {

  unsigned long currentTime = micros();

  uint8_t cPIND = PIND;  
  for (int i = 0; i < numPins; i++) {

    bool currentState = (cPIND & inputPinsMasks[i]) > 0;
    if (!currentState && lastPinState[i]) {
      pinFallen[i] = true;
      fallTime[i] = currentTime;
    }

    lastPinState[i] = currentState;
  }

  checkPinTimes();

  if (is_any_pin) {

    if (fallen_pins == numPins) {

      if ((pin_maxTime - pin_minTime) <= DETECTION_WINDOW) {

          /**/
          for (int i = 0; i < numPins; i++) {
            Serial.print(fallTime[i] - pin_minTime);
            Serial.print(", ");
          }
          /**/

          Serial.println();
          delay(500);
        }

      resetAllFlags();

    } else {

      if (currentTime - pin_minTime > DETECTION_WINDOW * 100) {

        resetAllFlags();
        delay(100);
      }
    }
  }
}

```

Looking ahead, we should note that the sketch had to abandon the standard `digitalRead` functions and access the registers directly for greater speed. This makes the sketch somewhat less flexible.

#### 1.6.4. Experiment to determine the spread of arrival times

As mentioned earlier, before building the transducer array, we need to determine how much the signal arrival time fluctuates between receivers. For this, we need half a bucket of water.
In the bucket, we can place all receiving transducers very close to the transmitting transducer. This eliminates all effects related to propagation time and lets us assess how differently the receivers behave.

Recall that we need this to determine the dimensions of the transducer array.

Our experimental setup looks like this:

| <img src="https://github.com/user-attachments/assets/d5ccbea9-d34e-4dfb-8015-4ae33906072f" width="480" /> |
| :---: |
| _The bucket does not have to be blue =)_ |

So:

- the transmitter's Arduino board has been programmed and disconnected from the PC
- the receiver's Arduino board has been programmed and connected to the PC
- the 'Serial Monitor' utility is open in the Arduino IDE, or another terminal application is running to receive data from the serial port
- the receiver stack is powered
- the transmitter is powered

If everything is assembled correctly, the 'Serial Monitor' window will show lines arriving every 4 seconds, each containing 4 comma-separated numbers. The sketch _normalizes_ the arrival times by subtracting the smallest value from each group.
A few dozen lines will be sufficient.

<details>
<summary>Here is the data set we obtained</summary>
<br/>

CSV (Comma-separated values) format, normalized signal arrival times in microseconds<br/>

#id,receiver_4,receiver_3,receiver_2,receiver1<br/>
1,0,140,56,200<br/>
2,56,236,0,56<br/>
3,0,84,24,172<br/>
4,0,28,28,180<br/>
5,0,132,132,132<br/>
6,0,172,0,172<br/>
7,0,248,160,160<br/>
8,0,228,168,24<br/>
9,0,112,52,140<br/>
10,56,316,0,168<br/>
11,0,356,52,84<br/>
12,0,204,112,0<br/>
13,0,168,80,108<br/>
14,0,272,212,212<br/>
15,0,32,0,32<br/>
16,0,264,28,112<br/>
17,0,116,52,52<br/>
18,28,168,140,0<br/>
19,0,116,56,56<br/>
20,0,92,0,32<br/>
21,0,144,28,84<br/>
22,0,252,80,192<br/>
23,0,28,60,28<br/>
24,208,244,0,208<br/>
25,60,0,28,148<br/>
26,84,0,24,112<br/>
27,132,280,188,0<br/>
28,0,136,108,168<br/>
29,168,136,0,52<br/>
30,80,136,0,136<br/>
31,136,136,0,52<br/>
32,88,204,172,0<br/>
33,0,140,228,196<br/>
34,108,108,196,0<br/>
35,28,172,140,0<br/>
36,28,116,0,56<br/>
37,120,120,0,0<br/>
38,80,228,0,164<br/>
39,164,164,0,52<br/>
40,0,104,188,188<br/>
41,0,260,108,80<br/>
42,52,152,52,0<br/>
43,0,56,28,56<br/>
44,108,0,136,136<br/>
45,28,268,120,0<br/>
46,160,248,0,188<br/>
47,0,224,76,164<br/>
48,0,280,128,128<br/>
49,0,28,56,152<br/>
50,28,84,0,204<br/>
51,0,172,52,84<br/>
52,0,224,80,192<br/>
53,80,224,0,192<br/>
54,0,140,28,140<br/>
55,0,136,52,196<br/>
56,24,168,140,0<br/>
57,88,56,28,0<br/>
58,0,92,0,56<br/>
59,0,28,184,56<br/>
60,28,84,84,0<br/>
61,0,172,80,52<br/>
62,28,148,0,88<br/>
63,80,108,140,0<br/>
64,28,152,0,64<br/>
65,28,0,60,0<br/>
66,56,96,28,0<br/>
67,172,52,0,52<br/>
68,0,224,164,52<br/>
69,0,28,88,56<br/>
70,136,108,0,168<br/>
71,0,32,0,32<br/>
72,108,228,52,0<br/>
73,0,32,0,60<br/>
74,0,276,132,244<br/>
75,84,0,260,52<br/>
76,28,88,0,28<br/>
77,0,116,28,84<br/>
78,0,340,160,132<br/>
79,0,108,108,108<br/>
80,0,164,52,164<br/>
81,28,204,0,84<br/>
82,28,120,28,0<br/>
83,0,84,56,116<br/>
84,0,104,160,192<br/>
85,28,228,0,168<br/>
86,0,232,0,144<br/>
87,0,228,76,76<br/>
88,108,0,192,192<br/>
89,0,168,112,200<br/>
90,28,112,0,144<br/>
91,56,196,0,196<br/>
92,80,0,52,120<br/>
93,56,300,84,0<br/>
94,0,336,216,132<br/>
95,0,144,28,112<br/>
96,0,148,0,176<br/>
97,112,172,28,0<br/>
98,56,0,84,116<br/>
99,0,0,0,64<br/>
100,0,164,224,80<br/>
101,0,120,0,88<br/>
102,28,60,28,0<br/>
103,108,108,0,108<br/>
104,0,80,164,164<br/>
105,112,172,0,56<br/>
106,0,28,60,28<br/>
107,28,168,200,0<br/>
108,52,0,84,52<br/>
109,24,0,112,232<br/>
110,0,260,108,52<br/>
111,0,204,140,28<br/>
112,0,348,0,168<br/>
113,0,292,60,172<br/>
114,0,220,80,220<br/>
115,28,260,0,168<br/>
116,0,132,104,164<br/>
117,116,52,0,84<br/>
118,0,216,216,132<br/>
119,0,176,0,116<br/>
120,28,144,84,0<br/>
121,52,228,0,136<br/>
122,0,172,52,108<br/>
123,84,144,0,52<br/>
124,0,152,0,0<br/>
125,0,164,196,80<br/>
126,80,228,0,164<br/>
127,0,140,140,28<br/>
128,28,176,0,84<br/>
129,56,0,28,116<br/>
130,28,28,60,0<br/>
131,0,80,80,228<br/>
132,0,88,28,184<br/>
133,60,120,0,0<br/>
134,0,120,0,32<br/>
135,120,28,28,0<br/>
136,80,196,0,164<br/>
137,0,216,184,156<br/>
138,52,224,0,196<br/>
139,0,164,80,256<br/>
140,0,80,80,80<br/>
141,84,24,0,84<br/>
142,0,176,84,56<br/>
143,108,140,80,0<br/>
144,160,248,216,0<br/>
145,32,156,0,0<br/>
146,28,208,56,0<br/>
147,104,256,104,0<br/>
148,0,280,80,192<br/>
149,28,264,84,0<br/>
150,136,0,80,256<br/>
151,0,260,112,80<br/>
152,80,232,0,80<br/>
153,56,196,0,228<br/>
154,60,180,28,0<br/>
155,0,264,84,28<br/>
156,164,344,108,0<br/>
157,0,60,0,148<br/>
158,0,60,0,148<br/>
159,28,172,264,0<br/>
160,132,0,188,220<br/>
161,56,236,24,0<br/>
162,164,108,0,164<br/>
163,64,184,32,0<br/>
164,0,164,164,52<br/>
165,0,80,136,136<br/>
166,0,228,80,140<br/>
167,56,112,0,200<br/>
168,0,140,80,52<br/>
169,28,348,0,196<br/>
170,28,60,236,0<br/>
171,136,196,0,80<br/>
172,0,32,0,156<br/>
173,0,84,84,28<br/>
174,56,0,112,204<br/>
175,28,288,0,196<br/>
176,0,132,132,164<br/>
177,28,116,0,116<br/>
178,56,152,24,0<br/>
179,0,168,80,168<br/>
180,0,52,52,180<br/>
181,156,224,0,156<br/>
182,0,112,56,172<br/>
183,84,176,0,28<br/>
184,0,116,84,28<br/>
185,0,84,28,116<br/>
186,60,0,60,28<br/>
187,0,132,164,132<br/>
188,60,120,0,60<br/>
189,0,280,132,188<br/>
190,52,172,112,0<br/>
191,88,0,28,28<br/>

<br/>  
</details>

For clarity, let us plot these times:

| <img src="https://github.com/user-attachments/assets/7c279546-244b-4e05-82c5-ebf7ce242d84" width="480" /> |
| :---: |
| _Most values do not exceed 300 μs_ |

The graph shows that arrival times generally fluctuate relative to one another within 300–350 microseconds. At a speed of sound of ~1500 m/s, this corresponds to about 0.5 meter.

> It is useful and easy to remember that sound travels about 1.5 meters in water in one millisecond.

The accuracy is not spectacular, but it is quite usable.

Based on this measured value, we can choose a spacing of 1 meter between the elements of our transducer array. Of course, the sample is fairly small and there is a good chance that the spread could reach 1 millisecond. But first, we want to understand the principle, and second, we will be able to see such cases when calculating the angles of arrival. For now, we want to avoid complicating matters with an excessively bulky array and to understand that even at this size, most data can be sufficiently accurate.

#### 1.6.5. Transducer array

If you have a simple way to hang 4 receiving transducers at 1-meter intervals, that is great — you will have almost nothing to do. We did not, so we assembled this structure from polypropylene plumbing pipes:

| <img src="https://github.com/user-attachments/assets/4f83bbf1-cee1-4bb4-8bc8-9d188ff52e59" width="480" /> |
| :---: |
| _A simple structure for positioning four receiving transducers a meter apart_ |

We expected the structure to sit directly on the water (in a swimming pool, of course; taking it to a natural body of water is strongly discouraged), so we added extra buoyancy. In fact, we could have done without it.

> Let us estimate the buoyancy of the whole frame. First, weigh it: ours was 1.5 kg. Now estimate a lower bound for the volume of water displaced. We use an upper bound for the weight and a lower bound for the volume. If the mass of this volume of water exceeds the measured weight by a reasonable margin, everything is fine: the structure will float. The calculation is very simple. Since we need the minimum volume, we calculate only the pipe volume, excluding fittings, which increase it.  
> Our pipe has a diameter of 25 mm, so its cross-sectional area is $&pi;r^2 = 3.1415*0.0125^2=0.000490859 \space m^2$. The total pipe length is 8 m. Multiplying the two gives the displaced water volume: $0.000490859 * 8 = 0.003926875 \space m^3$. At a density of $1000 \space kg/m^3$, this volume of water has a mass of 3.9 kg. The measured weight of the entire structure is only 1.5 kg, so we have 3.9-1.5=2.4 kg of excess buoyancy.

Without modifications, the receiving transducer cables are long enough to suspend the transducers about 15–20 cm below the frame.

| <img src="https://github.com/user-attachments/assets/e153663a-4163-43bb-9bf2-2a4f8f1ac977" width="480" /> |
| :---: |
| _Marks are made with electrical tape_ |

Lay everything out on the floor to see how it looks assembled and how much spare cable length is available.

| <img src="https://github.com/user-attachments/assets/50a4f879-4174-4035-86a0-b380e2bf2350" width="480" /> |
| :---: |
| _There is practically no spare cable length_ |

The stiff cables may prevent the transducers from hanging straight. This is not entirely without effect in our case, but it should not contribute much to the overall result. Besides, the user can certainly solve this mechanical issue independently.

#### 1.6.6. Swimming pool experiment

For a complete picture, we need data for several relative positions of the transmitter and receiving array.

First, let us define "left" and "right": transducer No. 1 is on the left and transducer No. 4 is on the right:

| <img src="https://github.com/user-attachments/assets/ffc94e53-bc17-49a5-93b0-0b3085f66b18" width="480" /> |
| :---: |
| _Order of transducers in the array_ |

At a minimum, use the following positions:

- "left": the transmitter is directly to the left, on the line containing the transducers
- "in front": the transmitter is on a line perpendicular to the array line
- "right": the transmitter is directly to the right, on the line containing the transducers

If possible, obtain data for intermediate positions, for example, between "left" and "in front", and between "in front" and "right".

Here is our experimental layout:

| <img src="https://github.com/user-attachments/assets/a4def20b-3364-4cca-940c-6eb6321206ec" width="480" /> |
| :---: |
| _No. 1 .. No. 4 are signal source positions; R1 .. R4 are receiving array element positions_ |

For each relative position of the transducer array and source, we recommend collecting 150–200 measurements.

> If the pool water has not settled, the receiving and transmitting transducers can often become covered in air bubbles quite quickly. If the receivers suddenly stop responding during the experiment while all connections are sound and there is no visible reason, look closely at the transducer surfaces: they may be covered in air bubbles. Simply remove the bubbles by hand to restore operation.

It is useful to monitor the experiment: first, ensure data is arriving, and second, have at least a general idea of whether it is plausible.
For example, if the source is directly to the left, the signal should reach transducer No. 1 first, then No. 2, and so on. Our sketch sends arrival times in reverse order, so we expect four successively decreasing numbers, such as `1936, 1284, 724, 0, `.
We strongly recommend thinking about the data you expect before conducting the experiment. This is good practice not only for this experiment, but for any experiment — and _good practice in life_ in general.

| <img src="https://github.com/user-attachments/assets/19bba39b-e685-4690-939e-434d7be7e843" width="480" /> |
| :---: |
| _Keeping a finger on the pulse_ |

We obtained data sets for five relative positions of the receiving array and signal source: left, between left and in front, in front, between in front and right, and right.
The water temperature in the pool during the experiment was 21.6 °C.

Here are the data, again in CSV (comma-separated values) format:

<details>
<summary>Experiment No. 1 - Source directly to the left</summary>
<br/>

# Normalized arrival times in microseconds
receiver_4,receiver_3,receiver_2,receiver_1<br/>
 1936, 1284, 724, 0<br/>
 1964, 1428, 680, 0<br/>
 1924, 1424, 696, 0<br/>
 1884, 1228, 728, 0<br/>
 1852, 1344, 652, 0<br/>
 1816, 1336, 784, 0<br/>
 1936, 1228, 832, 0<br/>
 1936, 1368, 724, 0<br/>
 1880, 1432, 604, 0<br/>
 1892, 1332, 800, 0<br/>
 1980, 1392, 856, 0<br/>
 1864, 1416, 808, 0<br/>
 1852, 1380, 652, 0<br/>
 1912, 1376, 628, 0<br/>
 1924, 1476, 756, 0<br/>
 1988, 1364, 756, 0<br/>
 1932, 1308, 808, 0<br/>
 1888, 1444, 828, 0<br/>
 1972, 1348, 628, 0<br/>
 1880, 1408, 628, 0<br/>
 1868, 1392, 808, 0<br/>
 1972, 1204, 784, 0<br/>
 1872, 1400, 732, 0<br/>
 1960, 1488, 652, 0<br/>
 1868, 1420, 776, 0<br/>
 1992, 1400, 732, 0<br/>
 1928, 1392, 784, 0<br/>
 1936, 1308, 784, 0<br/>
 1928, 1340, 808, 0<br/>
 1944, 1232, 724, 0<br/>
 1908, 1344, 704, 0<br/>
 1948, 1300, 576, 0<br/>
 1968, 1372, 628, 0<br/>
 1912, 1316, 680, 0<br/>
 1936, 1224, 836, 0<br/>
 1912, 1380, 656, 0<br/>
 1988, 1392, 748, 0<br/>
 1980, 1448, 832, 0<br/>
 1852, 1344, 652, 0<br/>
 1912, 1228, 724, 0<br/>
 1976, 1204, 680, 0<br/>
 1940, 1256, 724, 0<br/>
 1976, 1528, 836, 0<br/>
 1964, 1280, 808, 0<br/>
 1932, 1424, 696, 0<br/>
 1956, 1420, 776, 0<br/>
 1968, 1340, 676, 0<br/>
 1936, 1404, 596, 0<br/>
 1964, 1368, 732, 0<br/>
 1956, 1388, 832, 0<br/>
 1968, 1404, 628, 0<br/>
 1992, 1196, 776, 0<br/>
 1976, 1288, 680, 0<br/>
 1968, 1524, 912, 0<br/>
 1872, 1336, 784, 0<br/>
 1976, 1444, 884, 0<br/>
 1904, 1340, 756, 0<br/>
 1932, 1432, 676, 0<br/>
 1980, 1444, 836, 0<br/>
 1984, 1416, 780, 0<br/>
 1928, 1424, 808, 0<br/>
 1948, 1476, 888, 0<br/>
 1900, 1420, 728, 0<br/>
 1936, 1220, 832, 0<br/>
 1968, 1404, 628, 0<br/>
 1992, 1196, 776, 0<br/>
 1976, 1288, 680, 0<br/>
 1968, 1524, 912, 0<br/>
 1872, 1336, 784, 0<br/>
 1976, 1444, 884, 0<br/>
 1904, 1340, 756, 0<br/>
 1932, 1432, 676, 0<br/>
 1980, 1444, 836, 0<br/>
 1984, 1416, 780, 0<br/>
 1928, 1424, 808, 0<br/>
 1948, 1476, 888, 0<br/>
 1900, 1420, 728, 0<br/>
 1936, 1220, 832, 0<br/>
 2000, 1196, 756, 0<br/>
 1972, 1384, 604, 0<br/>
 1924, 1336, 804, 0<br/>
 1896, 1416, 808, 0<br/>
 1972, 1528, 912, 0<br/>
 1988, 1424, 732, 0<br/>
 1920, 1332, 856, 0<br/>
 1968, 1496, 576, 0<br/>
 1840, 1420, 756, 0<br/>

<br/> 
</details>

<details>
<summary>Experiment No. 2 - Source between directly left and in front</summary>
<br/>

# Normalized arrival times in microseconds
receiver_4,receiver_3,receiver_2,receiver_1<br/>
 1816, 1372, 728, 0<br/>
 1640, 1852, 784, 0<br/>
 1680, 1856, 732, 0<br/>
 1844, 1904, 732, 0<br/>
 1948, 1556, 784, 0<br/>
 1760, 1792, 732, 0<br/>
 1772, 1036, 724, 0<br/>
 1752, 1068, 652, 0<br/>
 1796, 1112, 832, 0<br/>
 1760, 1232, 724, 0<br/>
 1840, 1812, 388, 0<br/>
 1872, 1100, 628, 0<br/>
 1800, 1268, 1072, 0<br/>
 1920, 1148, 704, 0<br/>
 1680, 1208, 732, 0<br/>
 1888, 1740, 544, 0<br/>
 1640, 1816, 884, 0<br/>
 1744, 1124, 732, 0<br/>
 1672, 1228, 724, 0<br/>
 1844, 1872, 704, 0<br/>
 1976, 1384, 964, 0<br/>
 1924, 1392, 776, 0<br/>
 1960, 1216, 884, 0<br/>
 1860, 1416, 912, 0<br/>
 1844, 1340, 700, 0<br/>
 1720, 1808, 884, 0<br/>
 1812, 1664, 936, 0<br/>
 1864, 1680, 568, 0<br/>
 1764, 1856, 680, 0<br/>
 1860, 1268, 652, 0<br/>
 1836, 1864, 860, 0<br/>
 1820, 1224, 836, 0<br/>
 1808, 1336, 884, 0<br/>
 1812, 1716, 884, 0<br/>
 1824, 1224, 756, 0<br/>
 1716, 1068, 756, 0<br/>
 1796, 1668, 756, 0<br/>
 1804, 1776, 884, 0<br/>
 1748, 1308, 884, 0<br/>
 1828, 1860, 912, 0<br/>
 1880, 1344, 676, 0<br/>
 1768, 1296, 624, 0<br/>
 1904, 1340, 724, 0<br/>
 1804, 1864, 912, 0<br/>
 1892, 1324, 964, 0<br/>
 1628, 1424, 836, 0<br/>
 1736, 1440, 880, 0<br/>
 1644, 1024, 884, 0<br/>
 1908, 1224, 808, 0<br/>
 1820, 1792, 596, 0<br/>
 1768, 1356, 856, 0<br/>
 1712, 1204, 704, 0<br/>
 1904, 1256, 832, 0<br/>
 1748, 1272, 884, 0<br/>
 1860, 1892, 500, 0<br/>
 1992, 1308, 836, 0<br/>
 1852, 1940, 656, 0<br/>
 1740, 1236, 704, 0<br/>
 1920, 1352, 544, 0<br/>
 1772, 1148, 732, 0<br/>
 1968, 1260, 424, 0<br/>
 1856, 1200, 756, 0<br/>

<br/> 
</details>

<details>
<summary>Experiment No. 3 - Source in front</summary>
<br/>

# Normalized arrival times in microseconds
receiver_4,receiver_3,receiver_2,receiver_1<br/>
 132, 0, 300, 360<br/>
 104, 0, 272, 480<br/>
 300, 0, 180, 388<br/>
 28, 84, 0, 204<br/>
 188, 0, 128, 480<br/>
 0, 56, 228, 376<br/>
 28, 112, 0, 112<br/>
 260, 0, 260, 260<br/>
 464, 28, 0, 168<br/>
 688, 0, 132, 296<br/>
 604, 0, 156, 156<br/>
 428, 0, 28, 224<br/>
 708, 0, 184, 376<br/>
 640, 0, 260, 404<br/>
 676, 0, 352, 184<br/>
 540, 0, 208, 236<br/>
 636, 0, 80, 252<br/>
 560, 0, 128, 352<br/>
 692, 0, 184, 184<br/>
 496, 0, 52, 52<br/>
 712, 0, 180, 208<br/>
 652, 0, 208, 292<br/>
 788, 0, 56, 256<br/>
 616, 0, 156, 380<br/>
 696, 0, 104, 188<br/>
 736, 0, 212, 380<br/>
 108, 0, 108, 168<br/>
 472, 112, 56, 0<br/>
 664, 0, 104, 104<br/>
 172, 0, 84, 56<br/>
 616, 0, 380, 208<br/>
 604, 0, 80, 192<br/>
 56, 24, 24, 0<br/>
 612, 0, 108, 164<br/>
 628, 0, 76, 272<br/>
 268, 0, 184, 356<br/>
 232, 0, 232, 232<br/>
 528, 0, 184, 348<br/>
 660, 0, 108, 300<br/>
 604, 0, 160, 192<br/>
 688, 0, 336, 364<br/>
 612, 52, 0, 192<br/>
 868, 360, 0, 360<br/>
 628, 0, 104, 272<br/>
 764, 0, 208, 344<br/>
 664, 0, 24, 308<br/>
 812, 0, 56, 192<br/>
 660, 28, 0, 360<br/>
 728, 0, 344, 400<br/>
 564, 0, 156, 240<br/>
 552, 0, 52, 220<br/>
 576, 104, 0, 280<br/>
 780, 0, 260, 424<br/>
 572, 0, 104, 300<br/>
 556, 0, 28, 196<br/>
 604, 0, 160, 104<br/>
 660, 0, 156, 184<br/>
 644, 0, 80, 108<br/>
 676, 0, 236, 264<br/>
 660, 0, 80, 328<br/>
 700, 0, 80, 220<br/>
 680, 0, 180, 264<br/>
 544, 0, 156, 212<br/>
 244, 0, 188, 244<br/>
 328, 0, 132, 416<br/>
 312, 0, 104, 132<br/>
 184, 0, 308, 248<br/>
 248, 52, 0, 280<br/>
 216, 0, 248, 80<br/>
 192, 164, 0, 312<br/>
 56, 0, 28, 296<br/>
 76, 0, 272, 332<br/>
 104, 0, 280, 280<br/>
 136, 0, 104, 104<br/>
 388, 52, 0, 388<br/>
 84, 0, 28, 328<br/>
 116, 28, 0, 84<br/>
 164, 0, 80, 224<br/>
 280, 0, 164, 220<br/>
 312, 0, 136, 104<br/>
 364, 0, 336, 452<br/>
 352, 0, 320, 292<br/>
 132, 0, 160, 220<br/>
 272, 0, 104, 332<br/>
 60, 0, 176, 144<br/>
 296, 0, 156, 296<br/>
 312, 0, 164, 104<br/>
 84, 0, 116, 116<br/>
 248, 0, 80, 220<br/>
 104, 0, 104, 196<br/>
 140, 0, 252, 340<br/>
 276, 0, 80, 336<br/>
 316, 0, 232, 348<br/>
 168, 0, 112, 376<br/>
 84, 28, 0, 232<br/>
 244, 0, 160, 272<br/>
 112, 0, 252, 252<br/>
 52, 0, 192, 340<br/>
 348, 0, 208, 408<br/>
 188, 0, 300, 300<br/>
 180, 0, 212, 300<br/>
 220, 0, 52, 280<br/>
 300, 0, 132, 300<br/>
 84, 28, 0, 264<br/>
 28, 0, 56, 144<br/>
 272, 0, 216, 272<br/>
 344, 0, 260, 344<br/>
 80, 0, 136, 164<br/>
 200, 0, 56, 140<br/>
 288, 0, 256, 316<br/>
 240, 0, 156, 328<br/>
 168, 0, 112, 316<br/>
 112, 0, 56, 172<br/>
 264, 0, 208, 324<br/>
 56, 56, 0, 264<br/>
 0, 56, 0, 116<br/>
 52, 0, 192, 340<br/>
 56, 24, 0, 232<br/>
 188, 0, 104, 248<br/>
 192, 80, 0, 252<br/>
 84, 0, 112, 260<br/>
 372, 0, 312, 340<br/>
 192, 0, 52, 224<br/>
 256, 0, 112, 196<br/>
 104, 0, 308, 216<br/>
 324, 0, 156, 384<br/>
 276, 0, 192, 276<br/>
 276, 104, 0, 244<br/>
 236, 0, 180, 296<br/>
 168, 0, 112, 200<br/>
 188, 0, 104, 336<br/>
 80, 0, 164, 196<br/>
 324, 0, 240, 356<br/>
 160, 0, 76, 308<br/>
 364, 0, 132, 216<br/>
 200, 0, 60, 232<br/>
 184, 0, 184, 304<br/>
 304, 0, 80, 332<br/>
 284, 0, 84, 224<br/>
 104, 0, 76, 168<br/>
 104, 0, 244, 304<br/>
 296, 0, 240, 296<br/>
 180, 0, 236, 356<br/>
 332, 0, 80, 300<br/>
 148, 0, 24, 116<br/>
 188, 0, 104, 308<br/>
 24, 0, 136, 228<br/>
 120, 0, 28, 296<br/>
 372, 0, 260, 372<br/>
 232, 0, 0, 112<br/>
 244, 0, 212, 212<br/>
 52, 52, 0, 260<br/>
 180, 0, 208, 328<br/>
 292, 0, 32, 172<br/>
 220, 0, 160, 104<br/>
 216, 0, 160, 244<br/>
 264, 0, 264, 264<br/>
 0, 24, 84, 56<br/>
 284, 0, 80, 192<br/>
 344, 0, 372, 404<br/>
 224, 0, 104, 104<br/>
 112, 0, 0, 112<br/>
 292, 0, 292, 472<br/>
 368, 0, 284, 368<br/>
 0, 56, 84, 320<br/>
 308, 0, 188, 188<br/>
 328, 0, 156, 240<br/>
 240, 0, 180, 208<br/>
 224, 52, 0, 344<br/>
 168, 0, 28, 140<br/>
 132, 0, 248, 188<br/>
 192, 0, 160, 160<br/>
 56, 28, 176, 0<br/>
 132, 0, 104, 252<br/>
 332, 0, 104, 392<br/>
 156, 0, 156, 188<br/>
 132, 0, 308, 188<br/>
 160, 0, 104, 160<br/>
 128, 128, 0, 220<br/>
 304, 56, 0, 364<br/>

<br/> 
</details>

<details>
<summary>Experiment No. 4 - Source between in front and directly right</summary>
<br/>

# Normalized arrival times in microseconds
receiver_4,receiver_3,receiver_2,receiver_1<br/>
 0, 420, 1228, 1644<br/>
 0, 464, 1108, 1968<br/>
 0, 364, 1060, 1680<br/>
 0, 416, 1196, 1764<br/>
 0, 496, 1024, 1620<br/>
 0, 496, 1108, 1968<br/>
 0, 128, 744, 1424<br/>
 0, 604, 688, 1724<br/>
 0, 364, 916, 1544<br/>
 0, 652, 876, 1736<br/>
 0, 104, 828, 1720<br/>
 0, 292, 984, 1580<br/>
 0, 388, 864, 1456<br/>
 0, 596, 1208, 1924<br/>
 0, 724, 864, 1460<br/>
 76, 0, 748, 1308<br/>
 0, 292, 1012, 1756<br/>
 0, 260, 984, 1868<br/>
 0, 652, 928, 1492<br/>
 0, 544, 1240, 1924<br/>
 312, 0, 532, 1572<br/>
 0, 184, 936, 1528<br/>
 0, 180, 1072, 1640<br/>
 0, 516, 968, 1852<br/>
 0, 680, 820, 1496<br/>
 0, 156, 1048, 1676<br/>
 0, 576, 1272, 1920<br/>
 0, 232, 848, 1468<br/>
 0, 0, 720, 1608<br/>
 0, 232, 1096, 1392<br/>
 0, 544, 1216, 1960<br/>
 0, 340, 868, 1552<br/>
 0, 56, 692, 1552<br/>
 0, 132, 1024, 1560<br/>
 0, 232, 904, 1524<br/>
 0, 544, 1296, 1952<br/>
 0, 240, 904, 1620<br/>
 0, 336, 980, 1512<br/>
 0, 260, 740, 1416<br/>
 0, 396, 952, 1664<br/>
 0, 156, 904, 1620<br/>
 0, 80, 776, 1696<br/>
 0, 368, 948, 1428<br/>
 0, 312, 864, 1492<br/>
 0, 104, 692, 1460<br/>
 0, 240, 740, 1512<br/>
 0, 236, 768, 1504<br/>
 0, 644, 1232, 1948<br/>
 180, 0, 624, 1248<br/>
 0, 312, 924, 1604<br/>
 180, 0, 568, 1284<br/>
 0, 232, 848, 1380<br/>
 0, 292, 624, 1340<br/>
 0, 652, 1040, 1992<br/>
 164, 0, 524, 1416<br/>
 0, 104, 632, 1668<br/>
 0, 184, 744, 1868<br/>
 444, 0, 668, 1468<br/>
 288, 0, 708, 1240<br/>
 344, 0, 480, 1256<br/>
 0, 336, 756, 1940<br/>
 0, 312, 760, 1652<br/>
 0, 492, 1272, 1928<br/>
 0, 260, 704, 1564<br/>
 360, 0, 756, 1256<br/>
 236, 0, 540, 1076<br/>
 0, 104, 884, 1276<br/>
 260, 0, 564, 1280<br/>
 340, 0, 732, 1324<br/>
 344, 0, 648, 1148<br/>
 0, 732, 1340, 1848<br/>
 188, 0, 328, 976<br/>
 0, 628, 1128, 1724<br/>
 0, 0, 644, 1292<br/>
 216, 0, 632, 1492<br/>
 336, 0, 756, 1436<br/>
 0, 676, 1208, 1948<br/>
 316, 0, 540, 1284<br/>
 516, 0, 856, 1328<br/>
 388, 0, 756, 1168<br/>
 264, 0, 596, 1156<br/>
 156, 0, 708, 980<br/>
 416, 0, 584, 1296<br/>
 388, 0, 868, 1192<br/>
 268, 0, 684, 1160<br/>
 0, 756, 1280, 1788<br/>
 180, 0, 520, 1344<br/>
 140, 0, 552, 968<br/>
 0, 628, 1124, 1868<br/>
 388, 0, 776, 1372<br/>
 232, 0, 600, 1160<br/>
 156, 0, 572, 924<br/>
 260, 0, 540, 1076<br/>
 156, 0, 496, 1084<br/>
 0, 748, 1504, 1708<br/>
 420, 0, 700, 1352<br/>
 256, 0, 620, 1036<br/>
 308, 0, 648, 1120<br/>
 0, 652, 1372, 1732<br/>
 260, 0, 508, 1428<br/>
 208, 0, 768, 1212<br/>
 0, 620, 1292, 1948<br/>
 0, 680, 1316, 1648<br/>
 236, 0, 768, 1092<br/>
 344, 0, 648, 1092<br/>
 0, 728, 1228, 1824<br/>
 0, 680, 1316, 1824<br/>
 156, 0, 412, 1120<br/>
 264, 0, 680, 1036<br/>
 232, 0, 540, 988<br/>
 208, 0, 572, 1076<br/>
 372, 0, 896, 1192<br/>
 260, 0, 756, 1116<br/>
 440, 0, 888, 1360<br/>
 260, 0, 624, 1068<br/>
 0, 724, 1368, 1848<br/>
 184, 0, 652, 1044<br/>
 284, 0, 568, 1220<br/>
 288, 0, 928, 1280<br/>

<br/> 
</details>

<details>
<summary>Experiment No. 5 - Source directly to the right</summary>
<br/>

# Normalized arrival times in microseconds
receiver_4,receiver_3,receiver_2,receiver_1<br/>
 0, 704, 1508, 1956<br/>
 0, 524, 1308, 1924<br/>
 0, 652, 1156, 1776<br/>
 0, 728, 1284, 1908<br/>
 0, 724, 1532, 1952<br/>
 0, 704, 1488, 1840<br/>
 0, 672, 1480, 1960<br/>
 0, 704, 1340, 1876<br/>
 0, 680, 1516, 1956<br/>
 0, 544, 1492, 1904<br/>
 0, 724, 1448, 1920<br/>
 0, 728, 1392, 1988<br/>
 0, 680, 1372, 1908<br/>
 0, 548, 1384, 1884<br/>
 0, 620, 1456, 1936<br/>
 0, 676, 1432, 1992<br/>
 0, 656, 1548, 1932<br/>
 0, 676, 1564, 1924<br/>
 0, 524, 1276, 1924<br/>
 0, 652, 1544, 1988<br/>
 0, 704, 1484, 1984<br/>
 0, 680, 1428, 1936<br/>
 0, 780, 1368, 1956<br/>
 0, 620, 1568, 1984<br/>
 0, 704, 1484, 1896<br/>
 0, 676, 1480, 1840<br/>
 0, 652, 1320, 1940<br/>
 0, 596, 1320, 1944<br/>
 0, 704, 1232, 1944<br/>
 0, 628, 1464, 1996<br/>
 0, 696, 1480, 1952<br/>
 0, 680, 1516, 1988<br/>
 0, 776, 1528, 1920<br/>
 0, 572, 1292, 1948<br/>
 0, 656, 1520, 1960<br/>
 0, 696, 1560, 1924<br/>
 0, 576, 1128, 1992<br/>
 0, 884, 1556, 1908<br/>
 0, 748, 1364, 1836<br/>
 0, 704, 1512, 1984<br/>
 0, 652, 1488, 1960<br/>
 0, 672, 1204, 1948<br/>
 0, 732, 1480, 1956<br/>
 0, 524, 1076, 1852<br/>
 0, 836, 1584, 1912<br/>
 0, 728, 1456, 1984<br/>
 0, 652, 1456, 1876<br/>
 0, 808, 1476, 1920<br/>
 0, 696, 1396, 1992<br/>
 0, 756, 1392, 1900<br/>
 0, 756, 1508, 1980<br/>
 0, 696, 1424, 1952<br/>
 0, 576, 1348, 1740<br/>
 0, 732, 1092, 1980<br/>
 0, 828, 1528, 1912<br/>
 0, 780, 1364, 1988<br/>
 0, 752, 1420, 1928<br/>
 0, 600, 1268, 1800<br/>
 0, 756, 1480, 1952<br/>
 0, 776, 1392, 1840<br/>
 0, 784, 1504, 1980<br/>
 0, 784, 1532, 1952<br/>
 0, 780, 1280, 1992<br/>
 0, 680, 1400, 1964<br/>
 0, 780, 1480, 1980<br/>
 0, 628, 1292, 1740<br/>
 0, 756, 1424, 1988<br/>
 0, 628, 1184, 1956<br/>
 0, 672, 1316, 1968<br/>
 0, 628, 1320, 1944<br/>
 0, 704, 1264, 2000<br/>
 0, 756, 1456, 1956<br/>
 0, 680, 1544, 1988<br/>

<br/> 
</details>

Having collected the data, it is time for the most interesting part: processing it. Welcome to the next section.

#### 1.6.7. Processing the experimental results

In this section, we will touch briefly on mathematics and trigonometry.

First, consider a simple case in which a plane wavefront is incident on two elements of a transducer array:

| <img src="https://github.com/user-attachments/assets/bae6a922-551a-4cc1-80db-9da77cfceff5" width="480" /> |
| :---: |
| _Illustration of a plane wavefront incident on two receivers_ |

In the illustration above, the wavefront is incident on two receivers at an angle $\alpha$, with a delay $\Delta t$ between its arrival at the first receiver (left) and the second (right). If the propagation speed is $V$ and the spacing between receivers is $\Delta X$,
then the angle $\alpha$ can be determined from:

$$ \frac{\Delta t * V}{\Delta X} = cos(\alpha) $$ 

Cosine is the ratio of the adjacent side to the hypotenuse. In our case, the hypotenuse is $\Delta X$ and the adjacent side is $\Delta t * V$.

> **The KO MNE (TOWARD ME) rule**:  
> It is easy to remember cosine: **CO**sine is the ratio of the adjacent side (_TOWARD ME_) to the hypotenuse.
> Sine is therefore the ratio of the opposite side to the hypotenuse,
> **CO**tangent is the ratio of the adjacent side (_TOWARD ME_) to the opposite side,
> and tangent is the ratio of the opposite side to the adjacent side.

This relationship alone is enough to build an angle-measuring system with two receivers. As noted above, however, this is not advisable: a time measurement error at even one receiver will produce a completely incorrect result.
In such cases, it makes sense to increase the number of receivers and let each have a say.

First, assume that a _plane_ wavefront is incident on our array. Viewed from above, it is a line. This is a reasonable assumption if the distance to the source is much greater than the array size. Of course, this does not hold in the pool, but we have to start somewhere, right?

| <img src="https://github.com/user-attachments/assets/3fc62e4f-d9db-4b2b-86bb-5239f44c4b64" width="480" /> |
| :---: |
| _Determining the angle of arrival at a linear transducer array_ |

The diagram above shows a coordinate system centered on the first receiver. The X axis points to the right as usual, while the Y axis represents time multiplied by the wave propagation speed.

Now suppose we have taken a measurement and obtained signal arrival times at each receiver. We mark each receiver's time multiplied by the speed of sound in water with a green circle.

Here is a very important point: **if we assume a plane wavefront, the green circles should form a line**. The wavefront reaches each receiver after a time proportional to that receiver's distance from the origin and to the angle at which the wavefront is incident on the linear array.

But there is always a "but", isn't there?

The circles do not form a _perfectly straight_ line: there is always some measurement error. However, we need to account for the contribution of every propagation time. Essentially, we must position a line as close as possible to each green circle — as close as possible in the mathematical sense.

In 1929, Edwin Hubble formulated his famous law in precisely this way, drawing a line through a set of measurements.

| <img src="https://github.com/user-attachments/assets/b5b264dc-accc-4877-af43-346200343728" width="480" /> |
| :---: |
| _Graph from Hubble's original 1929 paper_ |

Hubble also obtained noisy measurements and plotted points with the distance to _Cepheids_ in nearby galaxies on the X axis and their velocity on the Y axis.
We must give Hubble credit: it takes considerable courage to draw a line through such a cloud of points and insist that the relationship between recession velocity and distance is linear.

Our task is much easier: we already _know_ there should be a line; we just need to draw it correctly, _approximating_ the set of points with a line.

The good news is that this is not difficult: drawing a line means finding its equation. The equation of a line is simple and has the general form $y=kx+b$. We therefore need to determine the coefficients $k$ and $b$, although, looking ahead, we do not really need $b$.

The coefficient $k$ is determined by:

$$ k = \frac {n \sum{x_i y_i} - \sum{x_i} \sum{y_i} } {n \sum {x^2_i} - (\sum {x_i})^2}  $$

$x_i$ are the coordinates of our receivers: 0 for the first, 1 for the second, since we agreed on a spacing of 1 meter.
$y_i$ are the measured arrival times multiplied by the speed of sound in water.

Another very important point: the coefficient $k$ is the tangent of the line's angle of inclination relative to the X axis.
Look again at the diagram above:

$$ tg \phi = \frac{\Delta t * V}{\Delta X} $$

And we recall that

$$ \frac{\Delta t * V}{\Delta X} = cos(\alpha) $$ 

This gives the interesting result that:

$$ tg \phi = cos \alpha = \frac{\Delta t * V}{\Delta X} $$

From this, we can easily calculate $\alpha$, the angle of arrival. Once again, here is the entire sequence of measurements and calculations:

1. Determine the arrival times at all elements of the transducer array
2. Use linear approximation to find the coefficient $k$ of the straight-line equation, which by definition is the tangent of its angle of inclination
3. Determine the angle of arrival as the arccosine of $k$

It is difficult to present all these data in an Excel chart or something similar, so we will use Matlab, or rather its free counterpart, [GNU Octave](https://octave.org).

It is convenient to save the data for processing in separate files "as is", in CSV format.
We will save them as `data1.csv`, `data2.csv`, `data3.csv`, `data4.csv` and `data5.csv`.

We have prepared the following script to process them:

```

clc;
clear all;
close all;

% Processing parameters
Num = 5;  % Data set number (1-5)

% Load data
data_1 = csvread('data1.csv');
data_2 = csvread('data2.csv');
data_3 = csvread('data3.csv');
data_4 = csvread('data4.csv');
data_5 = csvread('data5.csv');

actual_angles = [180, 135, 90, 45, 0];  % Actual angles for each data set

% Select data for processing
if (Num == 1) src_data = data_1;
elseif (Num == 2) src_data = data_2;
elseif (Num == 3) src_data = data_3;
elseif (Num == 4) src_data = data_4;
elseif (Num == 5) src_data = data_5;
endif

% Physical parameters
v = 1503.6;  % Speed of sound in water, m/s
t_scale = 1 / 1000000;  % Time scale (microseconds to seconds)

% Coordinates of the transducer array receivers (ULA)
ula4_xs = [3 2 1 0];
ula4_ys = [0 0 0 0];

% Create one window with two subplots
figure('Position', [100, 100, 1200, 600]);  % Larger window size

%% First plot: measurements and approximation
subplot(1, 2, 1);  % 1 row, 2 columns, position 1
axis equal
hold on
grid on

% Preliminary calculations for linear regression
x_sum = sum(ula4_xs);
x2_sum = sum(ula4_xs .^ 2);
x_sum2 = x_sum ^ 2;
rec_num = length(ula4_xs);

% Initialize arrays
k = zeros(length(src_data), 1);  % Slope coefficients
b = zeros(length(src_data), 1);  % Intercepts
alpha = zeros(length(src_data), 1);  % Angles of arrival

% Process each measurement
for n = 1:length(src_data)
    % Convert time delays to distances
    ys = src_data(n, :) .* t_scale .* v;

    % Check data validity
    if ~all(isfinite(ys))
        warning('Invalid data detected in row %d. Skipping.', n);
        continue;
    end

    % Plot measurements
    if n == 1
        plot(ula4_xs, ys, 'b.', 'DisplayName', 'Measurements V·t', 'MarkerSize', 4);
    else
        plot(ula4_xs, ys, 'b.', 'HandleVisibility', 'off', 'MarkerSize', 4);
    end

    % Calculate line coefficients (least squares method)
    y_sum = sum(ys);
    xy_sum = sum(ula4_xs .* ys);

    denominator = (rec_num * x2_sum - x_sum2);
    if denominator == 0
        warning('Degenerate system in row %d. Skipping.', n);
        continue;
    end

    k(n) = (rec_num * xy_sum - x_sum * y_sum) / denominator;
    b(n) = (y_sum - k(n) * x_sum) / rec_num;

    % Plot the fitted line
    x_range = [0, 3];
    y_range = k(n) * x_range + b(n);

    if n == 1
        line(x_range, y_range, 'Color', 'red', 'LineWidth', 0.5, 'DisplayName', 'Linear approximation');
    else
        line(x_range, y_range, 'Color', 'red', 'LineWidth', 0.5, 'HandleVisibility', 'off');
    end

    % Calculate the angle of arrival using arccosine
    k_bound = max(min(k(n), 1), -1);  % Clamp to the domain of acos
    alpha(n) = acos(-k_bound);
end

% Display receiver positions
plot(ula4_xs, ula4_ys, 'go', 'MarkerSize', 8, 'MarkerFaceColor', 'g', 'DisplayName', 'Array elements');

% Configure the first plot
tstr = sprintf("Linear approximation tgφ=cosα\nActual angle: %d°, sample: %d",...
               actual_angles(Num), length(src_data));
title(tstr, "fontsize", 14);
xlabel('X, m', "fontsize", 14);
ylabel('V·t, m', "fontsize", 14);

lh = legend('show');
set(lh, "fontsize", 12);

%% Second plot: angle histogram
subplot(1, 2, 2);  % 1 row, 2 columns, position 2

alpha_deg = rad2deg(alpha);  % Convert radians to degrees

% Angle statistics
mean_alpha = mean(alpha_deg);
std_alpha = std(alpha_deg);
max_alpha = max(alpha_deg);
min_alpha = min(alpha_deg);

% Plot the histogram
nbins = 20;
[counts, bins] = hist(alpha_deg, nbins);
hist(alpha_deg, nbins, 'DisplayName', 'α, °');
colormap(summer());

hold on;
y_limits = ylim;

% Statistical lines on the histogram
plot([mean_alpha, mean_alpha], y_limits, 'r-', 'LineWidth', 2,...
     'DisplayName', sprintf('Mean = %.1f°', mean_alpha));

plot([mean_alpha - std_alpha, mean_alpha - std_alpha], y_limits, 'g--',...
     'LineWidth', 1.5, 'DisplayName', sprintf('±1 SD (%.1f°)', std_alpha));
plot([mean_alpha + std_alpha, mean_alpha + std_alpha], y_limits, 'g--',...
     'LineWidth', 1.5, 'HandleVisibility', 'off');

% Configure the second plot
llh = legend('show');
set(llh, "fontsize", 12);

tstr = sprintf("Angle of arrival estimation\nActual angle: %d°, sample: %d",...
               actual_angles(Num), length(src_data));
title(tstr, "fontsize", 14);
xlabel('Angle α, °', "fontsize", 14);
ylabel('Frequency', "fontsize", 14);

% Print statistics to the console
fprintf('\n=== ANGLE STATISTICS ===\n');
fprintf('Mean: %.2f°\n', mean_alpha);
fprintf('SD: %.2f°\n', std_alpha);
fprintf('Minimum: %.2f°\n', min_alpha);
fprintf('Maximum: %.2f°\n', max_alpha);
fprintf('Range: %.2f°\n', max_alpha - min_alpha);

```

A couple of reminders:
- we measure angles counterclockwise from the horizontal.
- we have 5 data sets obtained at angles of 180, 135, 90, 45 and 0°.

Now let us look at the results.

For each relative position of the transducer array and source, we obtain two plots: one showing the measured arrival times and a line approximating these measurements, and the other a histogram of the calculated angle of arrival.

For an angle of 180°, the source is directly to the left of the array:

| <img src="https://github.com/user-attachments/assets/b6d81073-5b88-4ce3-9fda-f60392da5c36" width="480" /> |
| :---: |
| _Actual angle 180°_ |

| <img src="https://github.com/user-attachments/assets/7c58e653-6212-4c85-8a65-5f1beb1349bb" width="480" /> |
| :---: |
| _Actual angle 135°_ |

| <img src="https://github.com/user-attachments/assets/183bc4bb-ef78-4f40-b0cf-b55865812a9f" width="480" /> |
| :---: |
| _Actual angle 90°_ |

| <img src="https://github.com/user-attachments/assets/be7b7f95-b4f0-4d2f-afc5-b3719bbe9006" width="480" /> |
| :---: |
| _Actual angle 45°_ |

| <img src="https://github.com/user-attachments/assets/e65d0bfb-8300-4bc1-9c08-fd884cce6246" width="480" /> |
| :---: |
| _Actual angle 0°_ |

From the statistics we obtained, we can conclude that the prototype is fully functional overall, especially considering that a small pool is an extremely challenging "body of water" for such systems.

We can see that the standard deviation of the angle-of-arrival estimate is, on average, about 6°. The sample mean corresponds to the actual angle in every experiment except experiment No. 2 (135°). Particularly good results were obtained at 90° and 45°.

_How can this system be improved?_
First, ensure that the array elements (receivers) remain fixed by extending their cables and improving the frame.
Second, it would be interesting to see the results under more favorable conditions, such as in a small natural body of water.

> We suggest that advanced users explore the following issue independently: in our experiments, we assumed a plane wavefront. In reality, this assumption is valid only for angles of 180° and 0°, when the source lies on the array axis. Looking at the measurement plot for 90°, it is obvious that a circular arc would fit better than a line.
> Yes, this is more of a double-star challenge for beginners, but successfully solving it will earn you a well-deserved karma point.

Let us summarize:

- we estimated how much the detected signal arrival times fluctuate between receivers
- based on these data, we built an angle-measuring system using a 4-element transducer array
- we implemented a simple optimization solution based on linear approximation
- we conducted full-scale experiments in a small pool, confirming that the system works
- we evaluated the statistical properties of the result

Let us congratulate and praise ourselves for completing one of the most difficult projects in this manual — you are magnificent!








### 1.7. (In progress) Project 5 - Positioning a responder using a virtual long baseline

In this project, we will determine the geographic position — latitude and longitude — of a _stationary_ underwater object.
For this, we will build two transceivers, already familiar from [1.4. Project 2 - Assembling a transceiver and measuring slant range](#14-project-2---assembling-a-transceiver-and-measuring-slant-range). One will be the "underwater" object whose position we want to determine, and the other will be part of the measuring device.

How will we determine the object's geographic position — its latitude and longitude?

Recall that a measured range places the object on a sphere. If the vertical coordinate is known, it places it on a circle whose radius is determined by the measured range.
By measuring range from several points, we "draw" several such circles. The target object (the one we are looking for) will be at their intersection.

Now imagine measuring the range to an object from two different points, for example, from two ships or from the same ship at different times. Each measurement defines its own circle:

If the two circles touch at one point, that is ideal: the object is exactly there.
If they intersect at two points, we do not know which one is correct. Another measurement (another circle) is needed to choose the correct location.

In practice, measurements are always inaccurate, so the circles may not intersect at all — for example, if we used an underestimated speed of sound. We then seek a point that is "almost" equally distant from all the circles, i.e., the best approximation.

Such problems are called optimization (or minimization) problems: we seek the object position that best _agrees_ with all measurements.

Each pair of measurements from two different points forms a line: a measurement baseline, or simply a _baseline_. In our case, however, it is virtual rather than physical: measurements are taken sequentially, not simultaneously, from the same moving ship.

This method works only if the object is stationary. If it moves, it will change position while the ship moves to the next point, and we will measure distances to different positions of the object. The circles will then fail to converge, preventing correct positioning.

Clearly, we need two transceivers: we must _interrogate_ the object whose position we want to determine; it must _receive_ the request and then _emit_ a response signal, which must be _received_ by the interrogating or measuring device.

To establish a geographic reference, we need a GNSS receiver. We also need somewhere to output the results. At the simplest level, this is just a serial port connected to a PC; a display can also be used, or the measuring device can additionally be equipped with a radio modem.

Here is the list of what we need:

#### 1.7.1. Required equipment

| No.    | Name | Quantity | Note |
| :--- | :--- | :--- | :--- |
| 1    | Module [A<sup>3</sup>R](A3R_Datasheet_en.md) | 2 |  |
| 2    | Module [A<sup>3</sup>T](A3T_Datasheet_en.md) | 2 |  |
| 3    | Transceiving transducer [RT-1.332820-1](/documentation/EN/Transducers/RT_1_332820_1_Specification_en) | 2 |  |
| 4    | Any microcontroller board, for example, Arduino Nano | 2 |  |
| 5    | GNSS receiver, almost any model that can be connected to the microcontroller board used | 1 | |
| 6    | 433 MHz radio module, for example HC-12 or compatible | 2 | Optional |
| 7    | LCD display, for example MT-204S | 1 | Optional |
| 7    | Dupont Male-Female or Female-Female wires, 15+ cm | 8 | |

If you plan to build the version with the minimum functionality, the display and radio module are not required. All system results can then be output to the PC through the serial port.










### 1.8. (Planned) Project 6 - Long baseline navigation system

#### 1.8.1. (Planned) Required equipment

#### 1.8.2. (Planned) Navigation receiver buoy



## 2. (Planned) A<sup>3</sup>TC and A<sup>3</sup>RC

## 3. (Planned) A<sup>3</sup>T2 and A<sup>3</sup>R2

## 4. (Planned) A<sup>3</sup>AM


[Back to contents](#contents)

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/A3S/A3S_Users_Manual_ru.md commit=5e5766e3d53d20c67730cbadfd0ac0e2d4f33a9b date=2026-06-10 -->
