/*
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
*/


// 3ms. 62nd percentile.
// more about design than speed...
public class Codec {
    Map<String, String> longToShort = new HashMap<String, String>();
    Map<String, String> shortToLong = new HashMap<String, String>();
    String alphabet = "abcdefghjijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
    int keyLength = 6;
    
    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        StringBuilder sb = new StringBuilder();
        while (sb.length() < keyLength || shortToLong.containsKey(sb.toString())) {
            sb = new StringBuilder();
            for (int i = 0; i < keyLength; i++) {
                sb.append( alphabet.charAt( (int) Math.floor(Math.random()*alphabet.length()) ) );
            }
        }
        String key = sb.toString();
        longToShort.put(longUrl, key);
        shortToLong.put(key, longUrl);
        return "htpp://tinyurl.com/" + key;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        String key = shortUrl.substring(shortUrl.length()-keyLength, shortUrl.length());
        if (shortToLong.containsKey(key)) {
            return shortToLong.get(key);
        } else {
            return "";
        }
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));



 /*
 Notes:
Autoincrementing ints isn't the best idea. Obvious issue is that you might not want people to know how many urls you've made...
also really easy for someone to spam the tiny urls...bad to have keys of arbitary length...list goes on...
*/