from tkinter import *
from tkinter.ttk import *
import numpy
from PIL import Image, ImageTk
import pydot
import io

LARGE_FONT = ("Verdana", 10)


class Decision_Tree_GUI(Tk):

    def __init__(self, dec_tree , *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        self.dec_tree = dec_tree
        #self.maxsize(width=1920, height=1080)
        self.resizable(width=True, height=True)
        self.title('Preserving decision tree learning over multiple parties')
        container.pack(fill=X, expand=True)
        # container.pack_propagate(0)

        container.grid_rowconfigure(0, weight=0)
        container.grid_columnconfigure(0, weight=0)

        self.frames = {}

        for F in (StartPage, Page_statistics, Page_user_prediction, Page_tree_image):

            frame = F(container, self, self.dec_tree)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller, dec_tree):
        Frame.__init__(self, parent)
        self. controller = controller
        self.dec_tree= dec_tree
        # maxsize(width=500, height=300)

        self.page()

    def page(self):
        combo = Combobox(self, values=("your prediction", "statistics", "show tree"))
        combo.current(0)  # set the selected item
        combo.pack(pady=10, padx=10)

        button = Button(self, text="predict", command=lambda: self.controller.show_frame(self.check_combo(combo)))
        button.pack()

    def check_combo(self, cmb):

        if cmb.get() == "statistics":
            return Page_statistics

        elif cmb.get() == "your prediction":
            return Page_user_prediction

        elif cmb.get() == "show tree":
            return Page_tree_image

        else:
            return StartPage



class Page_statistics(Frame):

    def __init__(self, parent, controller, dec_tree):
        Frame.__init__(self, parent)
        self.dec_tree = dec_tree

        database = open("test_db.txt", "r")
        lines = database.readlines()  # arranges each line of the txt file in a cell of a list
        right_guesses = 0
        wrong_guesses = 0
        guess = 0

        for l in lines:
            sa = convert_str_arr_to_int_arr(l)
            guess_name, precent = dec_tree.predict(sa, "", self.dec_tree.get_tree_dict(), 0)
            if guess_name == "none":
                guess = 1
            elif guess_name == "long":
                guess = 2
            elif guess_name == "short":
                guess = 3

            if guess == sa[9]:
                right_guesses = right_guesses + 1
            else:
                wrong_guesses = wrong_guesses + 1

        whole_guesses = right_guesses + wrong_guesses
        succ_precent = (float(right_guesses) / whole_guesses) * 100
        label = Label(self, text= "out of "+ str(whole_guesses)+ " people tested,\n the tree was right in " + str(right_guesses) + "\nthis is "+ str(succ_precent) + "% correctness", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = Button(self, text="back",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class Page_user_prediction(Frame):

    def __init__(self, parent, controller, dec_tree):
        Frame.__init__(self, parent)
        self.dec_tree = dec_tree

        lbl = Label(self, text="Age:")
        lbl.grid(row=0, column=0, sticky=W)

        age = Entry(self)
        age.focus()
        age.grid(row=0, column=1, sticky=W)

        lbl2 = Label(self, text="Education:")
        lbl2.grid(row=1, column=0,sticky=W)

        eselected = IntVar()
        eselected.set(0)


        erad1 = Radiobutton(self, text='Low', value=1, variable=eselected)

        erad2 = Radiobutton(self, text='Average', value=2, variable=eselected)

        erad3 = Radiobutton(self, text='High', value=3, variable=eselected)

        erad1.grid(row=1, column=1, sticky=W)

        erad2.grid(row=1, column=2, sticky=W)

        erad3.grid(row=1, column=3, sticky=W)

        lbl3 = Label(self, text="Children:")
        lbl3.grid(column=0, row=2, sticky=W)

        var = IntVar()
        # var.set(0)

        spin = Spinbox(self, from_=0, to=20, width=5, textvariable=var)
        spin.grid(column=1, row=2, sticky=W)

        lbl4 = Label(self, text="Religious:")
        lbl4.grid(column=0, row=3, sticky=W)

        rselected = IntVar()
        # rselected.set(0)

        rrad1 = Radiobutton(self, text='Not religious', value=0, variable=rselected)

        rrad2 = Radiobutton(self, text='religious', value=1, variable=rselected)

        rrad1.grid(column=1, row=3, sticky=W)

        rrad2.grid(column=2, row=3, sticky=W)




        def clear_values():
            age.delete(0, END)
            spin.delete(0, END)
        def back():
            clear_values()
            text.set(' ')
            controller.show_frame(StartPage)

        btn = Button(self, text="Predict", command=lambda: clicked())

        btn.grid(column=1, row=5)

        button1 = Button(self, text="back",
                         command=lambda: back())
        button1.grid(column=2, row=5)

        button2 = Button(self, text="clear",
                         command=lambda: clear_values())
        button2.grid(column=3, row=5)

        text = StringVar()
        text.set(' ')
        lbl5 = Label(self, textvariable=text)
        lbl5.grid(row=6, column=0, columnspan=5)

        def clicked():
            obj_to_predict = [int(age.get()), int(eselected.get()), 4, int(spin.get()), int(rselected.get()), 1, 4, 4,
                              0, 3]
            res, precent = self.dec_tree.predict(obj_to_predict, "", self.dec_tree.get_tree_dict(), 0)

            text.set("The method you are most likely to use is " + res + ", and the " + precent)

            # controller.show_frame(Page_res_prediction)


class Page_tree_image(Frame):

    def __init__(self, parent, controller, dec_tree):
        Frame.__init__(self, parent)
        self.dec_tree = dec_tree
        self.show_image()
        self.controller=controller


    def show_image(self):
        dtree = self.dec_tree.get_tree_dict()

        def draw(parent_name, child_name):
            edge = pydot.Edge(parent_name, child_name)
            graph.add_edge(edge)

        def visit(node, parent=None):
            for k, v in node.items():
                if isinstance(v, dict):
                    # We start with the root node whose parent is None
                    # we don't want to graph the None node
                    if parent:
                        draw(parent, k)
                    visit(v, k)
                else:
                    draw(parent, k)
                    # drawing the label using a distinct name
                    draw(k, k + '_' + v)

        graph = pydot.Dot(graph_type='graph')
        visit(dtree)

        graph.write_png('example1_graph.png')
        load = Image.open("example1_graph.png")
        size = 1050,620
        load.thumbnail(size)
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.grid()

        button1 = Button(self, text="back",
                         command=lambda: self.controller.show_frame(StartPage))
        button1.grid(column = 2, row=0)


def convert_str_arr_to_int_arr (s):
    s1 = (str(s)).replace(' ', '')
    s2 = s1.replace('[', '')
    s3 = s2.replace(']', '')
    s4 = s3.replace(',', ' ')
    sl = s4.split(' ')
    si = [int(elem) for elem in sl]
    sa = numpy.array(si)
    return sa
#
# app = SeaofBTCapp()
# app.mainloop()