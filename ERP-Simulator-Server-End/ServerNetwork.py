# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/20
# author : Zhiquan.Wang

import socket
import threading


class ServerSocket(object):
    def __init__(self, _ip, _p):
        self.__host_ip = _ip
        self.__port = _p
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.__host_ip, self.__port))
        self.__max_connect_num = 512

    def launch_server(self):
        self.__socket.listen(self.__max_connect_num)
        while True:
            client_socket_info = self.__socket.accept()
            address_thread = threading.Thread(target=self.__address_request, args= client_socket_info)
            address_thread.start()

    def __address_request(self, _c_socket_info):
        tmp_socket = _c_socket_info[0]
        while True:
            data = tmp_socket.recv(1024)
            if not data:
                break
            print("Receive : " + data.decode('utf-8'))
            tmp_socket.send(('received ' + data.decode('utf-8')).encode('utf-8'))
        tmp_socket.close()
