f1 = open('data/ratings.csv').read().splitlines()
f1 = [r.split(',') for r in f1]
f2 = open('data/movies.csv').read().splitlines()
f2 = [a[:a.index(',')] + '\t' + a[a.index(',') + 1:a.rindex(',')] + '\t' + a[a.rindex(',') + 1:] for a in f2]
f2 = [r.split('\t') for r in f2]
f3 = open('data/tag_relevance.dat').read().splitlines()
f3 = [r.split('\t') for r in f3]

################################################################################################

movie1 = list(set([m[1] for m in f1]))
movies_genre = {r[0]: r[2] for r in f2}
movie2 = list(movies_genre.keys())
movie1 = set(movie2).intersection(movie1)
movie2 = [r[0] for r in f3]
movie = list(movie1.intersection(movie2))
genres = set()
for r in f2:
    genres.update(r[2].split('|'))
genres = list(genres)
movies_genre = []
for r in f2:
    if r[1] in movie:
        t = [0 if g not in r[2] else 1 for g in genres]

users = set()
for r in f1:
    if r[1] in movie:
        users.add(r[0])

users = list(users)
users = {x: y for x, y in zip(users, range(len(users)))}
ratings = [[0 for x in users.keys()] for y in movie]




