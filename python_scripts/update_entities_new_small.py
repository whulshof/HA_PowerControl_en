entities = hass.states.entity_ids('switch')
all_switches = ["Select"]
for e in entities:
   if e.startswith("switch.switch") : all_switches.append(e)

service_data = {'entity_id': 'input_select.load_switch_1', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_2', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_3', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_4', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_5', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)

entities = hass.states.entity_ids('sensor')
all_sensor = ["Select"]
for e in entities:
   if e.startswith("sensor.power") : all_sensor.append(e)
   
service_data = {'entity_id': 'input_select.power_load_1', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_2', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_3', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_4', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_5', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)

service_data = {'entity_id': 'input_select.power_load', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
