import packet

manager = packet.Manager(auth_token="smdAaUJ6RU2jAuEg518v5dde42LjMeiB")


# Gets and prints out all the available operating systems
def get_os():
    oss = manager.list_operating_systems()
    for os in oss:
        print(os)

# Checks if the inputted operating system from the user is valid
def check_os(opp):
    oss = manager.list_operating_systems()
    for os in oss:
        os_string = str(os)
        split = os_string.split()
        #ewr1print(split)
        if split[0] == opp:
            return True
    return False

# Gets and prints out all the available facilities
def get_facilities():
    facilities = manager.list_facilities()
    for facility in facilities:
        print(facility)

# Checks if the inputted facility from the user is valid
def check_facility(fac):
    facilities = manager.list_facilities()
    for facility in facilities:
        if str(facility) == fac:
            return True
    return False

# Creates a new device on the specifications of the user
def create_dev(host, fac, os):
    device = manager.create_device(project_id='ca73364c-6023-4935-9137-2132e73c20b4',
                               hostname= host,
                               plan='baremetal_1', facility= fac,
                               operating_system= os)
    return device

# Lists all the current devices of the project
def list_dev():
    devices = manager.list_devices(project_id='ca73364c-6023-4935-9137-2132e73c20b4')
    for device in devices:
        print(device)



# Main function where user can decide what to do
if __name__ == '__main__':
    print("What operating system do you want to use? Possible Options:")
    get_os()
    os = input("")
    # Checks to ensure that the operating system is valid
    while not check_os(os) :
        os = input("Invalid operating system, please enter a valid option:")

    print("What facility would you like?")
    get_facilities()
    facility = input("")
    # Checks to ensure that the facility is valid
    while not check_facility(facility):
        facility = input("Invalid facility, please enter a valid option:")

    hostname = input("What would you like the hostname to be?")

    # Creates a new device based on the inputted information
    device = create_dev(hostname, facility, os)
    print(device.id)

    # Prints the currently available devices
    print("Devices currently available:")
    list_dev()

    # Deletes the device and outputs the currently available devices
    device.delete()
    print("Devices currently available:")
    list_dev()
