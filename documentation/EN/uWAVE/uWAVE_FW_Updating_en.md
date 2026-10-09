[Main](/) ❯ [Underwater acoustic modems](/underwater_acoustic_modems_en) ❯ **uWave: Firmware update guide**

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

| ![logo](/documentation/sm_logo.png) | |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | Firmware update guide for uWave modems  |

<div style="page-break-after: always;"></div>

# Updating the firmware of uWave modems

> We are constantly working to improve our products, taking into account the opinions and wishes of users and eliminating the shortcomings we find. You can find the version history, new features and bug fixes on the page [uWave: Version history & changes](uWAVE_version_history_en.md).

## Step 1 
Download the necessary utilities.

### Step 1.1 
Download the demo application [uWave Host](https://github.com/ucnl/uWAVE_Host/releases/download/1.0/uWAVE_Host.zip) to work with uWave modems. The application runs on a PC under Windows OS (version 8 or later).

### Step 1.2 
Download the firmware update utility [UCNL_FW_Update](https://github.com/ucnl/UCNL_FW_Update/releases/download/1.1/UCNL_FW_Update.zip). The utility runs on a PC under Windows OS (version 8 or later).

### Step 1.3 
Simply unpack the downloaded archives into folders of your choice. Neither application requires installation. 

## Step 2
Prepare everything for connecting the modem to the PC.

### Step 2.1 
Connect your modem to a **UART<->USB** converter. The wire assignment by color is shown below:  

| ![uWAVE_wiring_diagram_en](/documentation/uWAVE_wiring_diagram_en.png) |
| :---: |
| Figure 1. Cable wire assignment |

The voltage on the data lines **MUST NOT** exceed 3.3 V. 
To switch the modem to command mode initially, provide a means of pulling the SVC/CMD wire up to a voltage of 3.3 or 5 V. This is conveniently done with a jumper.

### Step 2.2 
Provide a convenient way of switching the command mode on and off, as shown in the diagrams below.

| ![uwave_usb_cmd_mode_off](/documentation/uwave_usb_cmd_mode_off.png) |
| :---: |
| Figure 2. Connecting the modem to the PC USB port using an interface converter. **Command mode off** |

| ![uwave_usb_cmd_mode_on](/documentation/uwave_usb_cmd_mode_on.png) |
| :---: |
| Figure 3. Connecting the modem to the PC USB port using an interface converter. **Command mode on** |


## Step 3
Connect the device to the PC USB port.

### Step 3.1 
Make sure that the command mode is not enabled (the jumper is removed, the **SVC/CMD** wire is pulled to ground - as shown in the diagram in Fig. 2) 

### Step 3.2 
Connect the modem to the PC USB port using the converter:

| ![uwave_and_uart_usb_converter3](/documentation/uwave_and_uart_usb_converter3.png) |
| :---: |
| Figure 4. The modem is connected to the PC |

## Step 4
Enable the **Command mode by default** setting.

### Step 4.1 
Launch the [uWave Host](https://github.com/ucnl/uWAVE_Host/releases/download/1.0/uWAVE_Host.zip) application

### Step 4.2 
Press the **SETTINGS** button on the top toolbar. 

### Step 4.3 
In the settings window that opens, select the required port and press the **OK** button. 

| ![uwave_host1](/documentation/uwave_host1.png) |
| :---: |
| Figure 5. Selecting the port |

### Step 4.4
The application will prompt you to restart it to apply the new settings - confirm by pressing the **OK** button.

### Step 4.5 
After the application restarts, press the **CONNECT** button. 
If the application has successfully opened the port, the **CONNECT** button will become highlighted and change its name to **DISCONNECT**, and a corresponding message will be displayed in the **HISTORY WINDOW** text box.

If any error occurs, make sure that the port has been selected correctly and, if necessary, return to [Step 4.2](#step-42).

### Step 4.6
Press the **COMMAND MODE** button, thereby informing the application that you are going to work with the modem in command mode.

### Step 4.7
Put the modem into command mode by pulling the **SVC/CMD** wire up to 3.3 or 5 V.

### Step 4.8
Press the **QUERY** button on the **DEVICE INFO** tab. If everything is done correctly, the corresponding information will be displayed in the **HISTORY WINDOW** and in the text field on the **DEVICE INFO** tab, for example, as in Figure 6. 

| ![uwave_host2](/documentation/uwave_host2.png) |
| :---: |
| Figure 6. Reading the settings and setting the command mode by default |

Make sure that the **Command mode by default** checkbox is checked. If it is not, check it and press the **APPLY** button to change the modem settings.

If this does not happen, close the port by pressing the **DISCONNECT** button and go to [Step 4.2](#step-42). If the port is selected correctly after all, make sure that the **SVC/CMD** wire was pulled to "ground" at the moment power was applied to the modem, i.e. go to [Step 3](#step-3).

### Step 4.9
Close the [uWave Host](https://github.com/ucnl/uWAVE_Host/releases/download/1.0/uWAVE_Host.zip) application

### Step 4.10
Pull the **SVC/CMD** wire to "ground".

## Step 5
Updating the device firmware

### Step 5.1
If you do not have a firmware file for this modem, contact [technical support](mailto:support@unavlab.com) to obtain the firmware file. In the e-mail, state the serial number of the device:

| ![uwave_host3](/documentation/uwave_host3.png) |
| :---: |
| Figure 7. Serial number of the device in the **DEVICE INFO** window |

### Step 5.2
Launch the [UCNL_FW_Update](https://github.com/ucnl/UCNL_FW_Update/releases/download/1.1/UCNL_FW_Update.zip) utility.

### Step 5.3
Connect the modem to the PC via the interface converter, as shown in [Step 3](#step-3), making sure before connecting that the **SVC/CMD** wire is pulled to "ground".

### Step 5.4
In the **Port** drop-down list, select the port corresponding to the device.

### Step 5.5
Select the firmware file corresponding to the device by pressing the **Load** button. 
The remaining controls of the utility interface should look as in Figure 8:

| ![ucnl_fw_update1](/documentation/ucnl_fw_update1.png) |
| :---: |
| Figure 8. Preparing the **UCNL_FW_Update** utility for reflashing the **uWave** modem |

### Step 5.6
Start the firmware update process by pressing the **Start** button. 

If:  
* the port is selected correctly
* the state of the interface elements before the start corresponded to Figure 8
* the firmware file corresponds to the serial number of the device
* before power was applied to the device, the **SVC/CMD** wire was pulled to ground

Then the progress of the firmware update will start to be displayed in the bottom text field, as shown in Figures 9–11.

| ![ucnl_fw_update2](/documentation/ucnl_fw_update2.png) |
| :---: |
| Figure 9. Start of the firmware update |

| ![ucnl_fw_update3](/documentation/ucnl_fw_update3.png) |
| :---: |
| Figure 10. Uploading the update to the device |

| ![ucnl_fw_update4](/documentation/ucnl_fw_update4.png) |
| :---: |
| Figure 11. Firmware update completed successfully |

### Step 5.7
Close the application and disconnect the modem from the PC. The update is complete.

If the device firmware update cannot be performed, check the following possible causes:

* the port was selected incorrectly
* the state of the interface elements before the start did not correspond to Figure 8
* the firmware file does not correspond to the serial number of the device
* before power was applied to the device, the **SVC/CMD** wire was not pulled to ground
* the connection was interrupted during the firmware update

If the update cannot be performed, [contact technical support](mailto:support@unavlab.com).

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/uWAVE/uWAVE_FW_Updating_ru.md commit=5e5766e3d53d20c67730cbadfd0ac0e2d4f33a9b date=2026-06-10 -->
