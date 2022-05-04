from pathlib import Path

rootfolder = str(Path.home()/"AP_Debugger/")
downloads_path = str(Path.home() / "Downloads/")

path_target_list_by_version = \
    {
    '8.2.1-907' :
        {
            'path' :
                   {
                    'model' : '/tmp/lldpd.conf',
                    'power_source' : '/tmp/power_source',
                    'system_time' : '/tmp/sys_state_logs',
                    'mac_address' : '/tmp/eth_macs',
                    'hostname' : '/opt/sensor/sensor.conf',
                    'location' : '/opt/sensor/sensor.conf',
                    'ip_address' : '/opt/sysconfig/network-scripts/ifcfg-br0',
                    'status' : '/tmp/sys_state_logs',
                    'link_speed' : '/tmp/sensord_trigger/ethlink_info',
                    'last_upgraded' : '/opt/upgrade.log',
                    'last_booted' : '/tmp/reboot_log',
                    'capability' : '/tmp/led_status'
                  },
            'target' :
                    {
                    'model' : 'SYSTEM_NAME',
                    'power_source' : '',
                    'system_time' : 'Device Time',
                    'mac_address' : '',
                    'hostname' :'device_name=',
                    'location' :'location_identifier=',
                    'ip_address' :'IPADDR=',
                    'status' :'Sensor_Status',
                    'link_speed' :'LinkSpeed=',
                    'last_upgraded' :'',
                    'last_booted' :'',
                    'capability' :''
                    },
        },
    '8.8.3-12':
        {
            'path' :
                    {
                    'model': '/tmp/platform_info',
                    'power_source': '/tmp/power_source',
                    'system_time': '/tmp/sys_state_logs',
                    'mac_address': '/tmp/eth_macs',
                    'hostname': '/tmp/sensor.conf.debug',
                    'location': '/tmp/sensor.conf.debug',
                    'ip_address': '/opt/sysconfig/network-scripts/ifcfg-br0',
                    'status': '/tmp/sys_state_logs',
                    'link_speed': '/tmp/sensord_trigger/ethlink_info',
                    'last_upgraded': '/opt/upgrade.log',
                    'last_booted': '/tmp/reboot_log',
                    'capability': '/tmp/led_status'
                    },
            'target' :
                    {
                    'model' : 'SYSTEM_NAME',
                    'power_source' : '',
                    'system_time' : 'Device Time',
                    'mac_address' : '',
                    'hostname' :'device_name=',
                    'location' :'location_identifier=',
                    'ip_address' :'IPADDR=',
                    'status' :'Sensor_Status',
                    'link_speed' :'LinkSpeed=',
                    'last_upgraded' :'',
                    'last_booted' :'',
                    'capability' :''
                    },
        },
    '8.0.171':
        {
            'path' :
                    {
                    'model': '/tmp/lldpd.conf',
                    'power_source': '/tmp/power_source',
                    'system_time': '/tmp/sys_state_logs',
                    'mac_address': '/tmp/eth_macs',
                    'hostname': '/tmp/sensor.conf.debug',
                    'location': '/tmp/sensor.conf.debug',
                    'ip_address': '/opt/sysconfig/network-scripts/ifcfg-br0',
                    'status': '/tmp/sys_state_logs',
                    'link_speed': '/tmp/sensord_trigger/ethlink_info',
                    'last_upgraded': '/opt/upgrade.log',
                    'last_booted': '/tmp/reboot_log',
                    'capability': '/tmp/led_status'
                    },
            'target':
                    {
                    'model' : 'SYSTEM_NAME',
                    'power_source' : '',
                    'system_time' : 'Device Time',
                    'mac_address' : '',
                    'hostname' :'device_name=',
                    'location' :'location_identifier=',
                    'ip_address' :'IPADDR=',
                    'status' :'Sensor_Status',
                    'link_speed' :'LinkSpeed=',
                    'last_upgraded' :'',
                    'last_booted' :'',
                    'capability' :''
                    }
        },
    '11.0.1-49':
        {
            'path' :
                   {
                    'model' : '/tmp/lldpd.conf',
                    'power_source' : '/tmp/power_source',
                    'system_time' : '/tmp/sys_state_logs',
                    'mac_address' : '/tmp/eth_macs',
                    'hostname' : '/tmp/lldpd.conf',
                    'location' : '/opt/sensor/sensor.conf',
                    'ip_address' : '/opt/sysconfig/network-scripts/ifcfg-br0',
                    'status' : '/tmp/sys_state_logs',
                    'link_speed' : '/tmp/sensord_trigger/ethlink_info',
                    'last_upgraded' : '/opt/upgrade.log',
                    'last_booted' : '/tmp/reboot_log',
                    'capability' : '/tmp/led_status'
                  },
            'target' :
                    {
                    'model' : 'SYSTEM_DESCRIPTION',
                    'power_source' : '',
                    'system_time' : 'Device Time',
                    'mac_address' : '',
                    'hostname' :'SYSTEM_NAME=',
                    'location' :'location_identifier=',
                    'ip_address' :'IPADDR=',
                    'status' :'Sensor_Status',
                    'link_speed' :'LinkSpeed=',
                    'last_upgraded' :'',
                    'last_booted' :'',
                    'capability' :''
                    },
        },
    }