# Sources
# https://github.com/cmroche/greeclimate/tree/master

from greeclimate.discovery import Discovery
from greeclimate.device import Device, Mode, FanSpeed, TemperatureUnits, HorizontalSwing, VerticalSwing
 
discovery = Discovery()
for device_info in await discovery.scan(wait_for=5):
    try:
        device = Device(device_info)
        await device.bind() # Device will auto bind on update if you omit this step
    except Exception as e:
        print("Unable to bind to gree device: %s", device_info)
        continue
 
    print(
        "Adding Gree device at %s:%i (%s)",
        device.device_info.ip,
        device.device_info.port,
        device.device_info.name,
    )
    ip = device.device_info.ip
    port = device.device_info.port
    mac = device.device_info.mac
    name = device.device_info.name
    #device = Device(ip, mac, name, port)
   
    device.power = True
    device.mode = Mode.Auto
    device.target_temperature = 25
    device.temperature_units = TemperatureUnits.C
    device.fan_speed = FanSpeed.Auto
    device.fresh_air = True
    device.xfan = True
    device.anion = True
    device.sleep = True
    device.light = True
    device.horizontal_swing = HorizontalSwing.FullSwing
    device.vertical_swing = VerticalSwing.FullSwing
    device.quiet = True
    device.turbo = True
    device.steady_heat = True
    device.power_save = True
    device.target_humidity = 45
 
    # Send the state update to the HVAC
    await device.push_state_update()