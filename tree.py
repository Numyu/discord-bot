from Node import Node
from recipe_japan import *
from recipe_init import *
from recipe_fast_food import *
from restaurant import *

root = Node("Hey je suis le bot cuisine !\nTu veux cuisiner ou manger au restaurant ?","")

    # CUISINER
root.insert_node(Node(cuisine_choice,"cuisiner"),"Hey je suis le bot cuisine !\nTu veux cuisiner ou manger au restaurant ?")

        # JAPONAIS
root.insert_node(Node("Pas de soucis :)\nQu'est-ce qui te ferait envie ? Plutôt des nouilles, du riz ou autre ?","japonais"),cuisine_choice)
            # nouilles
root.insert_node(Node("Je comprends mieux tes goûts ! Tu préfères des nouilles fines ou épaisses ? ","nouilles"),"Pas de soucis :)\nQu'est-ce qui te ferait envie ? Plutôt des nouilles, du riz ou autre ?")
                # fines
root.insert_node(Node("Des nouilles fines c'est noté ! Au sarrasin ou au blé ?","fines"),"Je comprends mieux tes goûts ! Tu préfères des nouilles fines ou épaisses ? ")
                    # sarrasin
root.insert_node(Node(soba,"sarrasin"),"Des nouilles fines c'est noté ! Au sarrasin ou au blé ?")
                    # farine de blé
root.insert_node(Node(ramen,"blé"),"Des nouilles fines c'est noté ! Au sarrasin ou au blé ?")
                # épaisses
root.insert_node(Node(udon,"épaisses"),"Je comprends mieux tes goûts ! Tu préfères des nouilles fines ou épaisses ? ") 
            # riz
root.insert_node(Node("On a donc les mêmes goûts toi et moi ! Tu aimes bien les algues ou pas vraiment ? (oui/non)","riz"),"Pas de soucis :)\nQu'est-ce qui te ferait envie ? Plutôt des nouilles, du riz ou autre ?")
                # maki
root.insert_node(Node(maki,"oui"),"On a donc les mêmes goûts toi et moi ! Tu aimes bien les algues ou pas vraiment ? (oui/non)")
                # sushi
root.insert_node(Node(sushi,"non"),"On a donc les mêmes goûts toi et moi ! Tu aimes bien les algues ou pas vraiment ? (oui/non)")       
            # autre
root.insert_node(Node("Tu as donc envie de découvrir des plats moins connus !\nLe poulpe ça te tente ? (oui/non)","autre"),"Pas de soucis :)\nQu'est-ce qui te ferait envie ? Plutôt des nouilles, du riz ou autre ?")
                # poulpe
root.insert_node(Node(takoyaki,"oui"),"Tu as donc envie de découvrir des plats moins connus !\nLe poulpe ça te tente ? (oui/non)")
                # onigiri
root.insert_node(Node(gyoza,"non"),"Tu as donc envie de découvrir des plats moins connus !\nLe poulpe ça te tente ? (oui/non)")

        # FAST FOOD
root.insert_node(Node("Les légumes c'est bon, mais j'avoue qu'un petit burger c'est quand même meilleur !\nTu veux sa recette d'ailleurs ? (oui/non)","fast"),cuisine_choice)
            # burger
root.insert_node(Node(burger,"oui"),"Les légumes c'est bon, mais j'avoue qu'un petit burger c'est quand même meilleur !\nTu veux sa recette d'ailleurs ? (oui/non)")
            # Non 
root.insert_node(Node("Hmmm, tu veux manger du poisson ou de la viande ?","non"),"Les légumes c'est bon, mais j'avoue qu'un petit burger c'est quand même meilleur !\nTu veux sa recette d'ailleurs ? (oui/non)")
            # hot-dog
root.insert_node(Node(hot_dog,"viande"),"Hmmm, tu veux manger du poisson ou de la viande ?")
            # bagels au saumon fumé
root.insert_node(Node(bagel,"poisson"),"Hmmm, tu veux manger du poisson ou de la viande ?")


    # RESTAURANT
root.insert_node(Node(restaurant_choice,"restaurant"),"Hey je suis le bot cuisine !\nTu veux cuisiner ou manger au restaurant ?")
        #japonais
root.insert_node(Node(japonais,"japonais"),restaurant_choice)
        #coréen
root.insert_node(Node(coreen,"coréen"),restaurant_choice)
        #français
root.insert_node(Node(francais,"français"),restaurant_choice)
        #africain
root.insert_node(Node(africain,"africain"),restaurant_choice)