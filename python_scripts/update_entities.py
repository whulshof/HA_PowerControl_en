
entities = hass.states.entity_ids('switch')
all_switches = ["Selected"]
for e in entities:
    all_switches.append(e)

service_data = {'entity_id': 'input_select.load_1_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_2_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_3_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_4_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_5_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_6_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_7_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_8_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_9_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_10_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_11_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_12_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_13_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_14_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_15_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_16_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_17_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_18_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_19_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)
service_data = {'entity_id': 'input_select.load_20_switch', 'options': sorted(all_switches)}
hass.services.call('input_select', 'set_options', service_data)

entities = hass.states.entity_ids('sensor')
all_sensor = ["Selected"]
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

service_data = {'entity_id': 'input_select.power_loads', 'options': sorted(all_sensor)}
hass.services.call('input_select', 'set_options', service_data)
