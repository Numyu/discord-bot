import discord

japonais = discord.Embed(
    title = "Kodawari Ramen (Tsukiji)" ,
    description = "Restaurant authentique pour déguster les meilleurs ramen de Paris\nTu peux voir la carte en cliquant sur le titre ! :)" ,
    color = discord.Color.purple() ,
    url="https://www.kodawari-ramen.com/kodawari-tsukiji-la-carte/"
)
lieu_jap = "12 rue de Richelieu, 75001 Paris France"
japonais.set_image(url="https://www.kodawari-ramen.com/wp-content/uploads/2019/06/kodawari-tsukiji-homepage.jpg")
japonais.add_field(name="Lieu", value=lieu_jap, inline=True)

francais = discord.Embed(
    title = "Au coin" ,
    description = "De la bistronomie française qui séduira tout le monde\nTu peux voir la carte en cliquant sur le titre ! :)" ,
    color = discord.Color.purple() ,
    url="https://www.aucoin-ermont.fr/menus-carte/"
)
lieu_fr = "129 rue du Général de Gaulle 95120 Ermont"
francais.set_image(url="https://www.aucoin-ermont.fr/i/au-coin-bistrot-bar-chic-ermont-384692/3/4/9/2/6/0/1/5/0/3/5/6/9/1515425988_166/fdb6d52f8d9ff51066b2cecf48f8ebb8.jpg")
francais.add_field(name="Lieu", value=lieu_fr, inline=True)

coreen = discord.Embed(
    title = "Sam Chic" ,
    description = "Les barbecues coréens sont exquis ! Le restaurant est assez grand pour venir en groupe également.\nTu peux voir la carte en cliquant sur le titre ! :)" ,
    color = discord.Color.purple() ,
    url="https://samchic.fr/notre-menu/"
)
lieu_kr = "11 Rue Rameau, 75002 Paris"
coreen.set_image(url="https://res.cloudinary.com/tf-lab/image/upload/f_auto,q_auto,w_800,c_limit/customer/7dbb59e7-5ef4-4cc9-8836-647f22e6769c/b36475b9-2102-42d8-878a-30f0613039e1.jpg")
coreen.add_field(name="Lieu", value=lieu_kr, inline=True)

africain = discord.Embed(
    title = "Mama Jackson" ,
    description = "De la soul foud, spécialités du sud des Etats-Unis, où vous pourrez manger par exemple des gaufres au poulet frit. L'atmosphère est très décontractée !\nTu peux voir la carte en cliquant sur le titre ! :)" ,
    color = discord.Color.purple() ,
    url="https://www.facebook.com/mamajacksonsoulfood/?ref=settings"
)
lieu_af = "12 Rue Claude Tillier, 75012 Paris"
africain.set_image(url="https://media-cdn.tripadvisor.com/media/photo-s/1d/70/2c/89/caption.jpg")
africain.add_field(name="Lieu", value=lieu_af, inline=True)