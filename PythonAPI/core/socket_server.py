# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

# The Original Code is Copyright (C) 2020 Voxell Technologies.
# All rights reserved.

import socket

class Socket(object):

  def __init__(self, Agent, socketIP=socket.gethostname()):
    self.Agent = Agent

    self.listen_socket = socket.socket()
    self.socket_port = self.Agent.socket_port
    self.max_conn = self.Agent.socket_max_conn
    self.socketIP = socketIP

    self.listen_socket.bind((self.socketIP, self.socket_port))
    self.listen_socket.listen(self.max_conn)
    self.Agent._print(f"Server started at {self.socketIP} on port {self.socket_port}")
    self.client_socket, self.address = self.listen_socket.accept()
    self.Agent._print(f"New connection made!")

  def recv_msg(self):
    msg = self.client_socket.recv(1024).decode()
    self.Agent._print2(f"Recieved message: {msg}")
    return msg

  def send_msg(self, msg):
    self.Agent._print2(f"Sending message: {msg}")
    self.client_socket.send(msg.encode("ASCII"))

