/*
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
*/
// 60ms. 94th percentile.
const longToShort = {};
const shortToLong = {};
const keyLength = 6;
/**
 * Encodes a URL to a shortened URL.
 *
 * @param {string} longUrl
 * @return {string}
 */
var encode = function(longUrl) {
    let alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123457890";
    let key = [];
    while (key.length < keyLength || key in shortToLong) {
        for (let i = 0; i < keyLength; i++) {
            key.push(alphabet[Math.floor(Math.random()*alphabet.length)]);
        }
        key = key.join("");
    }
    shortToLong[key] = longUrl;
    longToShort[longUrl] = key;
    return "http://tinyurl.com/" + key;
};

/**
 * Decodes a shortened URL to its original URL.
 *
 * @param {string} shortUrl
 * @return {string}
 */
var decode = function(shortUrl) {
    let key = shortUrl.slice(shortUrl.length-keyLength, shortUrl.length);
    if (key in shortToLong) {
        return shortToLong[key];
    } else {
        return "";
    }
};

/**
 * Your functions will be called as such:
 * decode(encode(url));
 */

 /*
 Notes:
Autoincrementing ints isn't the best idea. Obvious issue is that you might not want people to know how many urls you've made...
also really easy for someone to spam the tiny urls...bad to have keys of arbitary length...list goes on...
*/