#Day 23
#535. Encode and Decode TinyURL

from random import randint

class Codec:

    def __init__(self):
        #maps tiny urls to long urls
        self.urls = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        tiny = randint(100000,999999)
        #create random 6 digit encoded url
        while(tiny in self.urls):
            #while loop to avoid collisions
            tiny = randint(100000,999999)
        tiny = str(tiny)
        self.urls[tiny] = longUrl
        #return url
        return "www.tinyLeet.com/" + tiny
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        #find in dict and return
        head,tiny = shortUrl.split("/")
        if tiny in self.urls:
            return self.urls[tiny]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
