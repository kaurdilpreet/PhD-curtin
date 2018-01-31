#! user/bin/env/python

def list_properties():
    return "have smaller emission region", "have much stable pulse period", "are recycled pulsars", "have smaller spin down rate"


def build_sentence(start):
    return "Millisecond pulsars %s." % start


def name_the_properties_of_pulsars():
    list_of_properties = list_properties()
    for start in list_of_properties:
        print(build_sentence(start))

name_the_properties_of_pulsars()

