# TODOs

1. **SUBMIT** the URL of this repository on eClass. 
2. List the CCID(s) of student(s) working on the project.
3. List all sources consulted while completing the assignment.

King Fu (CCID: xinjian) Scott Kavalinas (CCID:  skavalin)

# Videos

* Link to xinjian's video: https://drive.google.com/file/d/130JEUjZ34mcMLOIR4BrAv_6dF00wiUze/view?usp=drive_link
* Link to skavalin's video: https://drive.google.com/drive/folders/1n4XHfD5OLlv0xrpVhheKcYigvEI9EZnv?usp=sharing


Run the program invertedIndex.py to create inverted index: In command line, go to src folder.
type python3 invertedIndex.py [Path to json file] [Path to directory where the index will be stored</br>
The tsv files will be genreated in the src/ folder and each file is names according to its zone ID name.</br>
For example, we use data/dr_seuss_lines.json as input and the output file directory is in current directory,</br>
type "python3 invertedIndex.py ../data/dr_seuss_lines.json ./" in command line

If we use data/movie_plots.json as input and the output file directory is the current directory</br>
type "python3 invertedIndex.py ../data/movie_plots.json ./" in command line.

Run the program query.py to run the query. In Command line, go to src/ folder.</br>
python3 query.py [path to the tsv files are stored] "query"</br>
For example, if the tsv files are inthe current folder and the query is "book:Lorax AND line:Lorax"</br>
type python3 query.py ./ "book:Lorax AND line:Lorax"

Tokenization: 
we chose to use simple functions to do this,</br>
we split the corpus up for each space using split(),</br>
we removed punctuation using the string library</br>
we made all tokens lower case via lower()

Normalization:</br>
We used the NLTK lemmatizer to change certain words to a more basic form</br>
example: countries --> country

Stopwords:</br>
we chose not to modify the corpus in terms of its stop words.</br>
We believe that many stopwords such as she/ he would be potentially important when searching a reviews corpus for fermale and male movie characters

Stemming:</br>
We did not implement any form of stemming due to the risk of the process modifying strings that would not be retrived by queries
