# HA_PowerControl

The following package, combined with the python script "update_entities.py" aims to avoid the detachment of the meter due to too much power absorbed by the various appliances (loads).
A fundamental hardware requirement is the presence of switches on the loads to be controlled and a sensor that measures the power of the individual loads. 
I used Shelly 1PM and Shelly Plug S devices, perfect for the purpose.
It is recommended, but not mandatory, to use a sensor that monitors the overall consumption of the system (eg Shelly EM or an ESP8266 + PZEM).
The logic envisages the configuration of two maximum power thresholds and two intervention times (which reflect the operating logic of the electricity meters used in Italy):
- if the overall absorption exceeds the value of "Maximum Delayed Power", the package waits for the value in minutes of "Delayed Detachment Minutes", after which it starts to disconnect the loads;
- if the overall absorption exceeds the value of "Immediate maximum power", wait for a number of seconds set in "Seconds immediate detachment" and then start the detachment.

The disconnection of the loads that are absorbing energy starts from those with lower priority (Load 20) up to those with higher priority (Load 1), until the overall use of power is within the set limit. If a load is not absorbing, it is not detached.
The script keeps memory of the load absorption before the detachment and reconnects it only when the availability of power is sufficient not to cause a new detachment, in reverse priority order (from Load 1 to Load 20).
The configuration is entirely via graphical interface, except for the notification group (notify.tutti) which must be set manually.

# Installing

- Copy the file "packages/pc.yaml" to the "packages" directory
- Copy the files "python_scripts/update_entities.py" and "python_scripts/update_entities_new.py" to the "python_scripts" directory
- Alternatively, you can download the ZIP file and extract the contents of the "HA_PowerControl-main" folder to the Home Assistant folder.
- [Enable packages](https://www.home-assistant.io/docs/configuration/packages/)
- [Enable python scripts](https://www.home-assistant.io/integrations/python_script/)
- Add the contents of the file "pc.lovelace" to the Lovelace interface.
- Create a notification group "notify.tutti" in the file "configuration.yaml" and insert the devices that will receive the intervention notifications.
- [Configure the recoder](https://www.home-assistant.io/integrations/recorder/) to include the following sensors:
  - sensor.selected_power_loads
  - sensor.suspended_power_loads
  - sensor.maximum_power

# Configuration
Set the configuration parameters of the Lovelace graphical interface.

# Power Load Sensor
The most effective solution is to use a power sensor upstream of the system, just before the meter. In this case, simply select the appropriate sensor in the configuration.
Alternatively, it is possible to use the power sensors of the increased loads used (sensor.virtual_power_load) and maintain a certain margin of tolerance.
This involves monitoring all major loads (oven, stove, hair dryer, air conditioners, etc ...).
Of course, in this way the overall consumption cannot be assessed, so the limit value could be exceeded without load control intervening.
But using a conservative maximum power value (e.g. 3kW) and counting on the tolerances of 180 minutes up to 33% (e.g. 4kW) should be functional.

# Screenshot
![image](https://user-images.githubusercontent.com/7837288/107847400-773a8c80-6deb-11eb-9c08-90e9998ffe08.png)
![1](https://user-images.githubusercontent.com/7837288/212674703-2ba39593-9dea-4e0d-8f14-76562bd82f96.png)

# Debug

It is possible to activate the writing of log messages by enabling the relative component in the [logger section](https://www.home-assistant.io/integrations/logger/) of the configuration.yaml configuration file:
'''python
Logger:
 default: error
 Logs:
 homeassistant.components.pc: debugging
```