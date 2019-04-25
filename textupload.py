from flask import Flask, render_template, request
import collections
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('f.html')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('uploaded_file.txt')
        # f = open("uploaded_file.txt", "r")
        # s = f.read()

        # Read input file, note the encoding is specified here 
        # It may be different in your text file
        file = open('uploaded_file.txt', 'r')
        a = file.read()
        # Stopwords
        stopwords = set(line.strip() for line in open('stopwords.txt'))
        # print(stopwords)
        # stopwords = stopwords.union(set(['mr','mrs','one','two','said']))

        # Instantiate a dictionary, and for every word in the file, 
        # Add to the dictionary if it doesn't exist. If it does, increase the count.
        wordcount = {}
        # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
        for word in a.lower().split():
            word = word.replace(".","")
            word = word.replace(",","")
            word = word.replace(":","")
            word = word.replace("\"","")
            word = word.replace("!","")
            word = word.replace("â€œ","")
            word = word.replace("â€˜","")
            word = word.replace("*","")
            if word not in stopwords:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
        # Print most common word
        n_print = 10
        # n_print = int(input("How many most common words to print: "))
        # print("\nOK. The {} most common words are as follows\n".format(n_print))
        word_counter = collections.Counter(wordcount)
        mystring = 'top ' + str(n_print) + ' words: '
        for word, count in word_counter.most_common(n_print):
            # print(word, ": ", count)
            mystring+=' '+ word + ' – ' + str(count) + ';'
            # print(mystring)
        cleanedstring = mystring[14:]
        separatedstrings = cleanedstring.split('; ')
        for item in separatedstrings:
            print(item)
        # Close the file
        file.close()

        

        # print('your document length is',len(s),'words' )

        return render_template('e.html', separatedstrings=separatedstrings, count=n_print)
        # return mystring


