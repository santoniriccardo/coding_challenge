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
        if str(os) == opp:
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
                               hostname='host',
                               plan='baremetal_1', facility='fac',
                               operating_system='os')

# Lists all the current devices of the project
def list_dev():
    devices = manager.list_devices(project_id='ca73364c-6023-4935-9137-2132e73c20b4')
    for device in devices:
        print(device)
