#open file
#file name
fname='./imdb1.csv'
#check if file exists
from os.path import exists
print(exists(fname))
#loop through the file and print each line
frh=open(fname, 'r', encoding='utf-8', errors='ignore')
for line in frh:
    print(line)
frh.close()
print('-'*60)
#split
frh=open(fname, 'r', encoding='utf-8', errors='ignore')
for line in frh:
    ls=line.split(',')
    print(ls)
frh.close()
print('-'*60)
#strip
#string.strip([characters])  whitespace removed from string, use characters to be specific
frh=open(fname, 'r', encoding='utf-8', errors='ignore')
for line in frh:
    ls=line.split(',')
    title=(ls[11]).strip()
    print(title)
frh.close()
print('-'*60)
##
frh=open(fname, 'r', encoding='utf-8', errors='ignore')
for line in frh:
    ls=line.split(',')
    title=(ls[11]).strip()
    rating=(ls[25]).strip()
    print(title, rating)
frh.close()
print('-'*60)
##
frh=open(fname, 'r', encoding='utf-8', errors='ignore')
for line in frh:
    ls=line.split(',')
    director=(ls[1]).strip()
    title=(ls[11]).strip()
    rating=(ls[25]).strip()
    print(director, title, rating)
frh.close()
print('-'*60)
## creating {title, rating}
# 'The Icestorm':'7.5', 'Unforgiven':'8.3'
frh=open(fname, 'r', encoding='utf-8', errors='ignore')
imdbD={}
frh.readline()
for line in frh:
    ls=line.split(',')
    title=(ls[11]).strip()
    rating=(ls[25]).strip()
    print(director, title, rating)
    if (title not in imdbD.keys()):
        imdbD[title]=rating
        print(imdbD)
# create {director:{title:rank}}
userMR={}
frh=open(fname, 'r', encoding='utf-8', errors='ignore')
imdbND={}
frh.readline()
for line in frh:
    ls=line.split(',')
    director=(ls[1]).strip()
    title=(ls[11]).strip()
    rating=(ls[25]).strip()
    if director in imdbND.keys():
       titleratings= imdbND[director]
    else:
        titleratings={}
        titleratings[title]=rating
        imdbND[director]=titleratings
        print(imdbND)
frh.close()
print('#'*60)
fname='dmr.csv'
print(exists(fname))
frh=open(fname, 'w', encoding='utf-8', errors='ignore')
frh.write("Director,Title, Ratings\n")
for director , movieRatings in imdbND.items():
    for movie, rating in movieRatings.items():
        frh.write(director + "," + movie +","+rating+"\n")
frh.close()
print('-'*60)    
#check what was written
frh=open(fname, 'r')
print(frh.read())
frh.close()
print()
print('-'*60)    
## aswering the question
UserMovieRating={
"Amy":{"Family Plot":10, "Rebecca":5,"Spellbound":9,"Star":6},
"Bill":{"Apacalypto":8, "Braveheart":3,"Rebecca ":10,"Spellbound":5,"Star":7},
"Cathy":{"Spaceballs":7, "Ice Storm":4,"Family Plot":5,"Rebecca":9,"Spellbound":1},"Dave":{"Braveheart":5, "Rebecca":7,"Spellbound":4},
"Ernie":{"Apacalypto":3, "Braveheart":8,"Rebecca":1,"Star":7},
"Fiona":{"Ice Storm":3, "Family Plot":10,"Rebecca":9,"Star":6},
}

def minkowkisD(rating1,rating2,r):
    distance=0
    for item in rating1.keys():
        if item in rating2.keys():
            x=rating1[item]
            y=rating2[item]
            distance+=pow(abs(x-y),r)
            return pow(distance,1/r)
        
#let
userX="Amy"
userXRatings=UserMovieRating[userX]
userY="Bill"
userYRatings=UserMovieRating[userY]
manXY=minkowkisD(userXRatings,userYRatings, 1)
print(userX,userY, manXY)
#r=1 because we want the manhattan distance
lst=[]
for userY, userYRatings in UserMovieRating.items():
    manXY=minkowkisD(userXRatings,userYRatings, 1)
    print(userX,userY, manXY)
from operator import itemgetter    
lst=[]
for userY, userYRatings in UserMovieRating.items():
    manXY=minkowkisD(userXRatings,userYRatings, 1)
    tup=(userY,manXY)
    lst.append(tup)
    print(lst)
sortedlst=sorted(lst,key=itemgetter(1))
print(sortedlst)
    




