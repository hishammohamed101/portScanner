import socket

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
targ = input("what is your ip :")


def portscan(port):
    try:
        con = so.connect(targ, port)
        return True
    except:
        return False



for i in range(30):
    if portscan(i):
        print("Post number : {} is open :)".format(i))
