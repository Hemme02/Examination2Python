def get_port():
    while True:
        port_entered = input('Enter Port: ')
        if len(port_entered) == 0 or port_entered.isspace():
            print('Error. Port must be entered')
        else:
            return port_entered