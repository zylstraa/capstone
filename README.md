# Song Writing for Dummies: <h2>How to make a hit <h5>Alexa Zylstra's Capstone project for Nashville Software School, Data Science Cohort 4</h5>



<p>Let's say you want to make the next hit song. Where should you begin? This project has got you covered on audio features, musical mood, and lyrical starting points. </p>
<h3> Datasets <h3>

<p>This project heavily relied on the work put in by <a href='https://github.com/guoguo12/billboard-charts'> Allen Guo's billboard.py library </a>, <a href='https://spotipy.readthedocs.io/en/2.18.0/#'>Paul Lamere's spotipy package</a>, <a href='https://lyricsgenius.readthedocs.io/en/master/'>John Miller's lyricsgenius package</a>, and <a href='https://radimrehurek.com/gensim/intro.html'>Radim Řehůřek, the creator of gensim</a>.</p>

<h2>Billboard Chart data</h2>

<p>Using the billboard.py library, I pulled in data for three types of songs that could be written:
<ol>
  <li>One Hit Wonders (past three months of weekly hits in 2021)</li>
  <li>Songs that Last (year end top 100 songs from 2006-2020)</li>
  <li>Global Phenomena (past three months of the top 200 global chart)</li>
</ol>

<p>This gave me the song title and artist name, which was then fed into the Spotify API to return a dataframe of audio features. (Full audio features explained <a href='https://github.com/zylstraa/capstone/wiki/Audio-Features-Objects'>in my Wiki</a>.)

I used these audio features to extrapolate three components of a song: Vibe, Composition, and Mood. **Vibe** involved looking at how much bass was in a song, if it required the ability to rap, how danceable the track was, how energetic the song is, and how fast the tempo was. Anything that wasn't already on a scale of 0-1 was scaled using scikitlearn's MinMaxScaler function so it could all fit to a radar chart. **Composition** looked at the more technical parts of the song: what key is it in, is it major or minor chords, what's the time signature, how long is the song, and the occurence of mostly acoustic or instrumental tracks. **Mood** plotted energy versus valence (the "happiness" of a song's audio) which allowed us to know if angry, happy, sad, or peaceful music was more popular in hit songs.</p>


<p> Next the song title + artist name was fed into lyricsgenius' searchsongs feature, which returned the lyrics for each song found. These lyrics were then fed into gensim's LDA model, which returned a series of topics along with the words that contributed most to those topics. Each dataset was run so that the coherence score was optimized, resulting in 2 topics for One Hit Wonders and Songs that Last, and 4 topics for Global Phenomenon. 
