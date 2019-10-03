"""
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and 
it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode 
algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be 
decoded to the original URL.
"""

# 16ms. 90th percentile.
class Codec:

    def __init__(self):
        self.alphabet = list(string.ascii_lowercase + "0123456789")
        self.longToShort = collections.defaultdict(str)
        self.shortToLong = collections.defaultdict(str)
        self.shortLength = 6
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        key = []
        while len(key) < self.shortLength or key in self.shortToLong:
            key = []
            for i in range(self.shortLength):
                key.append(random.choice(self.alphabet))
            key = ''.join(key)
        
        self.shortToLong[key] = longUrl
        self.longToShort[longUrl] = key
        
        return "http://tinyurl.com/{}".format(key)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl[-6:]
        return self.shortToLong[key]

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


"""
Notes:
Autoincrementing ints isn't the best idea. Obvious issue is that you might not want people to know how many urls you've made...
also really easy for someone to spam the tiny urls...bad to have keys of arbitary length...list goes on...
"""