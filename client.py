import socket
import random
import numpy
from Processed_db import Processed_db


class Client:

    def __init__(self, client_index):
        self.__client_index = client_index
        self.__num_of_clients = 5
        self.__processed_db = Processed_db(client_index)
        self.__secret_vals_table = self.__processed_db.get_all()
        # self.__secret_val = self.get_next_secret_val()
        self.__polynom = []
        self.__client_index = client_index
        # self.__rand_val = client_rand_val

    # CONST LIST OF INT VALS, NO NEED TO MAKE 'SET' FUNC
    def get_polynom(self):
        return self.__polynom

    def get_deg(self):
        return self.__num_of_clients-1

    # CONST VALUE RECEIVED ON CONSTRUCT OF OBJECT, NO NEED TO MAKE 'SET' FUNC
    def get_rand_val(self):
        return self.__server.get_rand_vals()[self.__client_index]

    # CONST VALUE RECEIVED ON CONSTRUCT OF OBJECT, NO NEED TO MAKE 'SET' FUNC
    def get_client_index(self):
         return self.__client_index

    def get_num_of_clients(self):
        return self.__num_of_clients

    def get_table(self):
        return self.__secret_vals_table

    # Generates a random Poly of degree 'deg', deg=num-1 of parties, 'free organ'/const val of poly - the secret val of this party
    def generate_poly(self, secret_val, num_of_clients):
        # len = self.__server.get_numOfParties()
        len = num_of_clients
        coefficients=[]
        for i in range(0,len-1):
            coefficients.append(random.randint(-50,50))
        coefficients.append(secret_val)
        self.__polynom = coefficients
        return coefficients

    # calculates self polynom with the vals of all other clients, when x=val.
    def cal_val_in_poly(self, all_rand_vals):
        coefficients = self.get_polynom()
        rand_vals = all_rand_vals
        # print(str(all_rand_vals))
        # print ("tryyyy", str(convert_str_arr_to_int_arr (str_all_rand_vals)[0]))
        calculated_vals=[]
        for i in range (0, len(all_rand_vals)):
            val = all_rand_vals[i]
            if val == 0:
                print("Given value isn't valid")
                return
            else:
                res = 0
                deg = self.get_deg()
                for j in coefficients:
                    res = res + (j*(val**(deg)))
                    deg-=1
            calculated_vals.append(res)
        return calculated_vals

def convert_str_arr_to_int_arr (s):

    s1 = (str(s)).replace(' ', '')
    s2 = s1.replace('[','')
    s3 = s2.replace(']','')
    s4 = s3.replace(',',' ')
    sl = s4.split(' ')
    si = [int(elem) for elem in sl]
    sa = numpy.array(si)
    return sa


port = 8000
host = socket.gethostname()
BUFFER_SIZE = 2048

server = socket.socket()
server.connect((host, port))

client_index = int(server.recv(BUFFER_SIZE).decode())
server.send("got index".encode())
print("I am client ", str(client_index))
client = Client(client_index)
secret_vals_table = client.get_table()

#iterate over all the values in table

for atts, att in secret_vals_table.items():
    for vals, val in att.items():
        for nums, num in val.items():

            secret_val = num
            all_rand_vals_str = server.recv(BUFFER_SIZE).decode()
            all_rand_vals = convert_str_arr_to_int_arr(all_rand_vals_str)
            client_rand_val = all_rand_vals[client_index]

            client.generate_poly(secret_val, client.get_num_of_clients())

            # print("the coeffs of poly: ", client.get_polynom())

            calculated_values_in_poly_arr = client.cal_val_in_poly(all_rand_vals)
            # print("THE CALCULATED VALUES IN POLY ARR:", calculated_values_in_poly_arr)
            server.send(str(calculated_values_in_poly_arr).encode())

server.close()



