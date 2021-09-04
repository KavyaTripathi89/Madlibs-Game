def ask_user():
    while True:
        try:
            choice=int(input("Choose a story: 1\n story 1 \n story 2 \n story 3 \n "))
        except ValueError:
            print("This is not a number. Enter a number")
        if 0<choice<4:
            break
        else:
            print("This number does not lie between 1 and 3. Enter a valid number. ")
    print ("\n You entered {}: ".format(choice))

    def story1(): 
        animals= input('enter a animal name : ')
        profession = input('enter a profession name: ')
        cloth = input('enter a piece of cloth name: ')
        things = input('enter a thing name: ')
        name= input('enter a name: ')
        place = input('enter a place name: ')
        verb = input('enter a verb in ing form: ')
        food = input('food name: ')
        print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' 
        + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as '
         + animals + ' pretending to be a ' + profession +
          '. when we saw the second photo, it was exactly what I wanted. We both looked like '
          + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')
    
    def story2():
        adjective = input('enter adjective : ')
        color = input('enter a color name : ')
        thing = input('enter a thing name :')
        place = input('enter a place name : ')
        person= input('enter a person name : ')
        adjactive1 = input('enter a adjective : ')
        insect= input('enter a insect name : ')
        food = input('enter a food name : ')
        verb = input('enter a verb name : ')
        print('Last night I dreamed I was a ' +adjective+ 
    ' butterfly with ' + color+ 
    ' splocthes that looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '
    +person+ ' who was a '+adjactive1+ ' ' +insect +' .We ate some ' +food+
    ' when we got there and then decided to '+verb+ ' and the dream ended when I said-- lets ' +verb+ '.')


    def story3():
        person = input('enter person name: ')
        color = input('enter color : ')
        foods = input('enter food name : ')
        adjective = input('enter an adjective name: ')
        thing = input('enter a thing name : ')
        place = input('enter place : ')
        verb = input('enter verb : ')
        adverb = input('enter adverb : ')
        food = input('enter food name: ')
        things = input('enter a thing name : ')
    
        print('Today we picked apple from '+person+
         "'s Orchard. I had no idea there were so many different varieties of apples. I ate "
          +color+ ' apples straight off the tree that tasted like '+foods+ 
          '. Then there was a '+adjective+ ' apple that looked like a ' + thing + 
          '.When our bag were full, we went on a free hay ride to '+place+ 
          ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ 
          '. I can hardly wait to get home and cook with the apples. We are going to make apple '
          +food+ ' and '+things+' pies!.')



    mydict = {1:story1 ,2:story2, 3:story3}
    mydict[choice]()        


ask_user()
while input("\n Do you want to replay 'yes' or 'no': ").lower()=='yes':
    ask_user()

    
