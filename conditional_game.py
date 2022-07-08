# Horoscope fortune teller game
# import random
strength = ""
weaknesses = ""


# -------------------------------------------- 

	# You've just learned about variables, conditionals.
	# Just from knowing those two topics, you can do so much!
	
	# Let's try to make a simple program that responds to the user.
	# We're going to recreate the Magic 8 Ball!!!
			
			# Never heard of it? That's ok!

					# You got this!

  # -------------------------------------------- 

	# How a Magic 8 Ball Works:

	# The user asks a question and vigoriously shakes the ball. 
	# Then the ball will respond with one of twenty responses, chosen at random. 

	# That's pretty simple right?

 # -------------------------------------------- 

	# Part 1: 
	# Print instructions on the screen and 
	# prompt the user to ask a question

	

  # --------------------------------------------
# we are making a horoscope fortune teller thing

#Aquarius
AquariusStr="Progressive, original, independent, humanitarian"
AquariusWe="Runs from emotional expression, temperamental, #uncompromising, aloof"


#Pisces
PiscesStr="Compassionate, artistic, intuitive, gentle, wise, musical"
PiscesWe="Fearful, overly trusting, sad, desire to escape reality, can be a victim or a martyr"


#ARIES
AriesStr="Courageous, determined, confident, enthusiastic, optimistic, honest, passionate"
AriesWe="Impatient, moody, short-tempered, impulsive, aggressive"


#Taurus
TaurusStr="Reliable, patient, practical, devoted, responsible, stable"
TaurusWe="Stubborn, possessive, uncompromising"


#Gemini Traits
GeminiStr ="Gentle, affectionate, curious, adaptable, ability to learn quickly and exchange ideas"
GeminiWe ="Nervous, inconsistent, indecisive"


#Cancer Traits
CancerStr ="Tenacious, highly imaginative, loyal, emotional, sympathetic, persuasive"
CancerWe ="Moody, pessimistic, suspicious, manipulative, insecure"


# Leo Traits
LeoStr ="Creative, passionate, generous, warm-hearted, cheerful, humorous"
LeoWe= "Arrogant, stubborn, self-centered, lazy, inflexible"


# Virgo Traits
VirgoStr= "Loyal, analytical, kind, hardworking, practical"
VirgoWe="Shyness, worry, overly critical of self and others, all work and no play"


# Libra Traits
LibraStr= "Cooperative,diplomatic, gracious, fair-minded, social"
LibraWe= "Indecisive, avoids confrontations, will carry a grudge, self-pity"


# Scorpio Traits
ScorpioStr = "Strengths: Resourceful, powerful, brave, passionate, a true friend"
ScorpioWe = "Distrusting, jealous, manipulative, violent"


# Sagittarius Traits
SagittariusStr = "Generous, idealistic, great sense of humor"
SagittariusWe = "Promises more than can deliver, very impatient, will say anything no matter how undiplomatic"


# Capricorn Traits
CapricornStr = "Responsible, disciplined, self-control, good managers"

CapricornWe = "Know-it-all, unforgiving, condescending, expecting the worst"


print("Do you want to find out your horoscope?\nInput your birthday month:")

user_month = input()
user_month = str(user_month)
print("Now input the day of the month you were born in:")

user_day = input()
user_day = int(user_day)
# codnitionals for the horoscope signs
# Aries (March 21 – April 19)
# Taurus (April 20 – May 20)
# Gemini (May 21 – June 20)
# Cancer (June 21 – July 22)
# Leo (July 23 – August 22)
# Virgo (August 23 – September 22)
# Libra (September 23 – October 22)
# Scorpio (October 23 – November 21)
# Sagittarius (November 22 – December 21)
# Capricorn (December 22 – January 19)
# Aquarius (January 20 – February 18)
# Pisces (February 19 – March 20)
astrology_sign = ""
# determining the astrology sign

# January to June

if user_month == "January" and user_day <= 19:
  astrology_sign = "Capricorn"
  strengths = CapricornStr
  weaknesses = CapricornWe
elif user_month == "January" and user_day >= 20:
  astrology_sign = "Aquarius"
  strengths = AquariusStr
  weaknesses = AquariusWe
elif user_month == "January" and user_day >= 20:
  astrology_sign = "Aquarius"
  strengths = AquariusStr
  weaknesses = AquariusWe
elif user_month == "February" and user_day >= 19:
  astrology_sign = "Pisces"
  strengths = PiscesStr
  weaknesses = PiscesWe
elif user_month == "March" and user_day <= 20:
  astrology_sign = "Pisces"
  strengths = PiscesStr
  weaknesses = PiscesWe
elif user_month == "March" and user_day >= 21:
  astrology_sign = "Aries" 
  strengths = AriesStr
  weaknesses = AriesWe
elif user_month == "April" and user_day <= 19:
  astrology_sign = "Aries" 
  strengths = AriesStr
  weaknesses = AriesWe
elif user_month == "April" and user_day >= 20:
  astrology_sign = "Taurus"
  strengths = TaurusStr
  weaknesses = TaurusWe
elif user_month == "May" and user_day <= 20:
  astrology_sign = "Taurus"
  strengths = TaurusStr
  weaknesses = TaurusWe  
elif user_month == "May" and user_day >= 19:
  astrology_sign = "Gemini"
  strengths = GeminiStr
  weaknesses = GeminiWe
elif user_month == "June" and user_day <= 20:
  astrology_sign = "Gemini"
  strengths = GeminiStr
  weaknesses = GeminiWe
elif user_month == "June" and user_day >= 20:
  astrology_sign = "Cancer"
  strengths=CancerStr
  weaknesses=CancerWe
elif user_month == "July" and user_day <= 22:
  astrology_sign = "Cancer"
  strengths = CancerStr
  weaknesses = CancerWe
elif user_month == "July" and user_day >= 23: 
  astrology_sign = "Leo"
  strengths = LeoStr
  weaknesses = LeoWe
elif user_month == "August" and user_day <= 22: 
  astrology_sign = "Leo"
  strengths = LeoStr
  weaknesses = LeoWe
elif user_month == "August" and user_day >= 23: 
  astrology_sign = "Virgo"
  strengths = VirgoStr
  weaknesses = VirgoWe
elif user_month == "September" and user_day <= 22:
  astrology_sign = "Virgo"
  strengths = VirgoStr
  weaknesses = VirgoWe
elif user_month == "September" and user_day >= 23:
  astrology_sign = "Libra"
  strengths = LibraStr
  weaknesses = LibraWe
elif user_month == "October" and user_day <= 22:
  astrology_sign = "Libra"
  strengths = LibraStr
  weaknesses = LibraWe
elif user_month == "October" and user_day >= 23:
  astrology_sign = "Scorpio"
  strengths = ScorpioStr
  weaknesses = ScorpioWe
elif user_month == "November" and user_day <= 21:
  astrology_sign = "Scorpio"
  strengths = ScorpioStr
  weaknesses = ScorpioWe
elif user_month == "November" and user_day >= 22:
  astrology_sign = "Sagittarius"
  strengths = SagittariusStr
  weaknesses = SagittariusWe
elif user_month == "December" and user_day <= 21:
  astrology_sign = "Sagittarius"
  strengths = SagittariusStr
  weaknesses = SagittariusWe
elif user_month == "December" and user_day >= 22:
  astrology_sign = "Capricorn"
  strengths = CapricornStr
  weaknesses = CapricornWe
elif user_month == "January" and user_day <= 19:
  astrology_sign = "Capricorn"
  strengths = CapricornStr
  weaknesses = CapricornWe
else: 
  print("enter a valid birthday please :)")


print("your astrology sign is " + astrology_sign + "!!! \nRead below for your strengths and weaknesses:")
# weaknesses and strengths based on the sign 
#Aries Taurus Gemini Cancer Leo Virgo Libra Scorpio Sagittarius Capricorn Aquarius Pisces
print("Strengths: " + strengths)
print("Weaknesses: " + weaknesses)

    












# -------------------------------------------- 

	# Part 2: Next, we need to randomly select a response from 20 options.

	# Randomly select a number from 0 - 19 
	# Use that to select from the following responses:
		# 0 - It is certain.
		# 1 - It is decidedly so.
		# 2 - Without a doubt.
		# 3 - Yes - definitely.
		# 4 - You may rely on it.
		# 5 - As I see it, yes.
		# 6 - Most likely.
		# 7 - Outlook good.
		# 8 - Yes.
		# 9 - Signs point to yes.
		# 10 - Reply hazy, try again.
		# 11 - Ask again later.
		# 12 - Better not tell you now.
		# 13 - Cannot predict now.
		# 14 - Concentrate and ask again.
		# 15 - Don't count on it.
		# 16 - My reply is no.
		# 17 - My sources say no.
		# 18 - Outlook not so good.
		# 19 - Very doubtful.

	# Look up random.rand_int to see how you can use it to select a random number.

  # -------------------------------------------- 











# -------------------------------------------- 

	# Part 3: Customize it!

	# Select your own theme and use case and modify your code!
	
# -------------------------------------------- 

