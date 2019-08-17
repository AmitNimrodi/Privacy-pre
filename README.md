# Privacy-preserving-data-mining-methods-project
Implementation of Shamir's secret sharing algorithm, and ID3 algorithm.


This project is based on this article: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.156.6683&rep=rep1&type=pdf
and this databse (also referred as 'DB'): ftp://ftp.ics.uci.edu/pub/machine-learning-databases/cmc


Program flow:
'Server' is in charge of managing the secret sharing protocol.
Each client (of a total 5) holds his own database file, parses it and counts how many appearances are there of each value.
The clients and the server operate together to unite the distributed DB's while protecting each client's DB private.
Now, based on the united DB, the decision tree can be trained properly.
The DB holds 1473 objects. They were split into 6 different sized DBs and distributed between the 5 clients to process.
The 6th part was kept to test the trained decision tree.

How to run the program:
1. Run server
2. run client (repeat 5 times)
3. mess around with the GUI and printed results.

