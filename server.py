
import socket
import random
import numpy
from dec_tree import Dec_Tree
from scipy.interpolate import lagrange
from Processed_db import Processed_db
import pprint
from GUI import Decision_Tree_GUI

class Server:

    def __init__(self, num_of_parties):
        self.__num_of_parties = num_of_parties
        self.__deg = num_of_parties-1  #degree of the generated polynoms, set to be n-1, for n=number of parties participating in the protocol
        self.__summedXis=[] #X1,...,Xn.    Xi=(q1+...+qn)(xi)
        self.__rand_vals=[]
        self.__clientnum = 0
        self.__processed_db = Processed_db(-1)
        self.__table = self.__processed_db.get_all()

    def get_processed_db(self):
        return self.__processed_db

    def get_client_arr(self):
        return self.__client_arr

    def get_rand_vals(self):
        return self.__rand_vals

    def get_clientnum(self):
        return self.__clientnum

    def inc_clientnum(self):
        self.__clientnum = self.__clientnum+1

    def get_table(self):
        return self.__table

    def set_rand_vals(self):
        self.__rand_vals = random.sample(range(1,50), self.__num_of_parties)

    def get_num_of_parties(self):
        return self.__num_of_parties

    def get_deg(self):
        return self.__deg

    def get_summedXis(self):
        return self.__summedXis

    def set_summedXis(self, calculated_vals_of_poly):
        if self.__summedXis.__len__()==0:
            for i in calculated_vals_of_poly:
                self.__summedXis.append(i)
        else:
            for i in range (0, len(calculated_vals_of_poly)):
                self.__summedXis[i]=self.__summedXis[i]+calculated_vals_of_poly[i]

    def reset_summedXis(self):
        self.__summedXis = []

    # finds out what is Q(0), out of X1,...,Xn points, s.t Xi=(q1+...+qn(xi), and Q(Xi).
    def find_out_sum_value(self, Xs, fXs):
        return int(round(lagrange(Xs, fXs)(0)))


def convert_str_arr_to_int_arr (s):
    s1 = (str(s)).replace(' ', '')
    s2 = s1.replace('[', '')
    s3 = s2.replace(']', '')
    s4 = s3.replace(',', ' ')
    sl = s4.split(' ')
    si = [int(elem) for elem in sl]
    sa = numpy.array(si)
    return sa

HOST = 'localhost'
PORT = 8000
ADDRESS = (HOST,PORT)
BUFFER_SIZE = 2048
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(5)
server = Server(5)
print("Server created")
clients = []

for i in range(0,5):
    client, addr = s.accept()
    clients.append(client)
    client_index = server.get_clientnum()
    server.inc_clientnum()
    clients[i].send(str(client_index).encode())
    msg = clients[i].recv(BUFFER_SIZE).decode()

table = server.get_table()
for atts, att in table.items():
    for vals, val in att.items():
        for nums, num in val.items():

            server.set_rand_vals()

            for i in range(0, 5):

                clients[i].send(str(server.get_rand_vals()).encode())
                calculated_vals_str = clients[i].recv(BUFFER_SIZE).decode()
                calculated_vals = convert_str_arr_to_int_arr(calculated_vals_str)

                server.set_summedXis(calculated_vals)

            a = server.find_out_sum_value(server.get_rand_vals(),server.get_summedXis())  # NOTICE: i used rounding to natural number to get the right result in 'findOutSumValue' func
            table[atts][vals][nums] = a
            server.reset_summedXis()

s.close()

dec_tree = Dec_Tree(server)
pprint.pprint(dec_tree.get_tree_dict())

# my_gui = Dec_tree_gui(dec_tree)

app = Decision_Tree_GUI(dec_tree)
app.mainloop()
# my_gui.start_gui()



#*************image of the tree*********************************
# dec_tree = Dec_Tree(server)
# dtree = dec_tree.get_tree_dict()
# pprint.pprint(dtree)
#
# def draw(parent_name, child_name):
#     edge = pydot.Edge(parent_name, child_name)
#     graph.add_edge(edge)
#
# def visit(node, parent=None):
#     for k,v in node.items():
#         if isinstance(v, dict):
#             # We start with the root node whose parent is None
#             # we don't want to graph the None node
#             if parent:
#                 draw(parent, k)
#             visit(v, k)
#         else:
#             draw(parent, k)
#             # drawing the label using a distinct name
#             draw(k, k+'_'+v)
#
# graph = pydot.Dot(graph_type='graph')
# visit(dtree)
#
# graph.write_png('example1_graph.png')


#***********object of the user****************************************
# age = input("Insert your age")
# edu = input("Insert 1 if you have low education, 2 if average or 3 if high")
# kids = input("Insert how many children do you have or 0 if none")
# reg = input("Insert 1 if you consider yourself religious or 0 if not")
# obj_to_predict =[int(age), int(edu), 4, int(kids), int(reg), 1, 4, 4, 0, 3]
# pprint.pprint("The method you are most likely to use is ", dec_tree.predict(obj_to_predict, "", dec_tree.get_tree_dict(), 0))


#****************statistics*******************************************

# print(dec_tree.predict([24,2,3,3,1,1,2,3,0,1], "", dec_tree.get_tree_dict(), 0))
#
# database = open("test_db.txt", "r")
# lines = database.readlines()  # arranges each line of the txt file in a cell of a list
# right_guesses = 0
# wrong_guesses = 0
# guess = 0
#
# for l in lines:
#     sa = convert_str_arr_to_int_arr(l)
#     guess_name = dec_tree.predict2(sa, dec_tree.get_tree_dict(), 0)
#     if guess_name == "none":
#         guess = 1
#     elif guess_name == "long":
#         guess = 2
#     elif guess_name == "short":
#         guess = 3
#
#     if guess == sa[9]:
#         right_guesses = right_guesses + 1
#     else:
#         wrong_guesses = wrong_guesses + 1
#
# whole_guesses = right_guesses + wrong_guesses
# succ_precent = (float(right_guesses) / whole_guesses) * 100
# print("out of ", str(whole_guesses), "people tested, the tree was right in ", right_guesses)
# print("this is ", succ_precent, "% correctness")



# print(dec_tree.predict([24,2,3,3,1,1,2,3,0,1], "", dec_tree.get_tree_dict(), 0))

#************random object**********************************************