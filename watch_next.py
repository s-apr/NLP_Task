import spacy

#load model
nlp = spacy.load('en_core_web_md')

def get_similar_movie(description):
    #read movie descriptions
    with open('movies.txt', 'r') as file:
        content = file.readlines()

    #process input description
    input_doc = nlp(description)
    
    #list to store scores
    scores = []
    
    #iterate through lines in text
    for line in content:
        #process description from text file
        movie_doc = nlp(line)
        
        #compare text desc to input desc
        score = input_doc.similarity(movie_doc)

        #add scores & descriptions to the list
        scores.append((score, line.strip()))
    
    #sort the scores in descending order
    scores = sorted(scores, key=lambda x: x[0], reverse=True)
    
    #return scores
    return print(f"Similiarity Score: {scores[0][0]}, {scores[0][1]}")

#given film description
film_desc = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the 
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

#call function
get_similar_movie(film_desc)