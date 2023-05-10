import socket
import tweepy

HOST = 'localhost'
PORT = 9000

s = socket.socket()
s.bind((HOST, PORT))
print(f"Aguardando conexão na porta: {PORT}")

s.listen(5)
connection, address = s.accept()
print(f"Recebendo solicitação de {address}")

token="AAAAAAAAAAAAAAAAAAAAAIdnnQEAAAAAgDpEyN%2BqWf7fIWf2lYz4I4NjZw4%3D7gpPBwABIyGDzgkw24DL3qmESDxGgnoWxGeSU7XpbmZdWZuHbw"
keyword = "futebol"

class GetTweets(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        print("="*50)
        connection.send(tweet.text.encode('latin1', 'ignore'))

printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()


connection.close()