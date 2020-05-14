## For Users ##
user_id = input("Enter your Membership Name: ")
print("Hello! " + user_id)
print("These are the list of actors on the page")


if len(user_id) <3:
    print("Name must be at least 3 characters")

elif len(user_id) >50:
    print("Name must be a maximum of 50 characters")

else:
    print("")

names = ['Will Smith', 'Dwayne Johnson', 'Brad Pitt', 'Scarlett Johansson']
for name in names:
    print(name)


def test():
    name = input('Enter name of the actor:')

    if(name== 'Will Smith') or (name== "will smith"):

        print ("Spies in Disguise")
        print("I am Legend")
        print("Gemini Man")

    elif(name== 'Dwayne Johnson') or (name== 'dwayne johnson'):
        print("Hobbs & Shaw")
        print("Jumanji The Next Level")
        print("Skyscraper")

    elif(name== "Brad Pitt") or (name== 'brad pitt'):
        print("Once Upon a Time in Hollywood")
        print("World War Z")
        print("Inglourious Basterds")

    elif(name== "Scarlett Johansson") or (name== "scarlett johansson"):
        print("Black Widow")
        print("Jojo Rabbit")
        print("Avengers: Endgame")

    else:
        print("movie unavailable")

test()

def test():
    name = input('Enter Movie from List:')

    if(name == 'I am Legend') or (name== 'I am legend'):
        print("I am Legend is a Movie about: ")
        print("Set in New York City after a virus,\nwhich was originally created to cure cancer,\nhas wiped out most of mankind, leaving Neville\nas the last human in New York,\nother than nocturnal mutants.\nNeville is immune to the virus and he works\nto develop a cure\nwhile defending himself against the hostile mutants.")
        print("post-apocalyptic thriller film")
        print("This Movie has a 3.5 out of 5 stars")


    elif(name == 'Gemini Man') or (name== 'gemini man'):
        print("Gemini Man is a Movie about:")
        print("An over-the-hill hitman faces off\nagainst a younger clone of himself.\nA retiring assassin, Henry Brogan, finds himself\npursued by a mysterious killer\nthat can predict his every move.\nDiscovering that he's being hunted\nby a younger clone of himself,\nHenry needs to find out why he's being targeted\nand who the creator is.")
        print("American action thriller film")
        print ("This Movie has 3 out of 5 stars")


    elif(name == 'Spies in Disguise') or (name== 'spies in disguise'):
        print("Spies in Disguise is a Movie about")
        print("When the world's best spy is turned into a pigeon,\nhe must rely on his nerdy tech officer to save the world.\nSuper spy Lance Sterling and scientist Walter Beckett\nare almost exact opposites.\nLance is smooth, suave and debonair.\nWalter is not.")
        print("Computer-Animated Spy Comedy Film")
        print("This Movie has a 4.0 out of 5 stars")

    elif(name == 'Hobbs & Shaw') or (name== 'hobbs & shaw') or (name== 'Hobbs and Shaw') or (name== 'hobbs and shaw'):
        print("Hobbs and Shaw is a Movie about: ")
        print("Brixton Lorr is a cybernetically enhanced soldier\nwho possesses superhuman strength,\na brilliant mind and a lethal pathogen\nthat could wipe out half of the world's population.\nIt's now up to hulking lawman Luke Hobbs and lawless\noperative Deckard Shaw to put aside their past differences\nand work together to prevent the seemingly\nindestructible Lorr from destroying humanity.")
        print("Action Film")
        print("This Movie has a 3.5 out of 5 stars")

    elif(name== 'Jumanji The Next Level') or (name== 'jumanji the next level'):
        print("Jumanji The Next Level is a Movie about: ")
        print("When Spencer goes back into the fantastical world of Jumanji,\npals Martha, Fridge and Bethany re-enter the game to bring him home.\nBut the game is now broken -- and fighting back.\nEverything the friends know about Jumanji is about to change,\nas they soon discover there's more obstacles and more danger to overcome.")
        print("Fantasy Adventure Comedy Film")
        print("This Movie has a 4 out of 5 stars")

    elif(name== 'Skyscraper') or (name== 'skyscraper'):
        print("Skyscraper is a Movie about: ")
        print("Will Sawyer is a former FBI agent and U.S. war veteran\nwho now assesses security for skyscrapers.\nWhile he's on assignment in China, the world's\ntallest and safest building catches on fire -- and Will gets\nframed for it. Now a wanted man and on the run,\nhe must find those responsible, clear his\nname and somehow rescue his\nfamily members when they become trapped inside the inferno.")
        print("Action Film")
        print("This Movie has a 2 out of 5 stars")

    elif(name== 'Once Upon a Time in Hollywood') or (name== 'once upon a time in hollywood'):
        print("Once Upon a Time in Hollywood is a Movie about: ")
        print("Actor Rick Dalton gained fame and fortune by starring in a 1950s television Western,\nbut is now struggling to find meaningful work in a Hollywood\nthat he doesn't recognize anymore. He spends most of his time drinking\nand palling around with Cliff Booth, his easygoing best friend\nand longtime stunt double. Rick also happens to live next door\nto Roman Polanski and Sharon Tate -- the filmmaker and budding actress\nwhose futures will forever be altered by members\nof the Manson Family.")
        print("Comedy Drama")
        print("This Movie has a 5 out of 5 stars")

    elif (name == 'World War Z') or (name == 'world war z'):
        print("World War Z is a Movie about: ")
        print("When former U.N. investigator Gerry Lane (Brad Pitt)\nand his family get stuck in urban gridlock,\nhe senses that it's no ordinary traffic jam.\nHis suspicions are confirmed when, suddenly,\nthe city erupts into chaos. A lethal virus, spread\nthrough a single bite, is turning healthy people\ninto something vicious, unthinking and feral. As the pandemic threatens\nto consume humanity, Gerry leads a worldwide search to find the source of the infection\nand, with luck, a way to halt its spread.")
        print("Apocalyptic Action Horror Film")
        print("This Movie has a 4.5 out of 5 stars")

    elif (name == '	Inglourious Basterds') or (name == 'inglourious basterds'):
        print("	Inglourious Basterds is a Movie about: ")
        print("It is the first year of Germany's occupation of France.\nAllied officer Lt. Aldo Raine (Brad Pitt) assembles a team of\nJewish soldiers to commit violent acts of retribution against\nthe Nazis, including the taking of their scalps.\nHe and his men join forces with Bridget von Hammersmark,\na German actress and undercover agent, to bring down\nthe leaders of the Third Reich. Their fates converge with\ntheater owner Shosanna Dreyfus, who seeks to avenge\nthe Nazis' execution of her family.")
        print("War Film")
        print("This Movie has a 4.5 out of 5 stars")

    elif(name== 'Black Widow') or (name== 'black widow'):
        print("Black Widow is a Movie about: ")
        print("At birth the Black Widow (aka Natasha Romanova)\nis given to the KGB, which grooms\nher to become its ultimate operative.\nWhen the U.S.S.R. breaks up, the government tries to kill her\nas the action moves to present-day New York,\nwhere she is a freelance operative.")
        print("Action Adventure Film")
        print("This Movie has not been rated yet")

    elif (name == '	Jojo Rabbit') or (name == 'jojo rabbit'):
        print("Jojo Rabbit is a Movie about: ")
        print("Jojo is a lonely German boy who discovers that his single mother\nis hiding a Jewish girl in their attic. Aided only by\nhis imaginary friend -- Adolf Hitler -- Jojo must confront\nhis blind nationalism as World War II\ncontinues to rage on.")
        print("Comedy War")
        print("This Movie has a 5 out of 5 stars")

    elif (name == '	Avengers: Endgame') or (name == 'avengers: endgame'):
        print("Avengers: Endgame is a Movie about: ")
        print("Adrift in space with no food or water,\nTony Stark sends a message to Pepper Potts\nas his oxygen supply starts to dwindle.\nMeanwhile, the remaining Avengers -- Thor, Black Widow, Captain America\nand Bruce Banner -- must figure out a way to bring back their\nvanquished allies for an epic showdown with Thanos -- the evil demigod\nwho decimated the planet and the universe.")
        print("Action Sci - Fi")
        print("This Movie has a 5 out of 5 stars")

    else:
        ("This Movie is not available")

test()








