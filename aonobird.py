import time 
import tweepy # Library that provides us with access to the api of twitter

class App:

	""" This application will consume the twitter 
			api and allows us to extract information from users, 
			their profiles and tweets.
	"""
	def __init__(self,  consumer_key="", 
											consumer_secret="",
											access_token="",
											access_token_secret=""):
		
		# Consumer API keys
		self.__key = consumer_key
		self.__sectet_key = consumer_secret

		# Access token & access token secret
		self.__token = access_token 
		self.__token_secrect = access_token_secret

		# Authenticate to Twitter
		self.__auth = tweepy.OAuthHandler(self.__key, self.__sectet_key)
		self.__auth.set_access_token(self.__token, self.__token_secrect)

		# Create API object
		self.api = tweepy.API(self.__auth)

		self.user = self.api.get_user('twitter')

	def test(self):

		"""	We do a small test and verify that everything 
				functions correctly with our api
		"""
		
		print("Tweet done!")

		# Create a tweet
		tweet = self.api.update_status("Hi Ray, That tweet was made with Tweepy, apparently there is no mistake, fine! I will destroy myself in 10 seconds.")

		# Deley to delete the tweet
		time.sleep(20)

		# Delete a tweet
		self.api.destroy_status(tweet.id_str)

		print("Tweet deleted!")

	def user_info(self):

		"""Show user information
		"""
		print("Name:",self.user.screen_name)
		print("Number of followers:", self.user.followers_count)
		print("Number of followed:",len(self.user.friends()))

if __name__ == "__main__":
	bot = App()
	bot.test()
	bot.user_info()
