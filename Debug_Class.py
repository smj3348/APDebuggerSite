import dir_paths
import os, sys, tarfile
import pprint

class Debug_Log:

    def __init__(self,filename):
        # need --- create user input for either popup file explorer or text-based-path to replace the statically written "path_to_debug_log_file".
        #self.tar_file_path = input("Enter name of tarzip file\nPlease ensure the file is located within your Download folder or within your 'AP_Debugger' folder\n")
        self.tar_file_path = filename
        if self.tar_file_path[-4:] == ".tgz":  ####if the filepath contains .tgz, tar_file
            self.tar_file = self.tar_file_path
            self.tar_file_path = self.tar_file_path[:-4]
        else:
            self.tar_file = self.tar_file_path + ".tgz"
        self.fileinput = dir_paths.rootfolder + '/' + str(self.tar_file_path)
        self.extract(self.tar_file)
        self.version = self.version()
        try:
            self.filepath_location = dir_paths.path_target_list_by_version[self.version]['path']
            self.filepath_target = dir_paths.path_target_list_by_version[self.version]['target']
        except KeyError:
            print("\n\nThis firmware version is likely not yet accounted for within the Debug Logger code.\nPlease add the firmware paths and targets to the dir_paths.py file.\n(You can copy a similar/close version to see if it works)")
        try:
            self.model = self.model()
        except KeyError:
            print("Firmware version is:  " + self.version)
            sys.exit()
        self.power_source = self.power_source()
        self.system_time = self.system_time()
        self.mac_address = self.mac_address()
        self.hostname = self.hostname()
        self.location = self.location()
        self.status = self.status()
        self.ip_address = self.ip_address()
        self.link_speed = self.link_speed()
        self.last_upgraded = self.last_upgraded()
        self.last_booted = self.last_booted()
        self.capability = self.capability()

    def extract(self , tar_file):
        try:
            individual_debuglog_path = dir_paths.downloads_path + '/' + str(tar_file)
            target_extract_path = dir_paths.rootfolder + '/' + str(tar_file)
            file = tarfile.open(individual_debuglog_path)
            os.mkdir(target_extract_path[:-4])
            file.extractall(target_extract_path[:-4])
            file.close()
        except FileExistsError:
            print('File/folder already exists, skipping file & folder creation.')

    def version(self):
        versionpath = self.tar_file_path + '/opt/sensor/version'
        with open(dir_paths.rootfolder + "/" + versionpath, 'r') as readfile:
            for line in readfile:
                checkline = line.split(':')
                if checkline[0] == "BUILD_NO":
                    ap_fw_version = checkline[1].strip()
        return ap_fw_version

    def model(self):
        try:
            with open(self.fileinput + dir_paths.path_target_list_by_version[self.version]['path']['model'], 'r') as readfile:
                for line in readfile:
                    checkline = line.split('=')
                    if checkline[0] == dir_paths.path_target_list_by_version[self.version]['target']['model']:
                        ap_model = checkline[1].strip().replace('Mojo AP/Sensor Combo' ,'').replace('AirTight AP/Sensor ', '')
            return ap_model
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            print('\nError returning model:\n     if checkline[0] == "SYSTEM_NAME":\n     ap_model = checkline[1].strip().replace("Mojo AP/Sensor Combo" ,'')\nIn '+ dir_paths.path_target_list_by_version[self.version]['path']['model'])
            print("Exception type: ", exception_type)
            print("Line number: ", line_number)
            return 'Error / Unknown'

    def power_source(self):
        try:
            with open(self.fileinput + dir_paths.path_target_list_by_version[self.version]['path']['power_source'], 'r') as readfile:
                power_source = readfile.readline().strip()
            return power_source
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            print('\nError returning power_source:\npower_source = readfile.readline().strip()\nIn '+ dir_paths.path_target_list_by_version[self.version]['path']['power_source'])
            print("Exception type: ", exception_type)
            print("Line number: ", line_number)
            return 'Error / Unknown'

    def system_time(self):
        try:
            with open(self.fileinput + dir_paths.path_target_list_by_version[self.version]['path']['system_time'], 'r') as readfile:
                for line in readfile:
                    if "Device Time" in line:
                        system_time = line[16:].strip()
            return system_time
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            print('\nError returning power_source:\npower_source = readfile.readline().strip()\nIn '+ dir_paths.path_target_list_by_version[self.version]['path']['system_time'])
            print("Exception type: ", exception_type)
            print("Line number: ", line_number)
            return 'Error / Unknown'

    def mac_address(self):
        try:
            with open(self.fileinput + dir_paths.path_target_list_by_version[self.version]['path']['mac_address'], 'r') as readfile:
                line = readfile.readline()
                mac_addr = line[5:].strip()
            return mac_addr
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            print('\nError returning mac_address:\npower_source = readfile.readline().strip()\nIn '+ dir_paths.path_target_list_by_version[self.version]['path']['mac_address'])
            print("Exception type: ", exception_type)
            print("Line number: ", line_number)
            return 'Error / Unknown'

    def hostname(self):
        try:
            with open(self.fileinput + dir_paths.path_target_list_by_version[self.version]['path']['hostname'], 'r') as readfile:
                for line in readfile:
                    if dir_paths.path_target_list_by_version[self.version]['target']['hostname'] in line:
                        device_name = line[12:].strip()
            return device_name
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            print('\nError returning link_speed:\n     if "device_name=" in line:\n     device_name = line[12:].strip()\nIn '+ dir_paths.path_target_list_by_version[self.version]['path']['hostname'])
            print("Exception type: ", exception_type)
            print("Line number: ", line_number)
            return 'Error / Unknown'


    def location(self):
        try:
            with open(self.fileinput + dir_paths.path_target_list_by_version[self.version]['path']['location'], 'r') as readfile:
                for line in readfile:
                    if "location_path=" in line:
                        device_location = line[14:].strip()
                    if "location_identifier=" in line:
                        device_location = line[14:].strip()
            return device_location
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            print('\nError returning location:\n     location_path= //or// location_identifier= in line:\n     device_location = line[14:].strip()]\nIn ' + dir_paths.path_target_list_by_version[self.version]['path']['location'])
            print("Exception type: ", exception_type)
            print("Line number: ", line_number)
            return 'Error / Unknown'

    def status(self):
        try:
            with open(self.fileinput + dir_paths.path_target_list_by_version[self.version]['path']['status'], 'r') as readfile:
                for line in readfile:
                    if "Sensor_Status" in line:
                        break
                content = readfile.readline().strip()
            return content
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            print('\nError returning status:' + '\n     if "Sensor_Status" in line:\n     break\n     content = readfile.readline().strip()\nIn '+ dir_paths.path_target_list_by_version[self.version]['path']['status'])
            print("Exception type: "+ str(exception_type))
            print("Line number: "+ str(line_number))
            return 'Error / Unknown'

    def ip_address(self):
        try:
            with open(self.fileinput + dir_paths.path_target_list_by_version[self.version]['path']['ip_address'], 'r') as readfile:
                for line in readfile:
                    if "IPADDR=" in line:
                        device_ip_addr = line[7:].strip()
            return device_ip_addr
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            print('\nError returning ip_address:\n     if "IPADDR=" in line:\n     device_ip_addr = line[7:].strip()\nIn '+ dir_paths.path_target_list_by_version[self.version]['path']['ip_address'])
            print("Exception type: ", exception_type)
            print("Line number: ", line_number)
            return 'Error / Unknown'

    def link_speed(self):
        try:
            with open(self.fileinput + dir_paths.path_target_list_by_version[self.version]['path']['link_speed'], 'r') as readfile:
                for line in readfile:
                    if "LinkSpeed=" in line:
                        link_speed = line[10:].strip()
            return link_speed
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            print('\nError returning link_speed:\n     if "LinkSpeed=" in line:\n     link_speed = line[10:].strip()\nIn '+ dir_paths.path_target_list_by_version[self.version]['path']['link_speed'])
            print("Exception type: ", exception_type)
            print("Line number: ", line_number)
            return 'Error / Unknown'

    def last_upgraded(self):
        try:
            with open(self.fileinput + dir_paths.path_target_list_by_version[self.version]['path']['last_upgraded'], 'r') as readfile:
                last_line = readfile.readlines()[-1].strip()
            return last_line
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print('\nError returning last_upgraded:\nlast_line = readfile.readlines()[-1].strip()\nIn ' + dir_paths.path_target_list_by_version[self.version]['path']['last_upgraded'])
            print("Exception type: ", exception_type)
            print("Line number: ", line_number)
            return 'Error / Unknown'

    def last_booted(self):
        try:
            with open(self.fileinput + dir_paths.path_target_list_by_version[self.version]['path']['last_booted'], 'r') as readfile:
                last_line = readfile.readlines()[-1][1:25].strip()
            return last_line
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print('\nError returning last_booted:\nlast_line = readfile.readlines()[-1][1:25].strip()\nIn ' + dir_paths.path_target_list_by_version[self.version]['path']['last_booted'])
            print("Exception type: ", exception_type)
            print("Line number: ", line_number)
            return 'Error / Unknown'

    def capability(self):
        try:
            with open(self.fileinput + dir_paths.path_target_list_by_version[self.version]['path']['capability'], 'r') as readfile:
                device_capability = readfile.readline().strip()[15:]
            return device_capability
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print('\nError returning capability:\ndevice_capability = readfile.readline().strip()[15:]\nIn ' + dir_paths.path_target_list_by_version[self.version]['path']['capability'])
            print("Exception type: ", exception_type)
            print("Line number: ", line_number)
            return 'Error / Unknown'

    def cpu_usage(self):
        pass

    def memory_usage(self):
        pass


