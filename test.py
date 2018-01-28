#! user/bin/env/python

Name = "Pulsar 'abc'"
p = 2.13
P = p/1000

LC = 4.77e4 * P

print ("LC: %d km" %LC)

if LC < 100:
    print("%s has small radius of LC." % Name)
else:
    print("%s has normal radius of LC." % Name)


