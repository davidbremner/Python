
# films dictionary: first value is required age, second is tickets left.

films = {
    "Top Gun": [15, 2],
    "Jurassic World": [12, 1],
    "Doctor Strange": [12, 2],
    "Boss Baby": [3, 1]
}

tickets_left = 0
movie_list = ""

for key, value in films.items():
    available_tickets = value[1]
    tickets_left = tickets_left + available_tickets
    movie_list = movie_list + key + ", "


while tickets_left > 0:
    print("Here is what we have showing:", movie_list)
    choice = input("Which film would you like to watch? ").strip().title()
    if choice in films:
        age = int(input("How old are you? ").strip())
        if age >= films[choice][0]:
            if films[choice][1] > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
                tickets_left = tickets_left - 1
                print("Tickets left: " + str(films[choice][1]))
            else:
                print("Sorry there are no tickets left.")
        else:
            print("Unfortunately you are too young to view that film.")
    else:
        print("Sorry we don't have that film...")

print("The cinema is fully booked!")
