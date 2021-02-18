# NRX Multichannel Example

This example performs simultaneous Time Gate measurements on `Channel B` and `Channel E`, then prints the result.

## Equipment

-   R&S SMB100A Vector Signal Generator
-   R&S NRX Power Meter

## Connections

![schematic](doc/images/schematic.png)

## SMB100A RF Output

Running `smb_setup.py` yields the following pulse-modulated RF setup:

![SMB100A Screenshot](doc/images/smb100a-screenshot.png)

![Pulse modulation settings](doc/images/smb100a-pulse-modulation.png)

## Measurement Settings

The following NRX settings are used.

### Display

There are two identical measurements.

![NRX Screenshot](doc/images/nrx-screenshot.png)

### Time Gate Mode

The measurements use a `Time Gate` that corresponds to `RF High`.

![Time Gate settings](doc/images/nrx-time-gate.png)

### Trigger

![Trigger](doc/images/nrx-trigger.png)

## Results

I ran the script and measured the following:

![main output](doc/images/main-output.png)
