import sqlite3


def all(query: str):
   with sqlite3.connect('netflix.db') as con:
       con.row_factory = sqlite3.Row
       result = []

       for i in con.execute(query).fetchall():
           result.append(dict(i))
       return result

def one(querry: str):
    with sqlite3.connect('netflix.db') as con:
        con.row_factory = sqlite3.Row
        result = con.execute(querry).fetchone()

    if result is None:
        return None
    else:
        return dict(result)



def cast_with_Hofman(name_1: str='Jack Black', name_2: str='Dustin Hoffman'):
   querry = f"""
     SELECT * FROM netflix
     WHERE netflix.cast like '%Jack Black%' and netflix.cast like '%Dustin Hoffman%'
     """
   cast = []
   set_cast = set()
   result = all(querry)
   co = 0
   for i in result:
      for actor in i['cast'].split(','):
         cast.append(actor)

   for actor in cast:
      if cast.count(actor) > 2:
          set_cast.add(actor)
   return list(set_cast)




def step_6(film, year, genre):
        querry = f"""
        SELECT title, description FROM netflix
        WHERE "type" = '{film}' AND release_year = '{year}' AND
        listed_in like  '%{genre}%'
        """

        result = []
        for i in all(querry):
            result.append(
                {'title': i['title'],
                 'description' : i['description']}
            )
        return result

