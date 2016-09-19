from subprocess import check_output

def uptime():
    return check_output(['uptime']).decode('utf8')
