''' Docfinder - A keyword searchable document database 

    Design Philosophy 
        YAGNI / defer building code as late as possible
        hardwire all things easily parameterized later
        rebuild everything on each run
        any feature that speeds development is an essential priority (__repr__)
        minimize the learning curve by using existing knowledge
        destructive operations should be expressive
        avoid generic names
        create own exceptions
                
    API design
        create_db(force=False)
        add_document(uri, document)    uri: uniform resource identifier: the name is unique, raise DuplicateURI(ValueError) if uri is duplicated
        get_document(uri) --> document return document or raise UnknowURI(KeyError)-inherited from KeyError exception if no document matches uri
        document_search(keyword,...) --> [uri0,uri1...]    return a list of URIs sorted by relevance

    User Stories
        create a database and add documents
        create_db()
        for filename in glob.glob.('pep/*.txt'):
            doc=open(filename)
            uri=filename.split('.')[0]
            add_document(uri,document)
        
        search the database for the document
        uris=document_search('fun','game')
        for uri in uris[10]
            print uri
            doc=get_document(uri)
            print ''.join(doc.splitlines()[10])
    
    Data Structure
        e.g. 
        pep 279 - URI
        raymond - keyword
        enumerate - keyword
        15/10000  - relevance requency (count of the keyword/count of the words in document)
    
        documents
        -------------
        Index by URI
        -------------
        *URI        text    (* is primary key)
        document   BLOB 
                
        characters    for indexing
        -------------
        Index by word
        -------------
        URI        TEXT    (URI is a foreign key)
        *keyword    TEXT
        relevance frequency    REAL

        (The combination of URI and keyword is unique)

'''

from __future__ import division
from contextlib import closing
import os, re, collections, sqlite3, bz2


__all__ = ['create_db', 'add_document', 'get_document', 'document_search',
           'UnknownURI', 'DuplicateURI']

database = 'pepsearch.db'

class UnknownURI(KeyError):
    'This URI is not in the database'
    pass

class DuplicateURI(ValueError):
    'A URI needs to be unique and we already have one'
    pass

stoplist=['and','or','of','the']

def normalize(words):
    '''Improve comparability by stripping plurals and lowercasing

        normalize(['Hettinger', 'Enumerates'])  -->  ['hettinger', 'enumerate']
    '''
    lower=map(str.lower, words)
    lower_chop=map(lambda x: x[:-1] if x[-1]=='s' else x, lower)
    return [word for word in lower_chop if word not in stoplist]
    
    '''
    Solution 2
    lower_chops=[]
    for word in lower:
        if word[-1]=='s':
            word=word[:-1]
        lower_chops.append(word)
    return lower_chops
    
    Solution 3
    return [word for word in lower if word[-1]!='s']+[word[:-1] for word in lower if word[-1]=='s']
    '''        

def characterize(uri, text, n=200):
    'Scan text and return relative frequencies of the n most common words'
    # return list of tuples in the form: (uri, word, relative_frequency)
    
    words=re.findall(r"[A-Za-z'-]+", text)
    norm_words=normalize(words)
    word_count=collections.Counter(norm_words).most_common(n)
    total=sum([count for word,count in word_count])
    return [(uri,word,count/total) for word,count in word_count]
   

def create_db(force=False):
    'Set-up a new characterized document database, eliminating an old one if it exists'
    #if force is true, remove the database
    if force:
        try:
            os.remove(database)
        except OSError:
            pass
    with closing(sqlite3.connect(database)) as conn:
        c=conn.cursor()
        c.execute('CREATE TABLE documents (uri text, document blob)')
        c.execute('CREATE UNIQUE INDEX uriINDEX ON documents (uri)')
        c.execute('CREATE TABLE characters (uri text, word text, relfreq real)')
        c.execute('CREATE INDEX wordINDEX ON characters (word)')
        
        
def add_document(uri, text):
    ''' Add a document with a given identifier to the search database. 
        Decouple the analysis part and the database part. i.e. add_document=characterize+database_insertion
    '''
    #characterize
    characters=characterize(uri,text)
    #database_insertion
    with closing(sqlite3.connect(database)) as conn:
        c=conn.cursor()
        btext = sqlite3.Binary(bz2.compress(text))
        try:
            c.execute('INSERT INTO documents VALUES (?,?)',(uri,btext))
        except sqlite3.IntegrityError:
            raise DuplicateURI(uri)
        c.executemany('INSERT INTO characters VALUES (?,?,?)',characters)
        conn.commit()
    

def get_document(uri):
    'Retrieve a document with a given URI.'
    with closing(sqlite3.connect(database)) as conn:
        c=conn.cursor()
        t=(uri,)
        c.execute('SELECT document FROM documents WHERE uri=?',t)
        rows=c.fetchall()
        if not rows:
            raise UnknownURI(uri)
        return bz2.decompress(rows[0][0])

search_query_template='''
SELECT uri
FROM characters
WHERE word IN (%s)
GROUP BY uri
ORDER BY SUM(relfreq) DESC
'''
def document_search(*keywords):
    'Find ranked list of best matched URIs for a given keyword'
    keywords=normalize(keywords)
    questions=', '.join(['?']*len(keywords))
    search_query=search_query_template % questions
    with closing(sqlite3.connect(database)) as conn:
        c=conn.cursor()
        c.execute(search_query,keywords)
        rows=c.fetchall()
        return [uri for uri, in rows]
    

############################################################
###  Test harness code follows  ############################

if __name__ == '__main__':
    import pprint

    docdir = 'peps'

    if 0:
        print normalize(['Hettinger', 'enumerates'])

    if 0:
        filename = 'pep-0238.txt'
        fullname = os.path.join(docdir, filename)
        with open(fullname) as f:
            text = f.read()
        uri = os.path.splitext(filename)[0]
        
        c = characterize(uri, text)
        pprint.pprint(c)

    if 1:
        create_db(force=True)

    if 1:
        #for filename in ['pep-0237.txt', 'pep-0236.txt', 'pep-0235.txt']:
        for filename in os.listdir(docdir):
            fullname = os.path.join(docdir, filename)
            with open(fullname, 'rb') as f:
                text = f.read()
            uri = os.path.splitext(filename)[0]
            #print uri, len(text)
            add_document(uri, text)

    if 0:
        print get_document('pep-0237')[:100]

    if 1:
        pprint.pprint(document_search('Guido', 'zip', 'barry')[:100])
