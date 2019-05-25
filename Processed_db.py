
import math
import numpy
import pprint

#COUNTERS FOR EVERY ATTRIBUTE'S POSSIBLE VALUE (counter for every ai)

#hagar

class Processed_db:

    def __init__(self, client_index):
        self.__attributes = self.build_att_dict()
        self.__couples = self.build_couples()
        self.__trios = self.build_trios()
        self.__quads = self.build_quads()
        self.__pentas = self.build_pentas()

        if (client_index != -1):
            self.__db_name = "db" + str(client_index + 1) + ".txt"
            self.countValues(self.__db_name)


    def get_attribute(self):
        return self.__attributes

    def get_couples(self):
        return self.__couples

    def get_trios(self):
        return self.__trios

    def get_quads(self):
        return self.__quads

    def get_pentas(self):
        return self.__pentas

    def get_all(self):
        return {"attribute": self.get_attribute(),
                "couples": self.get_couples(),
                "trios": self.get_trios(),
                "quads": self.get_quads(),
                "pentas": self.get_pentas()}

    def build_att_dict(self):
        return {"age": {"U30": 0, "30-40": 0, "40+": 0},
                "education": {"low": 0, "avg": 0, "high": 0},
                "kids": {"U5": 0, "5-9": 0, "10+": 0},
                "religious": {"not-rel": 0, "rel": 0},
                "method": {"none": 0, "long": 0, "short": 0}}

    def build_couples(self):
        return {"age & education": {"U30_low": 0, "U30_avg": 0, "U30_high": 0,
                                    "30-40_low": 0, "30-40_avg": 0, "30-40_high": 0,
                                    "40+_low": 0, "40+_avg": 0, "40+_high": 0
                                    },
                "age & kids": {"U30_U5": 0, "U30_5-9": 0, "U30_10+": 0,
                               "30-40_U5": 0, "30-40_5-9": 0, "30-40_10+": 0,
                               "40+_U5": 0, "40+_5-9": 0, "40+_10+": 0
                               },
                "age & religious": {"U30_not-rel": 0, "U30_rel": 0,
                                    "30-40_not-rel": 0, "30-40_rel": 0,
                                    "40+_not-rel": 0, "40+_rel": 0
                                    },
                "age & method": {"U30_none": 0, "U30_long": 0, "U30_short": 0,
                                 "30-40_none": 0, "30-40_long": 0, "30-40_short": 0,
                                 "40+_none": 0, "40+_long": 0, "40+_short": 0
                                 },
                "education & kids": {"low_U5": 0, "low_5-9": 0, "low_10+": 0,
                                     "avg_U5": 0, "avg_5-9": 0, "avg_10+": 0,
                                     "high_U5": 0, "high_5-9": 0, "high_10+": 0
                                     },
                "education & religious": {"low_not-rel": 0, "low_rel": 0,
                                          "avg_not-rel": 0, "avg_rel": 0,
                                          "high_not-rel": 0, "high_rel": 0
                                          },
                "education & method": {"low_none": 0, "low_long": 0, "low_short": 0,
                                       "avg_none": 0, "avg_long": 0, "avg_short": 0,
                                       "high_none": 0, "high_long": 0, "high_short": 0
                                       },
                "kids & religious": {"U5_not-rel": 0, "U5_rel": 0,
                                     "5-9_not-rel": 0, "5-9_rel": 0,
                                     "10+_not-rel": 0, "10+_rel": 0
                                     },
                "kids & method": {"U5_none": 0, "U5_long": 0, "U5_short": 0,
                                  "5-9_none": 0, "5-9_long": 0, "5-9_short": 0,
                                  "10+_none": 0, "10+_long": 0, "10+_short": 0
                                  },
                "religious & method": {"not-rel_none": 0, "not-rel_long": 0, "not-rel_short": 0,
                                       "rel_none": 0, "rel_long": 0, "rel_short": 0}
                }

    def build_trios(self):
        return {"age & education & kids": {"U30_low_U5": 0, "U30_avg_U5": 0, "U30_high_U5": 0,
                                           "U30_low_5-9": 0, "U30_avg_5-9": 0, "U30_high_5-9": 0,
                                           "U30_low_10+": 0, "U30_avg_10+": 0, "U30_high_10+": 0,
                                           "30-40_low_U5": 0, "30-40_avg_U5": 0, "30-40_high_U5": 0,
                                           "30-40_low_5-9": 0, "30-40_avg_5-9": 0, "30-40_high_5-9": 0,
                                           "30-40_low_10+": 0, "30-40_avg_10+": 0, "30-40_high_10+": 0,
                                           "40+_low_U5": 0, "40+_avg_U5": 0, "40+_high_U5": 0,
                                           "40+_low_5-9": 0, "40+_avg_5-9": 0, "40+_high_5-9": 0,
                                           "40+_low_10+": 0, "40+_avg_10+": 0, "40+_high_10+": 0
                                           },
                "age & education & religious": {"U30_low_not-rel": 0, "U30_low_rel": 0,
                                                "U30_avg_not-rel": 0, "U30_avg_rel": 0,
                                                "U30_high_not-rel": 0, "U30_high_rel": 0,
                                                "30-40_low_not-rel": 0, "30-40_low_rel": 0,
                                                "30-40_avg_not-rel": 0, "30-40_avg_rel": 0,
                                                "30-40_high_not-rel": 0, "30-40_high_rel": 0,
                                                "40+_low_not-rel": 0, "40+_low_rel": 0,
                                                "40+_avg_not-rel": 0, "40+_avg_rel": 0,
                                                "40+_high_not-rel": 0, "40+_high_rel": 0
                                                },
                "age & education & method": {"U30_low_none": 0, "U30_avg_none": 0, "U30_high_none": 0,
                                             "U30_low_long": 0, "U30_avg_long": 0, "U30_high_long": 0,
                                             "U30_low_short": 0, "U30_avg_short": 0, "U30_high_short": 0,
                                             "30-40_low_none": 0, "30-40_avg_none": 0, "30-40_high_none": 0,
                                             "30-40_low_long": 0, "30-40_avg_long": 0, "30-40_high_long": 0,
                                             "30-40_low_short": 0, "30-40_avg_short": 0, "30-40_high_short": 0,
                                             "40+_low_none": 0, "40+_avg_none": 0, "40+_high_none": 0,
                                             "40+_low_long": 0, "40+_avg_long": 0, "40+_high_long": 0,
                                             "40+_low_short": 0, "40+_avg_short": 0, "40+_high_short": 0
                                             },
                "age & kids & religious": {"U30_U5_not-rel": 0, "U30_U5_rel": 0,
                                           "U30_5-9_not-rel": 0, "U30_5-9_rel": 0,
                                           "U30_10+_not-rel": 0, "U30_10+_rel": 0,
                                           "30-40_U5_not-rel": 0, "30-40_U5_rel": 0,
                                           "30-40_5-9_not-rel": 0, "30-40_5-9_rel": 0,
                                           "30-40_10+_not-rel": 0, "30-40_10+_rel": 0,
                                           "40+_U5_not-rel": 0, "40+_U5_rel": 0,
                                           "40+_5-9_not-rel": 0, "40+_5-9_rel": 0,
                                           "40+_10+_not-rel": 0, "40+_10+_rel": 0
                                           },
                "age & kids & method": {"U30_U5_none": 0, "U30_U5_long": 0, "U30_U5_short": 0,
                                        "U30_5-9_none": 0, "U30_5-9_long": 0, "U30_5-9_short": 0,
                                        "U30_10+_none": 0, "U30_10+_long": 0, "U30_10+_short": 0,
                                        "30-40_U5_none": 0, "30-40_U5_long": 0, "30-40_U5_short": 0,
                                        "30-40_5-9_none": 0, "30-40_5-9_long": 0, "30-40_5-9_short": 0,
                                        "30-40_10+_none": 0, "30-40_10+_long": 0, "30-40_10+_short": 0,
                                        "40+_U5_none": 0, "40+_U5_long": 0, "40+_U5_short": 0,
                                        "40+_5-9_none": 0, "40+_5-9_long": 0, "40+_5-9_short": 0,
                                        "40+_10+_none": 0, "40+_10+_long": 0, "40+_10+_short": 0
                                        },
                "age & religious & method": {"U30_not-rel_none": 0, "U30_not-rel_long": 0, "U30_not-rel_short": 0,
                                             "U30_rel_none": 0, "U30_rel_long": 0, "U30_rel_short": 0,
                                             "30-40_not-rel_none": 0, "30-40_not-rel_long": 0, "30-40_not-rel_short": 0,
                                             "30-40_rel_none": 0, "30-40_rel_long": 0, "30-40_rel_short": 0,
                                             "40+_not-rel_none": 0, "40+_not-rel_long": 0, "40+_not-rel_short": 0,
                                             "40+_rel_none": 0, "40+_rel_long": 0, "40+_rel_short": 0,
                                             },

                "education & kids & religious": {"low_U5_not-rel": 0, "low_U5_rel": 0,
                                                 "low_5-9_not-rel": 0, "low_5-9_rel": 0,
                                                 "low_10+_not-rel": 0, "low_10+_rel": 0,
                                                 "avg_U5_not-rel": 0, "avg_U5_rel": 0,
                                                 "avg_5-9_not-rel": 0, "avg_5-9_rel": 0,
                                                 "avg_10+_not-rel": 0, "avg_10+_rel": 0,
                                                 "high_U5_not-rel": 0, "high_U5_rel": 0,
                                                 "high_5-9_not-rel": 0, "high_5-9_rel": 0,
                                                 "high_10+_not-rel": 0, "high_10+_rel": 0
                                                 },
                "education & kids & method": {"low_U5_none": 0, "low_U5_long": 0, "low_U5_short": 0,
                                              "low_5-9_none": 0, "low_5-9_long": 0, "low_5-9_short": 0,
                                              "low_10+_none": 0, "low_10+_long": 0, "low_10+_short": 0,
                                              "avg_U5_none": 0, "avg_U5_long": 0, "avg_U5_short": 0,
                                              "avg_5-9_none": 0, "avg_5-9_long": 0, "avg_5-9_short": 0,
                                              "avg_10+_none": 0, "avg_10+_long": 0, "avg_10+_short": 0,
                                              "high_U5_none": 0, "high_U5_long": 0, "high_U5_short": 0,
                                              "high_5-9_none": 0, "high_5-9_long": 0, "high_5-9_short": 0,
                                              "high_10+_none": 0, "high_10+_long": 0, "high_10+_short": 0
                                              },
                "education & religious & method": {"low_not-rel_none": 0, "low_not-rel_long": 0, "low_not-rel_short": 0,
                                                   "low_rel_none": 0, "low_rel_long": 0, "low_rel_short": 0,
                                                   "avg_not-rel_none": 0, "avg_not-rel_long": 0, "avg_not-rel_short": 0,
                                                   "avg_rel_none": 0, "avg_rel_long": 0, "avg_rel_short": 0,
                                                   "high_not-rel_none": 0, "high_not-rel_long": 0,
                                                   "high_not-rel_short": 0,
                                                   "high_rel_none": 0, "high_rel_long": 0, "high_rel_short": 0,
                                                   },
                "kids & religious & method": {"U5_not-rel_none": 0, "U5_not-rel_long": 0, "U5_not-rel_short": 0,
                                              "U5_rel_none": 0, "U5_rel_long": 0, "U5_rel_short": 0,
                                              "5-9_not-rel_none": 0, "5-9_not-rel_long": 0, "5-9_not-rel_short": 0,
                                              "5-9_rel_none": 0, "5-9_rel_long": 0, "5-9_rel_short": 0,
                                              "10+_not-rel_none": 0, "10+_not-rel_long": 0, "10+_not-rel_short": 0,
                                              "10+_rel_none": 0, "10+_rel_long": 0, "10+_rel_short": 0,
                                              },
                }

    def build_quads(self):
        return {
            "age & education & kids & religious": {"U30_low_U5_not-rel": 0, "U30_avg_U5_not-rel": 0,
                                                   "U30_high_U5_not-rel": 0,
                                                   "U30_low_U5_rel": 0, "U30_avg_U5_rel": 0, "U30_high_U5_rel": 0,
                                                   "U30_low_5-9_not-rel": 0, "U30_avg_5-9_not-rel": 0,
                                                   "U30_high_5-9_not-rel": 0,
                                                   "U30_low_5-9_rel": 0, "U30_avg_5-9_rel": 0, "U30_high_5-9_rel": 0,
                                                   "U30_low_10+_not-rel": 0, "U30_avg_10+_not-rel": 0,
                                                   "U30_high_10+_not-rel": 0,
                                                   "U30_low_10+_rel": 0, "U30_avg_10+_rel": 0, "U30_high_10+_rel": 0,
                                                   "30-40_low_U5_not-rel": 0, "30-40_avg_U5_not-rel": 0,
                                                   "30-40_high_U5_not-rel": 0,
                                                   "30-40_low_U5_rel": 0, "30-40_avg_U5_rel": 0, "30-40_high_U5_rel": 0,
                                                   "30-40_low_5-9_not-rel": 0, "30-40_avg_5-9_not-rel": 0,
                                                   "30-40_high_5-9_not-rel": 0,
                                                   "30-40_low_5-9_rel": 0, "30-40_avg_5-9_rel": 0,
                                                   "30-40_high_5-9_rel": 0,
                                                   "30-40_low_10+_not-rel": 0, "30-40_avg_10+_not-rel": 0,
                                                   "30-40_high_10+_not-rel": 0,
                                                   "30-40_low_10+_rel": 0, "30-40_avg_10+_rel": 0,
                                                   "30-40_high_10+_rel": 0,
                                                   "40+_low_U5_not-rel": 0, "40+_avg_U5_not-rel": 0,
                                                   "40+_high_U5_not-rel": 0,
                                                   "40+_low_U5_rel": 0, "40+_avg_U5_rel": 0, "40+_high_U5_rel": 0,
                                                   "40+_low_5-9_not-rel": 0, "40+_avg_5-9_not-rel": 0,
                                                   "40+_high_5-9_not-rel": 0,
                                                   "40+_low_5-9_rel": 0, "40+_avg_5-9_rel": 0, "40+_high_5-9_rel": 0,
                                                   "40+_low_10+_not-rel": 0, "40+_avg_10+_not-rel": 0,
                                                   "40+_high_10+_not-rel": 0,
                                                   "40+_low_10+_rel": 0, "40+_avg_10+_rel": 0, "40+_high_10+_rel": 0
                                                   },
            "age & education & kids & method": {"U30_low_U5_none": 0, "U30_avg_U5_none": 0, "U30_high_U5_none": 0,
                                                "U30_low_U5_long": 0, "U30_avg_U5_long": 0, "U30_high_U5_long": 0,
                                                "U30_low_U5_short": 0, "U30_avg_U5_short": 0, "U30_high_U5_short": 0,
                                                "U30_low_5-9_none": 0, "U30_avg_5-9_none": 0, "U30_high_5-9_none": 0,
                                                "U30_low_5-9_long": 0, "U30_avg_5-9_long": 0, "U30_high_5-9_long": 0,
                                                "U30_low_5-9_short": 0, "U30_avg_5-9_short": 0, "U30_high_5-9_short": 0,
                                                "U30_low_10+_none": 0, "U30_avg_10+_none": 0, "U30_high_10+_none": 0,
                                                "U30_low_10+_long": 0, "U30_avg_10+_long": 0, "U30_high_10+_long": 0,
                                                "U30_low_10+_short": 0, "U30_avg_10+_short": 0, "U30_high_10+_short": 0,
                                                "30-40_low_U5_none": 0, "30-40_avg_U5_none": 0, "30-40_high_U5_none": 0,
                                                "30-40_low_U5_long": 0, "30-40_avg_U5_long": 0, "30-40_high_U5_long": 0,
                                                "30-40_low_U5_short": 0, "30-40_avg_U5_short": 0,
                                                "30-40_high_U5_short": 0,
                                                "30-40_low_5-9_none": 0, "30-40_avg_5-9_none": 0,
                                                "30-40_high_5-9_none": 0,
                                                "30-40_low_5-9_long": 0, "30-40_avg_5-9_long": 0,
                                                "30-40_high_5-9_long": 0,
                                                "30-40_low_5-9_short": 0, "30-40_avg_5-9_short": 0,
                                                "30-40_high_5-9_short": 0,
                                                "30-40_low_10+_none": 0, "30-40_avg_10+_none": 0,
                                                "30-40_high_10+_none": 0,
                                                "30-40_low_10+_long": 0, "30-40_avg_10+_long": 0,
                                                "30-40_high_10+_long": 0,
                                                "30-40_low_10+_short": 0, "30-40_avg_10+_short": 0,
                                                "30-40_high_10+_short": 0,
                                                "40+_low_U5_none": 0, "40+_avg_U5_none": 0, "40+_high_U5_none": 0,
                                                "40+_low_U5_long": 0, "40+_avg_U5_long": 0, "40+_high_U5_long": 0,
                                                "40+_low_U5_short": 0, "40+_avg_U5_short": 0, "40+_high_U5_short": 0,
                                                "40+_low_5-9_none": 0, "40+_avg_5-9_none": 0, "40+_high_5-9_none": 0,
                                                "40+_low_5-9_long": 0, "40+_avg_5-9_long": 0, "40+_high_5-9_long": 0,
                                                "40+_low_5-9_short": 0, "40+_avg_5-9_short": 0, "40+_high_5-9_short": 0,
                                                "40+_low_10+_none": 0, "40+_avg_10+_none": 0, "40+_high_10+_none": 0,
                                                "40+_low_10+_long": 0, "40+_avg_10+_long": 0, "40+_high_10+_long": 0,
                                                "40+_low_10+_short": 0, "40+_avg_10+_short": 0, "40+_high_10+_short": 0
                                                },
            "age & education & religious & method": {"U30_low_not-rel_none": 0, "U30_low_rel_none": 0,
                                                     "U30_low_not-rel_long": 0, "U30_low_rel_long": 0,
                                                     "U30_low_not-rel_short": 0, "U30_low_rel_short": 0,
                                                     "U30_avg_not-rel_none": 0, "U30_avg_rel_none": 0,
                                                     "U30_avg_not-rel_long": 0, "U30_avg_rel_long": 0,
                                                     "U30_avg_not-rel_short": 0, "U30_avg_rel_short": 0,
                                                     "U30_high_not-rel_none": 0, "U30_high_rel_none": 0,
                                                     "U30_high_not-rel_long": 0, "U30_high_rel_long": 0,
                                                     "U30_high_not-rel_short": 0, "U30_high_rel_short": 0,
                                                     "30-40_low_not-rel_none": 0, "30-40_low_rel_none": 0,
                                                     "30-40_low_not-rel_long": 0, "30-40_low_rel_long": 0,
                                                     "30-40_low_not-rel_short": 0, "30-40_low_rel_short": 0,
                                                     "30-40_avg_not-rel_none": 0, "30-40_avg_rel_none": 0,
                                                     "30-40_avg_not-rel_long": 0, "30-40_avg_rel_long": 0,
                                                     "30-40_avg_not-rel_short": 0, "30-40_avg_rel_short": 0,
                                                     "30-40_high_not-rel_none": 0, "30-40_high_rel_none": 0,
                                                     "30-40_high_not-rel_long": 0, "30-40_high_rel_long": 0,
                                                     "30-40_high_not-rel_short": 0, "30-40_high_rel_short": 0,
                                                     "40+_low_not-rel_none": 0, "40+_low_rel_none": 0,
                                                     "40+_low_not-rel_long": 0, "40+_low_rel_long": 0,
                                                     "40+_low_not-rel_short": 0, "40+_low_rel_short": 0,
                                                     "40+_avg_not-rel_none": 0, "40+_avg_rel_none": 0,
                                                     "40+_avg_not-rel_long": 0, "40+_avg_rel_long": 0,
                                                     "40+_avg_not-rel_short": 0, "40+_avg_rel_short": 0,
                                                     "40+_high_not-rel_none": 0, "40+_high_rel_none": 0,
                                                     "40+_high_not-rel_long": 0, "40+_high_rel_long": 0,
                                                     "40+_high_not-rel_short": 0, "40+_high_rel_short": 0
                                                     },
            "age & kids & religious & method": {"U30_U5_not-rel_none": 0, "U30_U5_rel_none": 0,
                                                "U30_U5_not-rel_long": 0, "U30_U5_rel_long": 0,
                                                "U30_U5_not-rel_short": 0, "U30_U5_rel_short": 0,
                                                "U30_5-9_not-rel_none": 0, "U30_5-9_rel_none": 0,
                                                "U30_5-9_not-rel_long": 0, "U30_5-9_rel_long": 0,
                                                "U30_5-9_not-rel_short": 0, "U30_5-9_rel_short": 0,
                                                "U30_10+_not-rel_none": 0, "U30_10+_rel_none": 0,
                                                "U30_10+_not-rel_long": 0, "U30_10+_rel_long": 0,
                                                "U30_10+_not-rel_short": 0, "U30_10+_rel_short": 0,
                                                "30-40_U5_not-rel_none": 0, "30-40_U5_rel_none": 0,
                                                "30-40_U5_not-rel_long": 0, "30-40_U5_rel_long": 0,
                                                "30-40_U5_not-rel_short": 0, "30-40_U5_rel_short": 0,
                                                "30-40_5-9_not-rel_none": 0, "30-40_5-9_rel_none": 0,
                                                "30-40_5-9_not-rel_long": 0, "30-40_5-9_rel_long": 0,
                                                "30-40_5-9_not-rel_short": 0, "30-40_5-9_rel_short": 0,
                                                "30-40_10+_not-rel_none": 0, "30-40_10+_rel_none": 0,
                                                "30-40_10+_not-rel_long": 0, "30-40_10+_rel_long": 0,
                                                "30-40_10+_not-rel_short": 0, "30-40_10+_rel_short": 0,
                                                "40+_U5_not-rel_none": 0, "40+_U5_rel_none": 0,
                                                "40+_U5_not-rel_long": 0, "40+_U5_rel_long": 0,
                                                "40+_U5_not-rel_short": 0, "40+_U5_rel_short": 0,
                                                "40+_5-9_not-rel_none": 0, "40+_5-9_rel_none": 0,
                                                "40+_5-9_not-rel_long": 0, "40+_5-9_rel_long": 0,
                                                "40+_5-9_not-rel_short": 0, "40+_5-9_rel_short": 0,
                                                "40+_10+_not-rel_none": 0, "40+_10+_rel_none": 0,
                                                "40+_10+_not-rel_long": 0, "40+_10+_rel_long": 0,
                                                "40+_10+_not-rel_short": 0, "40+_10+_rel_short": 0
                                                },
            "education & kids & religious & method": {"low_U5_not-rel_none": 0, "low_U5_rel_none": 0,
                                                      "low_U5_not-rel_long": 0, "low_U5_rel_long": 0,
                                                      "low_U5_not-rel_short": 0, "low_U5_rel_short": 0,
                                                      "low_5-9_not-rel_none": 0, "low_5-9_rel_none": 0,
                                                      "low_5-9_not-rel_long": 0, "low_5-9_rel_long": 0,
                                                      "low_5-9_not-rel_short": 0, "low_5-9_rel_short": 0,
                                                      "low_10+_not-rel_none": 0, "low_10+_rel_none": 0,
                                                      "low_10+_not-rel_long": 0, "low_10+_rel_long": 0,
                                                      "low_10+_not-rel_short": 0, "low_10+_rel_short": 0,
                                                      "avg_U5_not-rel_none": 0, "avg_U5_rel_none": 0,
                                                      "avg_U5_not-rel_long": 0, "avg_U5_rel_long": 0,
                                                      "avg_U5_not-rel_short": 0, "avg_U5_rel_short": 0,
                                                      "avg_5-9_not-rel_none": 0, "avg_5-9_rel_none": 0,
                                                      "avg_5-9_not-rel_long": 0, "avg_5-9_rel_long": 0,
                                                      "avg_5-9_not-rel_short": 0, "avg_5-9_rel_short": 0,
                                                      "avg_10+_not-rel_none": 0, "avg_10+_rel_none": 0,
                                                      "avg_10+_not-rel_long": 0, "avg_10+_rel_long": 0,
                                                      "avg_10+_not-rel_short": 0, "avg_10+_rel_short": 0,
                                                      "high_U5_not-rel_none": 0, "high_U5_rel_none": 0,
                                                      "high_U5_not-rel_long": 0, "high_U5_rel_long": 0,
                                                      "high_U5_not-rel_short": 0, "high_U5_rel_short": 0,
                                                      "high_5-9_not-rel_none": 0, "high_5-9_rel_none": 0,
                                                      "high_5-9_not-rel_long": 0, "high_5-9_rel_long": 0,
                                                      "high_5-9_not-rel_short": 0, "high_5-9_rel_short": 0,
                                                      "high_10+_not-rel_none": 0, "high_10+_rel_none": 0,
                                                      "high_10+_not-rel_long": 0, "high_10+_rel_long": 0,
                                                      "high_10+_not-rel_short": 0, "high_10+_rel_short": 0
                                                      },
        }

    def build_pentas(self):
        return {
            "age & education & kids & religious & method": {"U30_low_U5_not-rel_none": 0,
                                                            "U30_avg_U5_not-rel_none": 0,
                                                            "U30_high_U5_not-rel_none": 0,
                                                            "U30_low_U5_not-rel_long": 0,
                                                            "U30_avg_U5_not-rel_long": 0,
                                                            "U30_high_U5_not-rel_long": 0,
                                                            "U30_low_U5_not-rel_short": 0,
                                                            "U30_avg_U5_not-rel_short": 0,
                                                            "U30_high_U5_not-rel_short": 0,
                                                            "U30_low_U5_rel_none": 0,
                                                            "U30_avg_U5_rel_none": 0,
                                                            "U30_high_U5_rel_none": 0,
                                                            "U30_low_U5_rel_long": 0,
                                                            "U30_avg_U5_rel_long": 0,
                                                            "U30_high_U5_rel_long": 0,
                                                            "U30_low_U5_rel_short": 0,
                                                            "U30_avg_U5_rel_short": 0,
                                                            "U30_high_U5_rel_short": 0,
                                                            "U30_low_5-9_not-rel_none": 0,
                                                            "U30_avg_5-9_not-rel_none": 0,
                                                            "U30_high_5-9_not-rel_none": 0,
                                                            "U30_low_5-9_not-rel_long": 0,
                                                            "U30_avg_5-9_not-rel_long": 0,
                                                            "U30_high_5-9_not-rel_long": 0,
                                                            "U30_low_5-9_not-rel_short": 0,
                                                            "U30_avg_5-9_not-rel_short": 0,
                                                            "U30_high_5-9_not-rel_short": 0,
                                                            "U30_low_5-9_rel_none": 0,
                                                            "U30_avg_5-9_rel_none": 0,
                                                            "U30_high_5-9_rel_none": 0,
                                                            "U30_low_5-9_rel_long": 0,
                                                            "U30_avg_5-9_rel_long": 0,
                                                            "U30_high_5-9_rel_long": 0,
                                                            "U30_low_5-9_rel_short": 0,
                                                            "U30_avg_5-9_rel_short": 0,
                                                            "U30_high_5-9_rel_short": 0,
                                                            "U30_low_10+_not-rel_none": 0,
                                                            "U30_avg_10+_not-rel_none": 0,
                                                            "U30_high_10+_not-rel_none": 0,
                                                            "U30_low_10+_not-rel_long": 0,
                                                            "U30_avg_10+_not-rel_long": 0,
                                                            "U30_high_10+_not-rel_long": 0,
                                                            "U30_low_10+_not-rel_short": 0,
                                                            "U30_avg_10+_not-rel_short": 0,
                                                            "U30_high_10+_not-rel_short": 0,
                                                            "U30_low_10+_rel_none": 0,
                                                            "U30_avg_10+_rel_none": 0,
                                                            "U30_high_10+_rel_none": 0,
                                                            "U30_low_10+_rel_long": 0,
                                                            "U30_avg_10+_rel_long": 0,
                                                            "U30_high_10+_rel_long": 0,
                                                            "U30_low_10+_rel_short": 0,
                                                            "U30_avg_10+_rel_short": 0,
                                                            "U30_high_10+_rel_short": 0,
                                                            "30-40_low_U5_not-rel_none": 0,
                                                            "30-40_avg_U5_not-rel_none": 0,
                                                            "30-40_high_U5_not-rel_none": 0,
                                                            "30-40_low_U5_not-rel_long": 0,
                                                            "30-40_avg_U5_not-rel_long": 0,
                                                            "30-40_high_U5_not-rel_long": 0,
                                                            "30-40_low_U5_not-rel_short": 0,
                                                            "30-40_avg_U5_not-rel_short": 0,
                                                            "30-40_high_U5_not-rel_short": 0,
                                                            "30-40_low_U5_rel_none": 0,
                                                            "30-40_avg_U5_rel_none": 0,
                                                            "30-40_high_U5_rel_none": 0,
                                                            "30-40_low_U5_rel_long": 0,
                                                            "30-40_avg_U5_rel_long": 0,
                                                            "30-40_high_U5_rel_long": 0,
                                                            "30-40_low_U5_rel_short": 0,
                                                            "30-40_avg_U5_rel_short": 0,
                                                            "30-40_high_U5_rel_short": 0,
                                                            "30-40_low_5-9_not-rel_none": 0,
                                                            "30-40_avg_5-9_not-rel_none": 0,
                                                            "30-40_high_5-9_not-rel_none": 0,
                                                            "30-40_low_5-9_not-rel_long": 0,
                                                            "30-40_avg_5-9_not-rel_long": 0,
                                                            "30-40_high_5-9_not-rel_long": 0,
                                                            "30-40_low_5-9_not-rel_short": 0,
                                                            "30-40_avg_5-9_not-rel_short": 0,
                                                            "30-40_high_5-9_not-rel_short": 0,
                                                            "30-40_low_5-9_rel_none": 0,
                                                            "30-40_avg_5-9_rel_none": 0,
                                                            "30-40_high_5-9_rel_none": 0,
                                                            "30-40_low_5-9_rel_long": 0,
                                                            "30-40_avg_5-9_rel_long": 0,
                                                            "30-40_high_5-9_rel_long": 0,
                                                            "30-40_low_5-9_rel_short": 0,
                                                            "30-40_avg_5-9_rel_short": 0,
                                                            "30-40_high_5-9_rel_short": 0,
                                                            "30-40_low_10+_not-rel_none": 0,
                                                            "30-40_avg_10+_not-rel_none": 0,
                                                            "30-40_high_10+_not-rel_none": 0,
                                                            "30-40_low_10+_not-rel_long": 0,
                                                            "30-40_avg_10+_not-rel_long": 0,
                                                            "30-40_high_10+_not-rel_long": 0,
                                                            "30-40_low_10+_not-rel_short": 0,
                                                            "30-40_avg_10+_not-rel_short": 0,
                                                            "30-40_high_10+_not-rel_short": 0,
                                                            "30-40_low_10+_rel_none": 0,
                                                            "30-40_avg_10+_rel_none": 0,
                                                            "30-40_high_10+_rel_none": 0,
                                                            "30-40_low_10+_rel_long": 0,
                                                            "30-40_avg_10+_rel_long": 0,
                                                            "30-40_high_10+_rel_long": 0,
                                                            "30-40_low_10+_rel_short": 0,
                                                            "30-40_avg_10+_rel_short": 0,
                                                            "30-40_high_10+_rel_short": 0,
                                                            "40+_low_U5_not-rel_none": 0,
                                                            "40+_avg_U5_not-rel_none": 0,
                                                            "40+_high_U5_not-rel_none": 0,
                                                            "40+_low_U5_not-rel_long": 0,
                                                            "40+_avg_U5_not-rel_long": 0,
                                                            "40+_high_U5_not-rel_long": 0,
                                                            "40+_low_U5_not-rel_short": 0,
                                                            "40+_avg_U5_not-rel_short": 0,
                                                            "40+_high_U5_not-rel_short": 0,
                                                            "40+_low_U5_rel_none": 0,
                                                            "40+_avg_U5_rel_none": 0,
                                                            "40+_high_U5_rel_none": 0,
                                                            "40+_low_U5_rel_long": 0,
                                                            "40+_avg_U5_rel_long": 0,
                                                            "40+_high_U5_rel_long": 0,
                                                            "40+_low_U5_rel_short": 0,
                                                            "40+_avg_U5_rel_short": 0,
                                                            "40+_high_U5_rel_short": 0,
                                                            "40+_low_5-9_not-rel_none": 0,
                                                            "40+_avg_5-9_not-rel_none": 0,
                                                            "40+_high_5-9_not-rel_none": 0,
                                                            "40+_low_5-9_not-rel_long": 0,
                                                            "40+_avg_5-9_not-rel_long": 0,
                                                            "40+_high_5-9_not-rel_long": 0,
                                                            "40+_low_5-9_not-rel_short": 0,
                                                            "40+_avg_5-9_not-rel_short": 0,
                                                            "40+_high_5-9_not-rel_short": 0,
                                                            "40+_low_5-9_rel_none": 0,
                                                            "40+_avg_5-9_rel_none": 0,
                                                            "40+_high_5-9_rel_none": 0,
                                                            "40+_low_5-9_rel_long": 0,
                                                            "40+_avg_5-9_rel_long": 0,
                                                            "40+_high_5-9_rel_long": 0,
                                                            "40+_low_5-9_rel_short": 0,
                                                            "40+_avg_5-9_rel_short": 0,
                                                            "40+_high_5-9_rel_short": 0,
                                                            "40+_low_10+_not-rel_none": 0,
                                                            "40+_avg_10+_not-rel_none": 0,
                                                            "40+_high_10+_not-rel_none": 0,
                                                            "40+_low_10+_not-rel_long": 0,
                                                            "40+_avg_10+_not-rel_long": 0,
                                                            "40+_high_10+_not-rel_long": 0,
                                                            "40+_low_10+_not-rel_short": 0,
                                                            "40+_avg_10+_not-rel_short": 0,
                                                            "40+_high_10+_not-rel_short": 0,
                                                            "40+_low_10+_rel_none": 0,
                                                            "40+_avg_10+_rel_none": 0,
                                                            "40+_high_10+_rel_none": 0,
                                                            "40+_low_10+_rel_long": 0,
                                                            "40+_avg_10+_rel_long": 0,
                                                            "40+_high_10+_rel_long": 0,
                                                            "40+_low_10+_rel_short": 0,
                                                            "40+_avg_10+_rel_short": 0,
                                                            "40+_high_10+_rel_short": 0
                                                            }
            }

    def parse(self, db_name):
        database=open(db_name, "r")
        lines = database.readlines()    #arranges each line of the txt file in a cell of a list
        db_matrix=[]
        for l in lines:
            # def convert_str_arr_to_int_arr(s):
            s1 = (str(l)).replace(' ', '')
            s2 = s1.replace('[', '')
            s3 = s2.replace(']', '')
            s4 = s3.replace(',', ' ')
            sl = s4.split(' ')
            si = [int(elem) for elem in sl]
            sa = numpy.array(si)
                # return sa
            db_matrix.append(sa)
            # db_matrix.append(l.strip().split(","))
        return db_matrix
        # print(db_matrix[0])
        # print(len(db_matrix))

    def countValues(self, db_name):
        db_matrix = self.parse(db_name)
        for i in range(0, len(db_matrix)):
            if(db_matrix[i][0]<30):
                self.__attributes["age"]["U30"] +=1
                if(db_matrix[i][1] == 1):
                    self.__attributes["education"]["low"] += 1
                    self.__couples["age & education"]["U30_low"]+=1

                    if (db_matrix[i][3] < 5):
                        self.__trios["age & education & kids"]["U30_low_U5"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["U30_low_U5_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"]["U30_low_U5_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_U5_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_U5_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["U30_low_U5_rel"] += 1


                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_U5_rel_none"] += 1

                            elif (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_U5_rel_long"] += 1

                            elif (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_U5_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "U30_low_U5_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "U30_low_U5_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "U30_low_U5_short"] += 1

                    if (db_matrix[i][3] >= 10):
                        self.__trios["age & education & kids"]["U30_low_10+"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["U30_low_10+_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_10+_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_10+_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_10+_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["U30_low_10+_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_10+_rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_10+_rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_10+_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__pentas["age & education & kids & method"][
                                "U30_low_10+_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__pentas["age & education & kids & method"][
                                "U30_low_10+_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__pentas["age & education & kids & method"][
                                "U30_low_10+_short"] += 1

                    if (db_matrix[i][3] >= 5 and db_matrix[i][3] < 10):
                        self.__trios["age & education & kids"]["U30_low_5-9"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["U30_low_5-9_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_5-9_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_5-9_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_5-9_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["U30_low_5-9_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_5-9_rel_none"] += 1

                            elif (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_5-9_rel_long"] += 1

                            elif (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_low_5-9_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "U30_low_5-9_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "U30_low_5-9_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "U30_low_5-9_short"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & education & religious"]["U30_low_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "U30_low_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "U30_low_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "U30_low_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & education & religious"]["U30_low_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "U30_low_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "U30_low_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "U30_low_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & education & method"][
                            "U30_low_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & education & method"][
                            "U30_low_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & education & method"][
                            "U30_low_short"] += 1

                if(db_matrix[i][1] == 4):
                    self.__attributes["education"]["high"] += 1
                    self.__couples["age & education"]["U30_high"] += 1

                    if (db_matrix[i][3] < 5):
                        self.__trios["age & education & kids"]["U30_high_U5"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["U30_high_U5_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_U5_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_U5_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_U5_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["U30_high_U5_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_U5_rel_none"] += 1

                            elif (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_U5_rel_long"] += 1

                            elif (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_U5_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "U30_high_U5_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "U30_high_U5_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "U30_high_U5_short"] += 1

                    if (db_matrix[i][3] >= 10):
                        self.__trios["age & education & kids"]["U30_high_10+"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["U30_high_10+_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_10+_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_10+_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_10+_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["U30_high_10+_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_10+_rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_10+_rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_10+_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__pentas["age & education & kids & method"][
                                "U30_high_10+_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__pentas["age & education & kids & method"][
                                "U30_high_10+_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__pentas["age & education & kids & method"][
                                "U30_high_10+_short"] += 1

                    if (db_matrix[i][3] >= 5 and db_matrix[i][3] < 10):
                        self.__trios["age & education & kids"]["U30_high_5-9"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["U30_high_5-9_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_5-9_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_5-9_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_5-9_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["U30_high_5-9_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_5-9_rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_5-9_rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_high_5-9_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "U30_high_5-9_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "U30_high_5-9_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "U30_high_5-9_short"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & education & religious"]["U30_high_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "U30_high_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "U30_high_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "U30_high_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & education & religious"]["U30_high_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "U30_high_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "U30_high_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "U30_high_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & education & method"][
                            "U30_high_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & education & method"][
                            "U30_high_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & education & method"][
                            "U30_high_short"] += 1

                if(db_matrix[i][1] == 2 or db_matrix[i][1] == 3):# avg_edu
                    self.__attributes["education"]["avg"] += 1
                    self.__couples["age & education"]["U30_avg"] += 1

                    if (db_matrix[i][3] < 5):
                        self.__trios["age & education & kids"]["U30_avg_U5"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["U30_avg_U5_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_U5_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_U5_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_U5_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["U30_avg_U5_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_U5_rel_none"] += 1

                            elif (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_U5_rel_long"] += 1

                            elif (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_U5_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "U30_avg_U5_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "U30_avg_U5_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "U30_avg_U5_short"] += 1

                    if (db_matrix[i][3] >= 10):
                        self.__trios["age & education & kids"]["U30_avg_10+"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["U30_avg_10+_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_10+_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_10+_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_10+_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["U30_avg_10+_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_10+_rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_10+_rel_long"] += 1

                            if (db_matrix[i][9] == 3):

                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_10+_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "U30_avg_10+_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "U30_avg_10+_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "U30_avg_10+_short"] += 1

                    if (db_matrix[i][3] >= 5 and db_matrix[i][3] < 10):
                        self.__trios["age & education & kids"]["U30_avg_5-9"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["U30_avg_5-9_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_5-9_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_5-9_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_5-9_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["U30_avg_5-9_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_5-9_rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_5-9_rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "U30_avg_5-9_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "U30_avg_5-9_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "U30_avg_5-9_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "U30_avg_5-9_short"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & education & religious"]["U30_avg_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "U30_avg_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "U30_avg_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "U30_avg_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & education & religious"]["U30_avg_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "U30_avg_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "U30_avg_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "U30_avg_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & education & method"][
                            "U30_avg_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & education & method"][
                            "U30_avg_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & education & method"][
                            "U30_avg_short"] += 1

                if(db_matrix[i][3] < 5):
                    self.__attributes["kids"]["U5"] += 1
                    self.__couples["age & kids"]["U30_U5"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & kids & religious"]["U30_U5_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "U30_U5_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "U30_U5_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "U30_U5_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & kids & religious"]["U30_U5_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "U30_U5_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "U30_U5_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "U30_U5_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & kids & method"][
                            "U30_U5_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & kids & method"][
                            "U30_U5_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & kids & method"][
                            "U30_U5_short"] += 1

                if (db_matrix[i][3] >= 5 and db_matrix[i][3] <10):
                    self.__attributes["kids"]["5-9"] += 1
                    self.__couples["age & kids"]["U30_5-9"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & kids & religious"]["U30_5-9_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "U30_5-9_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "U30_5-9_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "U30_5-9_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & kids & religious"]["U30_5-9_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "U30_5-9_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "U30_5-9_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "U30_5-9_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & kids & method"][
                            "U30_5-9_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & kids & method"][
                            "U30_5-9_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & kids & method"][
                            "U30_5-9_short"] += 1

                if (db_matrix[i][3] >= 10):
                    self.__attributes["kids"]["10+"] += 1
                    self.__couples["age & kids"]["U30_10+"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & kids & religious"]["U30_10+_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "U30_10+_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "U30_10+_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "U30_10+_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & kids & religious"]["U30_10+_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "U30_10+_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "U30_10+_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "U30_10+_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & kids & method"][
                            "U30_10+_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & kids & method"][
                            "U30_10+_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & kids & method"][
                            "U30_10+_short"] += 1

                if(db_matrix[i][4] == 0):
                    self.__attributes["religious"]["not-rel"] += 1
                    self.__couples["age & religious"]["U30_not-rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & religious & method"][
                            "U30_not-rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & religious & method"][
                            "U30_not-rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & religious & method"][
                            "U30_not-rel_short"] += 1

                if (db_matrix[i][4] == 1):
                    self.__attributes["religious"]["rel"] += 1
                    self.__couples["age & religious"]["U30_rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & religious & method"][
                            "U30_rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & religious & method"][
                            "U30_rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & religious & method"][
                            "U30_rel_short"] += 1

                if (db_matrix[i][9] == 1):
                    self.__attributes["method"]["none"] += 1
                    self.__couples["age & method"]["U30_none"] += 1

                if (db_matrix[i][9] == 2):
                    self.__attributes["method"]["long"] += 1
                    self.__couples["age & method"]["U30_long"] += 1

                if (db_matrix[i][9] == 3):
                    self.__attributes["method"]["short"] += 1
                    self.__couples["age & method"]["U30_short"] += 1

            if(db_matrix[i][0]>40):
                self.__attributes["age"]["40+"] += 1

                if (db_matrix[i][1] == 1):
                    self.__attributes["education"]["low"] += 1
                    self.__couples["age & education"]["40+_low"] += 1

                    if (db_matrix[i][3] < 5):
                        self.__trios["age & education & kids"]["40+_low_U5"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["40+_low_U5_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_U5_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_U5_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_U5_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["40+_low_U5_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_U5_rel_none"] += 1

                            elif (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_U5_rel_long"] += 1

                            elif (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_U5_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "40+_low_U5_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "40+_low_U5_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "40+_low_U5_short"] += 1

                    if (db_matrix[i][3] >= 10):
                        self.__trios["age & education & kids"]["40+_low_10+"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["40+_low_10+_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_10+_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_10+_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_10+_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["40+_low_10+_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_10+_rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_10+_rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_10+_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "40+_low_10+_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "40+_low_10+_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "40+_low_10+_short"] += 1

                    if (db_matrix[i][3] >= 5 and db_matrix[i][3] < 10):
                        self.__trios["age & education & kids"]["40+_low_5-9"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["40+_low_5-9_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_5-9_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_5-9_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_5-9_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["40+_low_5-9_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_5-9_rel_none"] += 1

                            elif (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_5-9_rel_long"] += 1

                            elif (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_low_5-9_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "40+_low_5-9_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "40+_low_5-9_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "40+_low_5-9_short"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & education & religious"]["40+_low_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "40+_low_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "40+_low_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "40+_low_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & education & religious"]["40+_low_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "40+_low_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "40+_low_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "40+_low_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & education & method"][
                            "40+_low_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & education & method"][
                            "40+_low_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & education & method"][
                            "40+_low_short"] += 1

                if (db_matrix[i][1] == 4):
                    self.__attributes["education"]["high"] += 1
                    self.__couples["age & education"]["40+_high"] += 1

                    if (db_matrix[i][3] < 5):
                        self.__trios["age & education & kids"]["40+_high_U5"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["40+_high_U5_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_U5_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_U5_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_U5_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["40+_high_U5_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_U5_rel_none"] += 1

                            elif (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_U5_rel_long"] += 1

                            elif (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_U5_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "40+_high_U5_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "40+_high_U5_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "40+_high_U5_short"] += 1

                    if (db_matrix[i][3] >= 10):
                        self.__trios["age & education & kids"]["40+_high_10+"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["40+_high_10+_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_10+_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_10+_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_10+_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["40+_high_10+_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_10+_rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_10+_rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_10+_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "40+_high_10+_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "40+_high_10+_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "40+_high_10+_short"] += 1

                    if (db_matrix[i][3] >= 5 and db_matrix[i][3] < 10):
                        self.__trios["age & education & kids"]["40+_high_5-9"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["40+_high_5-9_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_5-9_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_5-9_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_5-9_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["40+_high_5-9_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_5-9_rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_5-9_rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_high_5-9_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "40+_high_5-9_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "40+_high_5-9_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "40+_high_5-9_short"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & education & religious"]["40+_high_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "40+_high_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "40+_high_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "40+_high_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & education & religious"]["40+_high_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "40+_high_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "40+_high_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "40+_high_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & education & method"][
                            "40+_high_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & education & method"][
                            "40+_high_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & education & method"][
                            "40+_high_short"] += 1

                if (db_matrix[i][1] == 2 or db_matrix[i][1] == 3):  # avg_edu
                    self.__attributes["education"]["avg"] += 1
                    self.__couples["age & education"]["40+_avg"] += 1

                    if (db_matrix[i][3] < 5):
                        self.__trios["age & education & kids"]["40+_avg_U5"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["40+_avg_U5_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_U5_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_U5_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_U5_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["40+_avg_U5_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_U5_rel_none"] += 1

                            elif (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_U5_rel_long"] += 1

                            elif (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_U5_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "40+_avg_U5_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "40+_avg_U5_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "40+_avg_U5_short"] += 1

                    if (db_matrix[i][3] >= 10):
                        self.__trios["age & education & kids"]["40+_avg_10+"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["40+_avg_10+_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_10+_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_10+_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_10+_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["40+_avg_10+_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_10+_rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_10+_rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_10+_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "40+_avg_10+_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "40+_avg_10+_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "40+_avg_10+_short"] += 1

                    if (db_matrix[i][3] >= 5 and db_matrix[i][3] < 10):
                        self.__trios["age & education & kids"]["40+_avg_5-9"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["40+_avg_5-9_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_5-9_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_5-9_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_5-9_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["40+_avg_5-9_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_5-9_rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_5-9_rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "40+_avg_5-9_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "40+_avg_5-9_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "40+_avg_5-9_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "40+_avg_5-9_short"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & education & religious"]["40+_avg_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "40+_avg_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "40+_avg_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "40+_avg_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & education & religious"]["40+_avg_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "40+_avg_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "40+_avg_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "40+_avg_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & education & method"][
                            "40+_avg_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & education & method"][
                            "40+_avg_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & education & method"][
                            "40+_avg_short"] += 1

                if (db_matrix[i][3] < 5):
                    self.__attributes["kids"]["U5"] += 1
                    self.__couples["age & kids"]["40+_U5"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & kids & religious"]["40+_U5_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "40+_U5_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "40+_U5_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "40+_U5_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & kids & religious"]["40+_U5_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "40+_U5_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "40+_U5_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "40+_U5_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & kids & method"][
                            "40+_U5_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & kids & method"][
                            "40+_U5_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & kids & method"][
                            "40+_U5_short"] += 1

                if (db_matrix[i][3] >= 5 and db_matrix[i][3] < 10):
                    self.__attributes["kids"]["5-9"] += 1
                    self.__couples["age & kids"]["40+_5-9"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & kids & religious"]["40+_5-9_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "40+_5-9_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "40+_5-9_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "40+_5-9_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & kids & religious"]["40+_5-9_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "40+_5-9_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "40+_5-9_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "40+_5-9_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & kids & method"][
                            "40+_5-9_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & kids & method"][
                            "40+_5-9_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & kids & method"][
                            "40+_5-9_short"] += 1

                if (db_matrix[i][3] >= 10):
                    self.__attributes["kids"]["10+"] += 1
                    self.__couples["age & kids"]["40+_10+"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & kids & religious"]["40+_10+_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "40+_10+_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "40+_10+_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "40+_10+_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & kids & religious"]["40+_10+_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "40+_10+_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "40+_10+_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "40+_10+_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & kids & method"][
                            "40+_10+_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & kids & method"][
                            "40+_10+_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & kids & method"][
                            "40+_10+_short"] += 1

                if (db_matrix[i][4] == 0):
                    self.__attributes["religious"]["not-rel"] += 1
                    self.__couples["age & religious"]["40+_not-rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & religious & method"][
                            "40+_not-rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & religious & method"][
                            "40+_not-rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & religious & method"][
                            "40+_not-rel_short"] += 1

                if (db_matrix[i][4] == 1):
                    self.__attributes["religious"]["rel"] += 1
                    self.__couples["age & religious"]["40+_rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & religious & method"][
                            "40+_rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & religious & method"][
                            "40+_rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & religious & method"][
                            "40+_rel_short"] += 1

                if (db_matrix[i][9] == 1):
                    self.__attributes["method"]["none"] += 1
                    self.__couples["age & method"]["40+_none"] += 1

                if (db_matrix[i][9] == 2):
                    self.__attributes["method"]["long"] += 1
                    self.__couples["age & method"]["40+_long"] += 1

                if (db_matrix[i][9] == 3):
                    self.__attributes["method"]["short"] += 1
                    self.__couples["age & method"]["40+_short"] += 1

            if (db_matrix[i][0] >= 30 and db_matrix[i][0] <= 40):
                self.__attributes["age"]["30-40"] += 1

                if(db_matrix[i][1] == 1):
                    self.__attributes["education"]["low"] += 1
                    self.__couples["age & education"]["30-40_low"]+=1

                    if (db_matrix[i][3] < 5):
                        self.__trios["age & education & kids"]["30-40_low_U5"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["30-40_low_U5_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"]["30-40_low_U5_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_U5_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_U5_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["30-40_low_U5_rel"] += 1


                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_U5_rel_none"] += 1

                            elif (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_U5_rel_long"] += 1

                            elif (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_U5_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "30-40_low_U5_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "30-40_low_U5_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "30-40_low_U5_short"] += 1

                    if (db_matrix[i][3] >= 10):
                        self.__trios["age & education & kids"]["30-40_low_10+"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["30-40_low_10+_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_10+_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_10+_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_10+_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["30-40_low_10+_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_10+_rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_10+_rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_10+_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "30-40_low_10+_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "30-40_low_10+_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "30-40_low_10+_short"] += 1

                    if (db_matrix[i][3] >= 5 and db_matrix[i][3] < 10):
                        self.__trios["age & education & kids"]["30-40_low_5-9"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["30-40_low_5-9_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_5-9_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_5-9_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_5-9_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["30-40_low_5-9_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_5-9_rel_none"] += 1

                            elif (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_5-9_rel_long"] += 1

                            elif (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_low_5-9_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "30-40_low_5-9_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "30-40_low_5-9_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "30-40_low_5-9_short"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & education & religious"]["30-40_low_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "30-40_low_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "30-40_low_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "30-40_low_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & education & religious"]["30-40_low_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "30-40_low_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "30-40_low_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "30-40_low_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & education & method"][
                            "30-40_low_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & education & method"][
                            "30-40_low_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & education & method"][
                            "30-40_low_short"] += 1

                if(db_matrix[i][1] == 4):
                    self.__attributes["education"]["high"] += 1
                    self.__couples["age & education"]["30-40_high"] += 1

                    if (db_matrix[i][3] < 5):
                        self.__trios["age & education & kids"]["30-40_high_U5"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["30-40_high_U5_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_U5_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_U5_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_U5_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["30-40_high_U5_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_U5_rel_none"] += 1

                            elif (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_U5_rel_long"] += 1

                            elif (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_U5_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "30-40_high_U5_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "30-40_high_U5_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "30-40_high_U5_short"] += 1

                    if (db_matrix[i][3] >= 10):
                        self.__trios["age & education & kids"]["30-40_high_10+"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["30-40_high_10+_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_10+_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_10+_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_10+_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["30-40_high_10+_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_10+_rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_10+_rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_10+_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "30-40_high_10+_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "30-40_high_10+_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "30-40_high_10+_short"] += 1

                    if (db_matrix[i][3] >= 5 and db_matrix[i][3] < 10):
                        self.__trios["age & education & kids"]["30-40_high_5-9"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["30-40_high_5-9_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_5-9_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_5-9_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_5-9_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["30-40_high_5-9_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_5-9_rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_5-9_rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_high_5-9_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "30-40_high_5-9_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "30-40_high_5-9_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "30-40_high_5-9_short"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & education & religious"]["30-40_high_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "30-40_high_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "30-40_high_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "30-40_high_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & education & religious"]["30-40_high_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "30-40_high_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "30-40_high_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "30-40_high_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & education & method"][
                            "30-40_high_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & education & method"][
                            "30-40_high_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & education & method"][
                            "30-40_high_short"] += 1

                if(db_matrix[i][1] == 2 or db_matrix[i][1] == 3):# avg_edu
                    self.__attributes["education"]["avg"] += 1
                    self.__couples["age & education"]["30-40_avg"] += 1

                    if (db_matrix[i][3] < 5):
                        self.__trios["age & education & kids"]["30-40_avg_U5"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["30-40_avg_U5_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_U5_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_U5_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_U5_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["30-40_avg_U5_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_U5_rel_none"] += 1

                            elif (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_U5_rel_long"] += 1

                            elif (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_U5_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "30-40_avg_U5_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "30-40_avg_U5_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "30-40_avg_U5_short"] += 1

                    if (db_matrix[i][3] >= 10):
                        self.__trios["age & education & kids"]["30-40_avg_10+"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["30-40_avg_10+_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_10+_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_10+_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_10+_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["30-40_avg_10+_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_10+_rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_10+_rel_long"] += 1

                            if (db_matrix[i][9] == 3):

                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_10+_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "30-40_avg_10+_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "30-40_avg_10+_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "30-40_avg_10+_short"] += 1

                    if (db_matrix[i][3] >= 5 and db_matrix[i][3] < 10):
                        self.__trios["age & education & kids"]["30-40_avg_5-9"] += 1

                        if (db_matrix[i][4] == 0):
                            self.__quads["age & education & kids & religious"]["30-40_avg_5-9_not-rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_5-9_not-rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_5-9_not-rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_5-9_not-rel_short"] += 1

                        if (db_matrix[i][4] == 1):
                            self.__quads["age & education & kids & religious"]["30-40_avg_5-9_rel"] += 1

                            if (db_matrix[i][9] == 1):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_5-9_rel_none"] += 1

                            if (db_matrix[i][9] == 2):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_5-9_rel_long"] += 1

                            if (db_matrix[i][9] == 3):
                                self.__pentas["age & education & kids & religious & method"][
                                    "30-40_avg_5-9_rel_short"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & kids & method"][
                                "30-40_avg_5-9_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & kids & method"][
                                "30-40_avg_5-9_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & kids & method"][
                                "30-40_avg_5-9_short"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & education & religious"]["30-40_avg_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "30-40_avg_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "30-40_avg_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "30-40_avg_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & education & religious"]["30-40_avg_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & education & religious & method"][
                                "30-40_avg_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & education & religious & method"][
                                "30-40_avg_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & education & religious & method"][
                                "30-40_avg_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & education & method"][
                            "30-40_avg_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & education & method"][
                            "30-40_avg_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & education & method"][
                            "30-40_avg_short"] += 1

                if(db_matrix[i][3] < 5):
                    self.__attributes["kids"]["U5"] += 1
                    self.__couples["age & kids"]["30-40_U5"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & kids & religious"]["30-40_U5_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "30-40_U5_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "30-40_U5_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "30-40_U5_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & kids & religious"]["30-40_U5_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "30-40_U5_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "30-40_U5_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "30-40_U5_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & kids & method"][
                            "30-40_U5_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & kids & method"][
                            "30-40_U5_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & kids & method"][
                            "30-40_U5_short"] += 1

                if (db_matrix[i][3] >= 5 and db_matrix[i][3] <10):
                    self.__attributes["kids"]["5-9"] += 1
                    self.__couples["age & kids"]["30-40_5-9"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & kids & religious"]["30-40_5-9_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "30-40_5-9_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "30-40_5-9_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "30-40_5-9_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & kids & religious"]["30-40_5-9_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "30-40_5-9_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "30-40_5-9_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "30-40_5-9_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & kids & method"][
                            "30-40_5-9_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & kids & method"][
                            "30-40_5-9_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & kids & method"][
                            "30-40_5-9_short"] += 1

                if (db_matrix[i][3] >= 10):
                    self.__attributes["kids"]["10+"] += 1
                    self.__couples["age & kids"]["30-40_10+"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["age & kids & religious"]["30-40_10+_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "30-40_10+_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "30-40_10+_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "30-40_10+_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["age & kids & religious"]["30-40_10+_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["age & kids & religious & method"][
                                "30-40_10+_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["age & kids & religious & method"][
                                "30-40_10+_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["age & kids & religious & method"][
                                "30-40_10+_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & kids & method"][
                            "30-40_10+_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & kids & method"][
                            "30-40_10+_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & kids & method"][
                            "30-40_10+_short"] += 1

                if(db_matrix[i][4] == 0):
                    self.__attributes["religious"]["not-rel"] += 1
                    self.__couples["age & religious"]["30-40_not-rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & religious & method"][
                            "30-40_not-rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & religious & method"][
                            "30-40_not-rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & religious & method"][
                            "30-40_not-rel_short"] += 1

                if (db_matrix[i][4] == 1):
                    self.__attributes["religious"]["rel"] += 1
                    self.__couples["age & religious"]["30-40_rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["age & religious & method"][
                            "30-40_rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["age & religious & method"][
                            "30-40_rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["age & religious & method"][
                            "30-40_rel_short"] += 1

                if (db_matrix[i][9] == 1):
                    self.__attributes["method"]["none"] += 1
                    self.__couples["age & method"]["30-40_none"] += 1

                if (db_matrix[i][9] == 2):
                    self.__attributes["method"]["long"] += 1
                    self.__couples["age & method"]["30-40_long"] += 1

                if (db_matrix[i][9] == 3):
                    self.__attributes["method"]["short"] += 1
                    self.__couples["age & method"]["30-40_short"] += 1



            if (db_matrix[i][1] == 1):

                if (db_matrix[i][3] < 5):
                    self.__couples["education & kids"]["low_U5"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["education & kids & religious"]["low_U5_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"]["low_U5_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "low_U5_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "low_U5_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["education & kids & religious"]["low_U5_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "low_U5_rel_none"] += 1

                        elif (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "low_U5_rel_long"] += 1

                        elif (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "low_U5_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["education & kids & method"][
                            "low_U5_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["education & kids & method"][
                            "low_U5_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["education & kids & method"][
                            "low_U5_short"] += 1

                if (db_matrix[i][3] >= 10):
                    self.__couples["education & kids"]["low_10+"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["education & kids & religious"]["low_10+_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "low_10+_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "low_10+_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "low_10+_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["education & kids & religious"]["low_10+_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "low_10+_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "low_10+_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "low_10+_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["education & kids & method"][
                            "low_10+_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["education & kids & method"][
                            "low_10+_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["education & kids & method"][
                            "low_10+_short"] += 1

                if (db_matrix[i][3] >= 5 and db_matrix[i][3] < 10):
                    self.__couples["education & kids"]["low_5-9"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["education & kids & religious"]["low_5-9_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "low_5-9_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "low_5-9_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "low_5-9_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["education & kids & religious"]["low_5-9_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "low_5-9_rel_none"] += 1

                        elif (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "low_5-9_rel_long"] += 1

                        elif (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "low_5-9_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["education & kids & method"][
                            "low_5-9_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["education & kids & method"][
                            "low_5-9_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["education & kids & method"][
                            "low_5-9_short"] += 1

                if (db_matrix[i][4] == 0):
                    self.__couples["education & religious"]["low_not-rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["education & religious & method"][
                            "low_not-rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["education & religious & method"][
                            "low_not-rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["education & religious & method"][
                            "low_not-rel_short"] += 1

                if (db_matrix[i][4] == 1):
                    self.__couples["education & religious"]["low_rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["education & religious & method"][
                            "low_rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["education & religious & method"][
                            "low_rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["education & religious & method"][
                            "low_rel_short"] += 1

                if (db_matrix[i][9] == 1):
                    self.__couples["education & method"][
                        "low_none"] += 1

                if (db_matrix[i][9] == 2):
                    self.__couples["education & method"][
                        "low_long"] += 1

                if (db_matrix[i][9] == 3):
                    self.__couples["education & method"][
                        "low_short"] += 1

            if (db_matrix[i][1] == 4):

                if (db_matrix[i][3] < 5):
                    self.__couples["education & kids"]["high_U5"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["education & kids & religious"]["high_U5_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "high_U5_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "high_U5_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "high_U5_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["education & kids & religious"]["high_U5_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "high_U5_rel_none"] += 1

                        elif (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "high_U5_rel_long"] += 1

                        elif (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "high_U5_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["education & kids & method"][
                            "high_U5_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["education & kids & method"][
                            "high_U5_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["education & kids & method"][
                            "high_U5_short"] += 1

                if (db_matrix[i][3] >= 10):
                    self.__couples["education & kids"]["high_10+"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["education & kids & religious"]["high_10+_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "high_10+_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "high_10+_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "high_10+_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["education & kids & religious"]["high_10+_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "high_10+_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "high_10+_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "high_10+_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["education & kids & method"][
                            "high_10+_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["education & kids & method"][
                            "high_10+_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["education & kids & method"][
                            "high_10+_short"] += 1

                if (db_matrix[i][3] >= 5 and db_matrix[i][3] < 10):
                    self.__couples["education & kids"]["high_5-9"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["education & kids & religious"]["high_5-9_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "high_5-9_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "high_5-9_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "high_5-9_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["education & kids & religious"]["high_5-9_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "high_5-9_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "high_5-9_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "high_5-9_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["education & kids & method"][
                            "high_5-9_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["education & kids & method"][
                            "high_5-9_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["education & kids & method"][
                            "high_5-9_short"] += 1

                if (db_matrix[i][4] == 0):
                    self.__couples["education & religious"]["high_not-rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["education & religious & method"][
                            "high_not-rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["education & religious & method"][
                            "high_not-rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["education & religious & method"][
                            "high_not-rel_short"] += 1

                if (db_matrix[i][4] == 1):
                    self.__couples["education & religious"]["high_rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["education & religious & method"][
                            "high_rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["education & religious & method"][
                            "high_rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["education & religious & method"][
                            "high_rel_short"] += 1

                if (db_matrix[i][9] == 1):
                    self.__couples["education & method"][
                        "high_none"] += 1

                if (db_matrix[i][9] == 2):
                    self.__couples["education & method"][
                        "high_long"] += 1

                if (db_matrix[i][9] == 3):
                    self.__couples["education & method"][
                        "high_short"] += 1

            if (db_matrix[i][1] == 2 or db_matrix[i][1] == 3):  # avg_edu

                if (db_matrix[i][3] < 5):
                    self.__couples["education & kids"]["avg_U5"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["education & kids & religious"]["avg_U5_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "avg_U5_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "avg_U5_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "avg_U5_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["education & kids & religious"]["avg_U5_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "avg_U5_rel_none"] += 1

                        elif (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "avg_U5_rel_long"] += 1

                        elif (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "avg_U5_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["education & kids & method"][
                            "avg_U5_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["education & kids & method"][
                            "avg_U5_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["education & kids & method"][
                            "avg_U5_short"] += 1

                if (db_matrix[i][3] >= 10):
                    self.__couples["education & kids"]["avg_10+"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["education & kids & religious"]["avg_10+_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "avg_10+_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "avg_10+_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "avg_10+_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["education & kids & religious"]["avg_10+_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "avg_10+_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "avg_10+_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "avg_10+_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["education & kids & method"][
                            "avg_10+_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["education & kids & method"][
                            "avg_10+_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["education & kids & method"][
                            "avg_10+_short"] += 1

                if (db_matrix[i][3] >= 5 and db_matrix[i][3] < 10):
                    self.__couples["education & kids"]["avg_5-9"] += 1

                    if (db_matrix[i][4] == 0):
                        self.__trios["education & kids & religious"]["avg_5-9_not-rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "avg_5-9_not-rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "avg_5-9_not-rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "avg_5-9_not-rel_short"] += 1

                    if (db_matrix[i][4] == 1):
                        self.__trios["education & kids & religious"]["avg_5-9_rel"] += 1

                        if (db_matrix[i][9] == 1):
                            self.__quads["education & kids & religious & method"][
                                "avg_5-9_rel_none"] += 1

                        if (db_matrix[i][9] == 2):
                            self.__quads["education & kids & religious & method"][
                                "avg_5-9_rel_long"] += 1

                        if (db_matrix[i][9] == 3):
                            self.__quads["education & kids & religious & method"][
                                "avg_5-9_rel_short"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["education & kids & method"][
                            "avg_5-9_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["education & kids & method"][
                            "avg_5-9_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["education & kids & method"][
                            "avg_5-9_short"] += 1

                if (db_matrix[i][4] == 0):
                    self.__couples["education & religious"]["avg_not-rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["education & religious & method"][
                            "avg_not-rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["education & religious & method"][
                            "avg_not-rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["education & religious & method"][
                            "avg_not-rel_short"] += 1

                if (db_matrix[i][4] == 1):
                    self.__couples["education & religious"]["avg_rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["education & religious & method"][
                            "avg_rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["education & religious & method"][
                            "avg_rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["education & religious & method"][
                            "avg_rel_short"] += 1

                if (db_matrix[i][9] == 1):
                    self.__couples["education & method"][
                        "avg_none"] += 1

                if (db_matrix[i][9] == 2):
                    self.__couples["education & method"][
                        "avg_long"] += 1

                if (db_matrix[i][9] == 3):
                    self.__couples["education & method"][
                        "avg_short"] += 1

            if (db_matrix[i][3] < 5):

                if (db_matrix[i][4] == 0):
                    self.__couples["kids & religious"]["U5_not-rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["kids & religious & method"][
                            "U5_not-rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["kids & religious & method"][
                            "U5_not-rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["kids & religious & method"][
                            "U5_not-rel_short"] += 1

                if (db_matrix[i][4] == 1):
                    self.__couples["kids & religious"]["U5_rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["kids & religious & method"][
                            "U5_rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["kids & religious & method"][
                            "U5_rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["kids & religious & method"][
                            "U5_rel_short"] += 1

                if (db_matrix[i][9] == 1):
                    self.__couples["kids & method"][
                        "U5_none"] += 1

                if (db_matrix[i][9] == 2):
                    self.__couples["kids & method"][
                        "U5_long"] += 1

                if (db_matrix[i][9] == 3):
                    self.__couples["kids & method"][
                        "U5_short"] += 1

            if (db_matrix[i][3] >= 5 and db_matrix[i][3] < 10):

                if (db_matrix[i][4] == 0):
                    self.__couples["kids & religious"]["5-9_not-rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["kids & religious & method"][
                            "5-9_not-rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["kids & religious & method"][
                            "5-9_not-rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["kids & religious & method"][
                            "5-9_not-rel_short"] += 1

                if (db_matrix[i][4] == 1):
                    self.__couples["kids & religious"]["5-9_rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["kids & religious & method"][
                            "5-9_rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["kids & religious & method"][
                            "5-9_rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["kids & religious & method"][
                            "5-9_rel_short"] += 1

                if (db_matrix[i][9] == 1):
                    self.__couples["kids & method"][
                        "5-9_none"] += 1

                if (db_matrix[i][9] == 2):
                    self.__couples["kids & method"][
                        "5-9_long"] += 1

                if (db_matrix[i][9] == 3):
                    self.__couples["kids & method"][
                        "5-9_short"] += 1

            if (db_matrix[i][3] >= 10):

                if (db_matrix[i][4] == 0):
                    self.__couples["kids & religious"]["10+_not-rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["kids & religious & method"][
                            "10+_not-rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["kids & religious & method"][
                            "10+_not-rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["kids & religious & method"][
                            "10+_not-rel_short"] += 1

                if (db_matrix[i][4] == 1):
                    self.__couples["kids & religious"]["10+_rel"] += 1

                    if (db_matrix[i][9] == 1):
                        self.__trios["kids & religious & method"][
                            "10+_rel_none"] += 1

                    if (db_matrix[i][9] == 2):
                        self.__trios["kids & religious & method"][
                            "10+_rel_long"] += 1

                    if (db_matrix[i][9] == 3):
                        self.__trios["kids & religious & method"][
                            "10+_rel_short"] += 1

                if (db_matrix[i][9] == 1):
                    self.__couples["kids & method"][
                        "10+_none"] += 1

                if (db_matrix[i][9] == 2):
                    self.__couples["kids & method"][
                        "10+_long"] += 1

                if (db_matrix[i][9] == 3):
                    self.__couples["kids & method"][
                        "10+_short"] += 1

            if (db_matrix[i][4] == 0):

                if (db_matrix[i][9] == 1):
                    self.__couples["religious & method"][
                        "not-rel_none"] += 1

                if (db_matrix[i][9] == 2):
                    self.__couples["religious & method"][
                        "not-rel_long"] += 1

                if (db_matrix[i][9] == 3):
                    self.__couples["religious & method"][
                        "not-rel_short"] += 1

            if (db_matrix[i][4] == 1):

                if (db_matrix[i][9] == 1):
                    self.__couples["religious & method"][
                        "rel_none"] += 1

                if (db_matrix[i][9] == 2):
                    self.__couples["religious & method"][
                        "rel_long"] += 1

                if (db_matrix[i][9] == 3):
                    self.__couples["religious & method"][
                        "rel_short"] += 1