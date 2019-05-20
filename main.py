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
