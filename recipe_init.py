import discord

cuisine_choice = discord.Embed(
        title = "Quelle cuisine te donne envie ?" ,
        description = "- Japonais\n- Fast food" ,
        color = discord.Color.purple()
    )

restaurant_choice = discord.Embed(
        title = "Quelle cuisine te donne envie ?" ,
        description = "- Japonais\n- Coréen\n- Français\n- Africain" ,
        color = discord.Color.purple()
    )

recipe_list = {
    'Burger': ['Voici une petite citation pour te donner encore plus envie !',
               "*Faut faire attention à ce que l'on mange* \n *Mais  ne nous priverons pas d'un cheeseburger,* \n *Parce que ce n'est franchement pas drôle de vivre de fruits et de salades.*",
               'https://avec-amour-burger.com/',
               0x11806a],
    'Sushi': ['Voici un petit poème pour te donner encore plus envie !',
              "*Mon bel amour, mon sushi * \n *Belle perle du Japon* \n *Ton rouge point de saumon* \n *S'accorde parfaitement* \n *Avec ton délicieux riz.*",
              'http://sushiseivincennes.blogspot.com/',
              0xe91e63],

    'Un Plat Fait Maison': ['Voici une petite citation pour te donner encore plus    envie !',
            "*Cuisiner.* \n *C'est l'art le plus beau et le plus complet.* \n *Il engage nos cinq sens, plus un - le besoin de donner le meilleur de nous-mêmes*",
            'https://www.marmiton.org/recettes/top-internautes-plat-principal.aspx',
            0x95a5a6]
}