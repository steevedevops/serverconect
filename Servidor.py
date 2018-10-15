# Socket Server Basico pyprO
import socketserver  # importo el modulo del server



class MiTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.oracion = self.request.recv(1024).strip()  

        self.num = len(self.oracion)  

        print("La oracion recv e ", self.oracion, " el num de chars ", self.num)
        self.request.send(str(self.num))  


def main():

    host = "192.168.18.1"  
    port = 9999

    server1 = socketserver.TCPServer((host, port), MiTcpHandler)

    print("server correndo")
    server1.serve_forever()  


main()
