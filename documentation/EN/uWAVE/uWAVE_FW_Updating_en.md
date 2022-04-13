<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | Instructions for updating the firmware of uWave modems   |

<div style="page-break-after: always;"></div>

# Updating the firmware of uWave modems

>We are constantly working to improve products, take into account the opinions and wishes of users and eliminate the identified shortcomings. Version history, new feature additions, and bug fixes can be found on the [uWave: Version and Changes History](uWAVE_version_history_en.md) page.

## Step 1 
Download the necessary utilities.

### Step 1.1 
Download the demo app [uWave Host](https://github.com/ucnl/uWAVE_Host/releases/download/1.0/uWAVE_Host.zip) to work with uWave modems. The application runs on a PC running Windows OS (Version 8 and above).

### Step 1.2 
Download the firmware update utility [UCNL_FW_Update](https://github.com/ucnl/UCNL_FW_Update/releases/download/1.1/UCNL_FW_Update.zip). The utility works on a PC running OC Windows (Version 8 and higher).

### Step 1.3 
Just unpack the downloaded archives into folders convenient for you. Both applications do not require installation.

## Step 2
Prepare everything to connect the modem to the PC.

### Step 2.1 
Connect your modem to the **UART<->USB** converter. The purpose of the cable cores by color is shown below:

| ![uWAVE_wiring_diagram_en](/documentation/uWAVE_wiring_diagram_en.png) |
| :---: |
| Fig 1. Functions of cable cores |

The voltage on the data lines **MUST NOT** exceed 3.3 V.
For the initial switching of the modem to the command mode, it is necessary to provide for the possibility of tightening the SVC / CMD wire to a voltage of 3.3 or 5 Volts. It is convenient to do this with a jumper.

### Step 2.2 
Provide the ability to conveniently turn on and off the command mode according to the diagrams below.

| ![uwave_usb_cmd_mode_off](/documentation/uwave_usb_cmd_mode_off.png) |
| :---: |
| Fig 2. Connecting a modem to a PC USB port using an interface converter. **Command mode OFF** |

| ![uwave_usb_cmd_mode_on](/documentation/uwave_usb_cmd_mode_on.png) |
| :---: |
| Fig 3. Connecting a modem to a PC USB port using an interface converter. **Command mode ON** |


## Step 3
Connecting the device to the USB port of the PC.

### Step 3.1 
Make sure that the command mode is not enabled (jumper removed, **SVC/CMD** wire pulled to GND- as shown in the diagram in Fig. 2).

### Step 3.2 
Connect the modem to the USB port of the PC using a converter:

| ![uwave_and_uart_usb_converter3](/documentation/uwave_and_uart_usb_converter3.png) |
| :---: |
| Fig 4. Modem is connected to a PC |

## Step 4
Enabling the **Command mode by default** setting.

### Step 4.1 
Start the [uWave Host](https://github.com/ucnl/uWAVE_Host/releases/download/1.0/uWAVE_Host.zip) application.

### Step 4.2 
Press the **SETTINGS** button on the top toolbar.

### Step 4.3 
In the settings window that opens, select the desired port and click the **OK** button.

| ![uwave_host1](/documentation/uwave_host1.png) |
| :---: |
| Fig 5. Selecting right port |

### Step 4.4
The application will prompt to restart it to apply the new settings - confirm by pressing the **OK** button.

### Step 4.5 
After restarting the application, press the **CONNECT** button.
If the application was able to successfully open the port, the **CONNECT** button will become highlighted and change its name to **DISCONNECT** and a corresponding message will be displayed in the **HISTORY WINDOW** text box.

If any error occurs, check that the correct port has been selected and return to [Step 4.2](#step-42) if necessary.

### Step 4.6
Press the **COMMAND MODE** button, thereby informing the application that you are going to work with the modem in command mode.

### Step 4.7
Put the modem into command mode by pulling the **SVC/CMD** wire to 3.3 or 5 Volts.

### Step 4.8
Press the **QUERY** button on the **DEVICE INFO** tab. If everything is done correctly, then in the **HISTORY WINDOW** windows and the text field on the **DEVICE INFO** tab, the corresponding information will be displayed, for example, as in Figure 6.

| ![uwave_host2](/documentation/uwave_host2.png) |
| :---: |
| Fig 6. Reading settings and enabling the "Command mode by default" settings |

Make sure the **Command mode by default** checkbox is checked. If not, install it and press the **APPLY** button to change the modem settings.

If it doesn't, close the port by pressing the **DISCONNECT** button and go to [Step 4.2](#step-42). If the port is selected correctly, make sure that the **SVC/CMD** wire was pulled to GND when power was supplied to the modem, i.e. go to [Step 3](#step-3).

### Step 4.9
Close [uWave Host](https://github.com/ucnl/uWAVE_Host/releases/download/1.0/uWAVE_Host.zip) application.

### Step 4.10
Pull the **SVC/CMD** conductor to the GND.

## Step 5
Updating device firmware

### Step 5.1
If you do not have a firmware file for this modem, please contact the [developer](mailto:support@unavlab.com) for a firmware file. In the letter, place the serial number of the device:

| ![uwave_host3](/documentation/uwave_host3.png) |
| :---: |
| Fig 7. Serial number of the device in **DEVICE INFO** tab |

### Step 5.2
Start the [UCNL_FW_Update](https://github.com/ucnl/UCNL_FW_Update/releases/download/1.1/UCNL_FW_Update.zip) utility.

### Step 5.3
Connect the modem to the PC via the interface converter as shown in [Step 3](#step-3), making sure the **SVC/CMD** wire is pulled to GND before connecting.

### Step 5.4
In the **Port** Combobox, select the appropriate port for the device.

### Step 5.5
Select the appropriate firmware file for the device by pressing the **Load** button.
The rest of the utility interface controls should look like in Figure 8.:

| ![ucnl_fw_update1](/documentation/ucnl_fw_update1.png) |
| :---: |
| Fig 8. Preparing the **UCNL_FW_Update** utility for flashing the **uWave** modem |

### Step 5.6
Start the firmware update process by pressing the **Start** button.

If:
* port is correct
* the state of the interface elements before the start corresponded to Figure 8
* the firmware file corresponds to the serial number of the device
* before powering up the device, the **SVC/CMD** wire was pulled to the GND

Then, the bottom text box will start to display the progress of the firmware update, as shown in Figures 9 to 11.

| ![ucnl_fw_update2](/documentation/ucnl_fw_update2.png) |
| :---: |
| Fig 9. Firmware update start |

| ![ucnl_fw_update3](/documentation/ucnl_fw_update3.png) |
| :---: |
| Fig 10. Downloading the update to the device |

| ![ucnl_fw_update4](/documentation/ucnl_fw_update4.png) |
| :---: |
| Fig 11. Firmware update completed successfully |

### Step 5.7
Close the application and disconnect the modem from the PC. Update completed.

If the device firmware update fails, check the following reasons:

* port selected incorrectly
* the state of the interface elements before the start did not match Figure 8
* the firmware file does not match the serial number of the device
* before powering up the device, the **SVC/CMD** wire was not connected to GND
* the connection was broken during the firmware update

If the update fails, [contact the developer](mailto:support@unavlab.com)

<div style="page-break-after: always;"></div>
