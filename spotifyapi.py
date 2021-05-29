# https://api.spotify.com/v1/search?q=
# artist name + track title with %20 for spaces
# &type=artist%2Ctrack
# reset the auth code each time you run this, it expires
# link here: https://developer.spotify.com/console/get-search-item/?q=Justin%20Bieber&type=artist&market=US&limit=10&offset=5&include_external=







curl -X "GET" 
    "https://api.spotify.com/v1/search?q='H.E.R.%20Slide'&type=artist,track" 
    -H "Accept: application/json" 
    -H "Content-Type: application/json" 
    -H "Authorization: Bearer BQC8x8ymN9MuhnJi55BcpYnBTSUFfgx3S0ppNrpYSBKhNGT2hUroOlcP13g8mHPxKmM66AnzRanGFumuIq0Hiv3gavP8FxPZfLGeZXGPb3a_CSupHeF1kINYgsBS8wYsvCODq-yelbGZ9irjO4aY0yp-s_tBR6OdyHmNGgbjQb47twMklvIg1CfbQyK72Lq19Gg"