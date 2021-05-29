# https://api.spotify.com/v1/search?q=
# artist name + track title with %20 for spaces
# &type=artist%2Ctrack
# reset the auth code each time you run this, it expires
# link here: https://developer.spotify.com/console/get-search-item/?q=Justin%20Bieber&type=artist&market=US&limit=10&offset=5&include_external=






curl -X "GET" 
    "https://api.spotify.com/v1/search?q=Justin%20Bieber&type=artist" 
    -H "Accept: application/json" 
    -H "Content-Type: application/json" 
    -H "Authorization: Bearer BQA4GOu9mqZv9kOT-OMYYWdReT3ijjvvrj8F-2ALmZGZWXF8mfR8Fqurwss3xCqNmqVyuI70A5obpHgRXP95N83Myh2x9eK304oLQE1EcuqMshg3QnSdmN2q8Dkx6ACnkyAfiJf2zB6GEqxZk1XqC2NTWk8WDvjVfGfXhoHsrkoKdR9VqC32p24rtA1BU1HacC8"