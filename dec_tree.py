import random
import math


class Dec_Tree:

    def __init__(self,server):
        self.__processed_db = server.get_processed_db()
        atts = list(self.__processed_db.get_attribute().keys())
        atts.remove("method")
        self.__root = Node(self ,None,0, [], [], atts) #tree, father, depth, atts, vals, left_atts
        self.__tree_dict=self.build_tree(0, self.__root)

    def get_tree_dict(self):
        return self.__tree_dict

    def get_processed_db(self):
        return self.__processed_db

    def build_tree(self, depth, node):
        dominant=node.get_dominant()
        tree={}
        tree[dominant]={}
        atts=node.get_atts()[:]
        atts.append(dominant)
        val = node.get_vals()[:]
        leftAtts = node.get_left_atts()[:]
        leftAtts.remove(dominant)
        values_of_dominant = self.__processed_db.get_attribute()[dominant].keys() ##example: if dominant=age, vals=[U30, 30-40, 40+]
        for x in values_of_dominant:
            val_node=Node(self, node, depth+1, atts, val+[x], leftAtts)
            if val_node.get_is_leaf()>0:  ## if >0, means its a leaf
                dominantval = val_node.get_dominant()

                tree[dominant][x]=dominantval
            else:
                tree[dominant][x]=self.build_tree(depth+1, val_node)
        return tree

    def turn_inst_into_dict(self, inst):
        instance={}
        string=""
        if inst[0]<30:
            instance["age"]="U30"
            string=string+"U30"
        elif inst[0]<40:
            instance["age"]="30-40"
            string=string+"30-40"
        else:
            instance["age"]="40+"
            string=string+"40+"
        if inst[1]<2:
            instance["education"]="low"
            string=string+"_low"
        elif inst[1]<4:
            instance["education"]="avg"
            string=string+"_avg"
        else:
            instance["education"]="high"
            string=string+"_avg"
        if inst[3]<5:
            instance["kids"]="U5"
            string=string+"_U5"
        elif inst[3]<10:
            instance["kids"]="5-9"
            string=string+"_5-9"
        else:
            instance["kids"]="10+"
            string=string+"_10+"
        if inst[4]==0:
            instance["religious"]="not-rel"
            string=string+"_not-rel"
        else:
            instance["religious"]="rel"
            string=string+"_rel"
        return instance, string


    def predict(self, inst, string, tree, parsed): ##assuming inst looks like : [24,2,3,3,1,1,2,3,0,1]. parsed parameter is a flag
        x=0
        if parsed==0:
            inst, string = self.turn_inst_into_dict(inst)
        for nodes in tree.keys():
            value=inst[nodes]
            tree=tree[nodes][value]
            if type(tree) is dict:
                prediction=self.predict(inst, string, tree, 1)
            else:
                prediction=tree
                str2=string+"_"+prediction
                y=self.get_processed_db().get_pentas()["age & education & kids & religious & method"][str2]
                t=self.get_processed_db().get_quads()["age & education & kids & religious"][string]
                x=y*100/t
                x="{0:.2f}".format(x)
                toprint="Certaincy of prediction: "+x+" %"
                return prediction,toprint
        return prediction


class Node:

    def __init__(self, tree, father, depth, atts, vals, leftAtts):
        self.__tree = tree      ##only use it so node can reach tree's db. alternative: make db field for node
        self.__processed_db = self.__tree.get_processed_db()
        self.__father = father   ##father node - NOT USED BY NOW, DELETE MAYBE?
        self.__depth = depth  ##relevant depths : 1 to 4. 0 is root(general db), and 5 is category values.
        self.__atts = atts #example : for node u30_low, att will be ["age", "education"] - depth is 2
        self.__vals = vals #example: for node u30_low, vals will be ["U30", "low"]
        self.__stringed_atts = self.atts_string(atts)  #example: input:["age, "education"] ->output: "age & education"
        self.__stringed_vals = self.vals_string(vals)  ##example: input:["U30", "low"] will become output: "U30_low"
        self.__tuple = self.get_tuple(self.__stringed_atts)
        self.__left_atts=leftAtts  ##example: for node u30_low the left Atts are ["kids" , "religious"]
        self.__is_leaf= -1  ##default value, will turn into 1 if dominant is category value (in calculate_gain func)
        if len(self.__atts)==0: ## in case this is root - we want amount of all obj
            sum=0
            for y in self.__tuple["age"].values(): ## count all values of age is enough - every obj has an age value.
                    sum=sum+y
            self.__amount_of_objects=sum
        else:
            self.__amount_of_objects = self.__tuple.get(self.__stringed_atts).get(self.__stringed_vals) #num of objects in this node's subtree
        if self.__amount_of_objects == 0:
            self.__is_leaf=1
            list=["none","long","short"]
            self.__dominant=random.choice(list)  ##just guess anything, there aren't any objects on the path of this object
        else:
            self.__dominant=self.calculate_gain() ##finds the dominant att of the left_atts, or category val.

    def get_depth(self):
        return self.__depth

    def get_tuple(self, att_str):
        x=att_str.count("&")
        if x==0:
            return self.__processed_db.get_attribute()
        if x==1:
            return self.__processed_db.get_couples()
        if x==2:
            return self.__processed_db.get_trios()
        if x==3:
            return self.__processed_db.get_quads()
        if x==4:
            return self.__processed_db.get_pentas()

    def get_left_atts(self):
        return self.__left_atts

    def get_dominant(self):
        return self.__dominant

    def get_is_leaf(self):
        return self.__is_leaf

    def get_atts(self):
        return self.__atts

    def get_vals(self):
        return self.__vals

    def vals_string(self, vals):
        if len(vals)==0:
            return ""
        else:
            new_vals=[]
            if "U30" in vals:
                new_vals.append("U30")
            elif "30-40" in vals:
                new_vals.append("30-40")
            elif "40+" in vals:
                new_vals.append("40+")
            if "low" in vals:
                new_vals.append("low")
            elif "avg" in vals:
                new_vals.append("avg")
            elif "high" in vals:
                new_vals.append("high")
            if "U5" in vals:
                new_vals.append("U5")
            elif "5-9" in vals:
                new_vals.append("5-9")
            elif "10+" in vals:
                new_vals.append("10+")
            if "not-rel" in vals:
                new_vals.append("not-rel")
            elif "rel" in vals:
                new_vals.append("rel")
            if "none" in vals:
                new_vals.append("none")
            elif "long" in vals:
                new_vals.append("long")
            elif "short" in vals:
                new_vals.append("short")
            string=new_vals[0]
            for x in new_vals:
                if string!=x:
                    string=string+"_"+x
            return string

    def atts_string(self, atts):
        if len(atts)==0:
            return ""
        else:
            new_atts=[]
            if "age" in atts:
                new_atts.append("age")
            if "education" in atts:
                new_atts.append("education")
            if "kids" in atts:
                new_atts.append("kids")
            if "religious" in atts:
                new_atts.append("religious")
            string=new_atts[0]
            for x in new_atts:
                if string!=x:
                    string=string+" & "+x
            return string

    def calculate_ET(self,t, val_str, att_str):
        sum=0
        if val_str=="" and att_str=="":
            updated_str_att="method"
            updated_val_short="short"
            updated_val_long="long"
            updated_val_none="none"
        else:
            updated_str_att=att_str+" & method"
            updated_val_none = val_str+"_none"
            updated_val_long= val_str+"_long"
            updated_val_short= val_str+"_short"
        tuple = self.get_tuple(updated_str_att)
        for x,y in tuple.get(updated_str_att).items():
            if x in(updated_val_none,updated_val_long,updated_val_short) and t!=0:
                fraction = y/t
                if fraction==1: ##this checks if all U30_low (t) for example, are also U30_low_none (y) (share same cat val)
                    if x.find("none")>-1:
                        return 0, "none"
                    if x.find("long")>-1:
                        return 0, "long"
                    if x.find("short")>-1:
                        return 0, "short"
                elif fraction == 0:
                    sum += 0
                else:
                    sum += (-fraction*math.log2(fraction))
        return sum

    def calculate_gain(self):
        etas={}
        str=""
        if self.__depth==4: ##this means we went throguh all the attributes, need to find most popular category for left objects
            updated_val_none=self.__stringed_vals+"_none"
            updated_val_long=self.__stringed_vals+"_long"
            updated_val_short=self.__stringed_vals+"_short"
            updated_atts_str=self.__stringed_atts+" & method"
            tuples=self.get_tuple(updated_atts_str)
            max=-math.inf
            self.__is_leaf=1
            for x in tuples.values(): ##example of value: ("U30_low_U5_not-rel_none": SOME NUMBER)
                for y,z in x.items():
                    if y in(updated_val_short,updated_val_long,updated_val_none):
                        if (z==self.__amount_of_objects):  ##ex: U30_low_U5_not-rel == U30_low_U5_not-rel_none
                            w=y.replace(self.__stringed_vals+"_",'')
                            str=w
                            break
                        if z>max:
                            max=z
                            w=y.replace(self.__stringed_vals+"_", '')
                            str=w
        else:
            et = self.calculate_ET(self.__amount_of_objects,self.__stringed_vals,self.__stringed_atts)
            if type(et)==tuple: #this means that all the left objects share same category
                self.__is_leaf=1
                return et[1]   ##et[1] is the category val that all objects share now.
            else:
                min=math.inf
                for x in self.__left_atts: ## x is att, ex: "kids"
                    etas[x] = self.calculate_ETA(x)     ##this loop calculates all the eta values and adds keys to each
                for x,y in etas.items(): ##
                    if y<min:
                        min=y
                        str=x
        return str ##returned value is the dominant left att


    def calculate_ETA(self, att):
        sum=0
        t=self.__amount_of_objects
        updated_atts = self.get_atts()[:]
        updated_atts.append(att)
        updated_atts_str=self.atts_string(updated_atts)  ##example: "age & education & kids" if given att was "kids" and we're in node "u30_low"
        tuples=self.get_tuple(updated_atts_str)
        for x,y in tuples.get(updated_atts_str).items(): ##example: if updated_str_att is as above, then x can be U30_low_U5
            if x.find(self.__stringed_vals)>-1 and y!=0:
                updated_str_values = self.vals_string(x)
                tai=self.calculate_ET(y, updated_str_values, updated_atts_str)
                if type(tai)==tuple:
                    tai=tai[0]
                sum+=(y*tai/t)
        return sum