#import class libaries for engagment with discord 
#import responses
    #run the bot 
import discord 
#importation of discord from the libary 
import os 
#writing to the file 
import random 
#creation of function to generate random
#module is being imported
from dotenv import load_dotenv 
#functions are imported from the moduel
from ec2_metadata import ec2_metadata
#importation of AWS to retrievee metadata functions 
print(ec2_metadata.region)
#printing the region 
print(ec2_metadata.instance_id)
#printing the instance ID

load_dotenv()
#from dotenv import load_dotenv 
#importation of token string

#from discord class create client object 
#OAuth2 installization with token
  
client = discord.Client() 
#function is created to connect with discord API 
token = os.getenv('TOKEN')
#function initiation
# formation of string into argument parameter 
#output creation

@client.event 
#allows responds to functions 
async def on_ready(): 
    print("Logged in as a bot {0.user}".format(client))

    #creation of an output into a string
    #objects conversiion data type,indexind and string splitting
@client.event 
async def on_message(message): 
	username = str(message.author).split("#")[0] 
	#user sends message 
	channel = str(message.channel.name) 
	#creation of a channel for the message to be sent 
	user_message = str(message.content) 
	#user sends message

#output, format(f) with brackets
	print(f'Message {user_message} by {username} on {channel}') 
	#clinet user = bot
	if message.author == client.user: 
		return
#run conditional statements to check string index
	if channel == "random": 
		if user_message.lower() == "hello" or user_message.lower() == "hi": 
			await message.channel.send(f'Hello {username}') 
			return 
		#addational string options
		#if condition is  met in lower case then the program will continue on
		elif user_message.lower() == "bye": 
		#program waits for the function to completion before moving on to next line of code
			await message.channel.send(f'Bye {username}') 
		#message from user is on lowercase
		elif user_message.lower() == "hello world": 
		#user message conditioned in lowercase
			await message.channel.send(f'Hello {username}') 
		#completion of the function is awaited before moving onto next line of code 
		elif user_message.lower() == "tell me about my server!": 
		#function compleition is awaited 
			await message.channel.send(f"""Ec2 server data \n region:{ec2_metadata.region} \n zone:{ec2_metadata.availability_zone} \n IP adress:{ec2_metadata.private_ipv4}""")
#conditional statement defined, await message.channel.send to send messages to the channel
		elif user_message.lower() == "tell me a joke": 
			jokes = [" Can someone please shed more light on how my lamp got stolen?", "Why is she called llene? She stands on equal legs.","What do you call a gazelle in a lions territory? Denzel."] 
			await message.channel.send(random.choice(jokes)) 
#run function
client.run(token)
