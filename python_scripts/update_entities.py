
entities = hass.states.entity_ids('switch')
all_switches = ["Select"]
for e in entities:
    all_switches.append(e)

entities = hass.states.entity_ids('light')
for e in entities:
    all_switches.append(e)


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
service_data = {'entity_id': 'input_select.load_switch_6', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_7', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_8', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_9', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_10', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_11', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_12', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_13', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_14', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_15', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_16', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_17', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_18', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_19', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_switch_20', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)

entities = hass.states.entity_ids('sensor')
all_sensor = ["Select"]
for e in entities:
    all_sensor.append(e)

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
service_data = {'entity_id': 'input_select.power_load_6', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_7', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_8', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_9', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_10', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_11', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_12', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_13', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_14', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_15', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_16', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_17', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_18', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_19', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.power_load_20', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)

service_data = {'entity_id': 'input_select.power_load', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
