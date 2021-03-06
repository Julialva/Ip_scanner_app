import socket


def socket_test(ip, port):
    some_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    location = (ip, port)
    result_of_check = some_socket.connect_ex(location)

    if result_of_check == 0:
        some_socket.shutdown(socket.SHUT_RDWR)
        some_socket.close()
        return "Connection to " + str(ip) + " was successful..."  # port open
    else:
        return "Connection to " + str(ip) + " failed..."  # port closed


# print(socket_test("192.168.0.22",22)) should print 0 on home lan
