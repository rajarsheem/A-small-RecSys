import numpy as np
f = open('movies.csv').read().splitlines()
f = [a[:a.index(',')] + '\t' + a[a.index(',')+1:a.rindex(',')] + '\t' + a[a.rindex(',')+1:] for a in f]
movies_genre = {int(r.split('\t')[0]) : r.split('\t')[2] for r in f}
genres = []
for i in movies_genre.values(): genres.extend(i.split('|'))
genres = list(set(genres))
for i in movies_genre.keys():
    v = movies_genre[i].split('|')
    t = [0 if g not in v else 1 for g in genres]
    movies_genre[i] = t

f = open('movies.dat').readlines()
movies_popularity = {int(r.split('\t')[0]) : [r.split('\t')[1], int(r.split('\t')[2])] for r in f}

movies_popularity = {k:movies_popularity[k] for k in movies_popularity.keys() if k in movies_genre.keys()}
movies_genre = {k:movies_genre[k] for k in movies_genre.keys() if k in movies_popularity.keys()}
print(movies_popularity)

movies_tag = { k:[] for k in range(max(movies_genre.keys())+1)}

f = open('tag_relevance.dat').readlines()
for i in f:
    if int(i.split('\t')[0]) in movies_genre.keys():
        movies_tag[int(i.split('\t')[0])].append(float(i.split('\t')[2]))
        
