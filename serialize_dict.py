import pickle

# denne fil er kun til tests af serialisering

'''
# create file:
dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }
filename = 'dogs'
outfile = open(filename, 'wb')
pickle.dump(dogs_dict, outfile)
'''

# read file:
infile = open('dogs','rb')
new_dict = pickle.load(infile)
infile.close()
print(new_dict)
