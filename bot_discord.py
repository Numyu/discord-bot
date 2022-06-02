import discord
import tree
from discord.ext import commands
from Node import Node
from random import randint
import random
from recipe_init import recipe_list

intents = discord.Intents().all()

client = commands.Bot(command_prefix="!", case_insensitive=True,intents=intents)

save_node = {
    # "username" : [current_node, [previous_node1, previous_node2, ...]],
}
current_node = Node
previous_node = None

quiz_answer = None

@client.event
async def on_ready():
    print("Hosu est là :D")

@client.event
async def on_member_join(member):
    welcome_channel: discord.TextChannel = client.get_channel(980116575132737618) # <-- add channel id here
    await welcome_channel.send("Bienvenue " + member.mention + " ! Tape !bot pour plus d'infos ! 🙂 ")
    

@client.command()
async def hello(ctx):
    global save_node

    username = str(ctx.author)
    current_node = tree.root
    if username not in save_node:
        # crée un nouveau élément dans le dictionnaire
        save_node[username] = [current_node, []]
    await ctx.send(save_node[username][0].question)


@client.event
async def on_message(message):   

    global current_node
    global previous_node
    global save_node
    global quiz_answer

    member = str(message.author)
    
    if member == client.user:
        return
    else:

        if message.content == quiz_answer:
            message.content = message.content.lower()
            quiz_answer = None
            await message.channel.send("Bravo " + message.author.mention + " ! Tu as répondu correctement à la question !")

        # vérifie si l'utilisateur est déja dans le dictionnaire
        if member in save_node:
            message.content = message.content.lower()
            user_sentence = message.content.split()

            for word in user_sentence:
                if Node.node_child(save_node[member][0], word) != None:
                    previous_node = save_node[member][0]
                    current_node = Node.node_child(save_node[member][0], word)

                    save_node[member][0] = current_node
                    save_node[member][1].append(previous_node)

                    if type(save_node[member][0].question) == str:
                        await message.channel.send(save_node[member][0].question)
                    elif not type(save_node[member][0].question) == str:
                        await message.channel.send(embed = save_node[member][0].question)

                elif word == "reset":
                    current_node = tree.root

                    save_node[member] = [current_node, []]

                    await message.channel.send(save_node[member][0].question)  

                elif word == "bye":
                    current_node = Node
                    previous_node = None

                    save_node.pop(member)

                    await message.channel.send("A bientôt " + member + " !")

                    return

                elif word == "merci":
                    current_node = Node
                    previous_node = None

                    save_node.pop(member)

                    await message.channel.send("Ce fut un plaisir de t'aider " + member + " !")

                    return

                elif word == "retour":

                    current_node = save_node[member][1][-1]

                    save_node[member][0] = current_node

                    if type(save_node[member][0].question) == str:
                        await message.channel.send(save_node[member][0].question)
                    elif not type(current_node.question) == str:
                        await message.channel.send(embed = save_node[member][0].question)

                    if len(save_node[member][1]) > 1 and current_node == save_node[member][1][-1]:
                        save_node[member][1].pop()
            

        await client.process_commands(message)


@client.command()
async def bot(ctx):
    embed = discord.Embed(
        title="Hello Food 🍕🍔🍣", 
        description="Ce bot fonctionne avec une conversation, il suffit juste de répondre aux questions !", 
        color=0xcdb4db
    )
    embed.add_field(name="Commandes générales", value="!modo = appeler un modérateur\n!food = plat aléatoire (channel **hello food**)\n !hello = appeler le bot  (channel **hello food**)\n !quiz = lance un quiz (channel **quiz**)", inline=False)
    embed.add_field(name="Commandes conversation", value="bye / merci = quitter la conversation\n retour = revenir en arrière\n reset = recommencer la conversation", inline=False)
    embed.set_footer(text="Enjoy 😃 !")

    await ctx.send(embed = embed)


@client.command()
async def modo(ctx):

    modo_list = []
    for member in client.get_all_members():
        if member.status != discord.Status.offline:
            for role in member.roles:
                if role.name == "modo":
                    modo_list.append(member)
                    
 
    if len(modo_list) == 0:
        await ctx.channel.send("Aucun modo n'est connecté ! Tape '!bot' pour plus d'infos")
    else:
        random_number = randint(0, len(modo_list)-1)
        await ctx.channel.send(modo_list[random_number].mention + " est connecté.e ! Envoies lui ta question en privé :)")


@client.command()
async def clear(ctx):
    await ctx.channel.purge(limit=100)

@client.command()
async def food(ctx):

    # Choix aléatoire d'un plat pour toi
    random_key = random.choice(list(recipe_list.keys()))

    # Position dans le dictionnaire du plat séléctionné(string)
    position_index = list(recipe_list).index(random_key)

    # Sous-titre de la description
    subtilte = list(recipe_list.values())[position_index][0]
    # Poème
    poeme_section = list(recipe_list.values())[position_index][1]
    # Lien web
    web_site_link = list(recipe_list.values())[position_index][2]
    # color de Embed
    color_used = list(recipe_list.values())[position_index][3]

    # Déclaration du Embed
    embed = discord.Embed(title='**Tu mangeras ' + random_key + ' à ton prochain repas **',
                          url=web_site_link, description=subtilte + '\n \n' + poeme_section, color=color_used)

    # Envoi du Embed à l'utilisateur
    await ctx.send(embed=embed)

@client.command()
async def quiz(ctx):
    global quiz_answer
    
    quiz = {
        "Le Samgyetang est un plat :" : ["coréen", ["japonais", "thaïlandais", "coréen"]],
        "Parmi les plats suivants, lequel est un plat français ?" : ["quiche lorraine", ["quiche lorraine", "paella", "pizza"]],
        "Le Kare-kare est un plat : " : ["philippin", ["grec", "philippin", "norvégien"]],
        "Comment s'orthographie cette spécialité grecque ?" : ["tzatziki", ["taztziki", "tzatziki", "tsatsiki"]],
        "La guacamole est une spécialité à base de ..." : ["avocat", ["courgette", "avocat", "concombre"]],
        "De quel pays nous viennent les tapas ?" : ["espagne", ["portugal", "italie", "espagne"]],
        "Où mange-t-on des Wienerschnitzel ?" : ["autriche", ["allemagne", "autriche", "suisse"]],
    }
    
    random_question = random.choice(list(quiz.keys()))
    quiz_answer = quiz[random_question][0]
    random_order_choice = []

    i = 0
    while i < 3:
        quiz_choice = random.choice(quiz[random_question][1])
        random_order_choice.append(quiz_choice)
        quiz[random_question][1].remove(quiz_choice)
        i += 1  

    embed = discord.Embed(
        title=random_question, 
        description="- " + random_order_choice[0] + "\n" + "- " +random_order_choice[1] + "\n" + "- " + random_order_choice[2],
        color=0xe9c46a
    )

    await ctx.send(embed = embed) 


client.run("add your token here")
