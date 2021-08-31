import socket

import scapy.all as scapy


class sweeper:
    def __init__(self, net_ip):
        self.net_ip = net_ip

    def run(self):
        sweep_result = self.__scan(self.net_ip)
        sweep_result_final = self.__find_hostnames()
        return sweep_result_final

    def __scan(self, ip):
        arp_req_frame = scapy.ARP(pdst=ip)

        broadcast_frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

        broadcast_arp_req_frame = broadcast_frame / arp_req_frame

        answered_list = scapy.srp(broadcast_arp_req_frame, timeout=1, verbose=False)[0]
        result = []
        for i in range(0, len(answered_list)):
            client_dict = {
                "ip": answered_list[i][1].psrc,
                "mac": answered_list[i][1].hwsrc,
            }
            result.append(client_dict)

        return result

    def __find_hostnames(self, sweep_result):
        for item in sweep_result:
            # this could be better
            try:
                item["hostname"] = socket.gethostbyaddr(item["ip"])
            except:
                item["hostname"] = None
        return sweep_result
