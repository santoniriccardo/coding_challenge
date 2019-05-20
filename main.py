import packet

manager = packet.Manager(auth_token="smdAaUJ6RU2jAuEg518v5dde42LjMeiB")

def get_os():
    oss = manager.list_operating_systems()
    for os in oss:
        print(os)

def check_os(opp):
    oss = manager.list_operating_systems()
    for os in oss:
        if str(os) == opp:
            return True
    return False

def get_facilities():
    facilities = manager.list_facilities()
    for facility in facilities:
        print(facility)

def check_facility(fac):
    facilities = manager.list_facilities()
    for facility in facilities:
        if str(facility) == fac:
            return True
    return False

def create_dev(host, fac, os):
    device = manager.create_device(project_id='ca73364c-6023-4935-9137-2132e73c20b4',
                               hostname='host',
                               plan='baremetal_1', facility='fac',
                               operating_system='os')


def list_dev():
    devices = manager.list_devices(project_id='ca73364c-6023-4935-9137-2132e73c20b4')
    for device in devices:
        print(device)
