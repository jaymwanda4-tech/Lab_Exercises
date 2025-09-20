Favourite_Movies = {'Demon Slayer','The Forge','The Addams Family','The Gods Must Be Crazy'}

print("Current movies:", Favourite_Movies)
print("Hello, please add or remove movies from your current list")

new_movie= input("Add new movie:")
Favourite_Movies.add(new_movie)

print("Current movies:",Favourite_Movies)
remove_movie= input("Remove a movie:")
if remove_movie in Favourite_Movies:
    Favourite_Movies.remove(remove_movie)
    print("Current movies:", Favourite_Movies)
else:
    print("*Movie was not identified in the list*")

print("Sorted movies:", Favourite_Movies)
Sorted_Movies= sorted(Favourite_Movies)
print(Sorted_Movies)