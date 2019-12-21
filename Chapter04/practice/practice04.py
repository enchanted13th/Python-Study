class OopsException(Exception) :
    pass

try :
    raise OopsException('Caught an oops')
except OopsException as exc :
    print(exc)

titles = [ 'Creature of Habit', 'Crewel Fate' ]
plots = [ 'A nun turns into a monster', 'A haunted yarn shop' ]
movies = dict(zip(titles, plots))

print(movies)