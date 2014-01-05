''' Demonstrate how to make a REST API using itty.
    Show the effective use of decorators to register functions to routes.

    * Welcome page
    * Time server
    * Dynamic directory display is JSON format
    * Simple text title casing and upper cases services
    * Document finder services:  search, retrieve, and upload

'''

from itty import run_itty, get, Response, NotFound, post
import time
import subprocess
import json
import os
import docfinder

@get('/')
def welcome(request):
    return 'Howdy!'

@get('/now')
def lookup_the_time(request):
    return time.ctime()

@get('/files')
def directory(request):
    result = subprocess.check_output('ls -l', shell=True)
    return Response(result, content_type='text/plain')

@get('/jfiles')
def directory_in_json_format(request):
    result = os.listdir('.')
    text = json.dumps(result, indent=4)
    return Response(text, content_type='application/json')

@get('/upper')                    # /upper?word=raymond
def upper_case(request):
    word = request.GET.get('word')
    return word.upper()

@get('/document')                 # /document?uri=pep-0287
def lookup_document(request):
    uri = request.GET.get('uri')
    try:
        result = docfinder.get_document(uri)
    except docfinder.UnknownURI:
        raise NotFound(uri)
    return Response(result, content_type='text/plain')

@get('/search')                  # /search?q=Hettinger+Enumerates
def search_through_documents(request):
    query = request.GET.get('q')
    terms = query.split()
    uris = docfinder.document_search(*terms)
    text = json.dumps(uris, indent=4)
    return Response(text, content_type='application/json')

@get('/upload')                     # /upload
def show_upload_form(request):
    'Display a web form for document uploads'
    return upload_html

@post('/upload')
def test_upload(request):
    ''' Upload a document using POST data with a multipart/form-data
        content-type according  to RFC 2388.  The fields should be
        the "uri" and the "document".

        For example:
        
            curl localhost:9600/upload -F uri=pep-9999 
                 -F document=@somefile.txt
  
    '''
    print 'Loading file: ', request.POST['document'].filename
    document = request.POST['document'].file.read()
    uri = request.POST['uri']
    try:
        docfinder.add_document(uri, document)
    except docfinder.DuplicateURI(uri):
        return Response('Failed upload. Duplicate URI: %r' % uri, status=409)
    return Response('Successfully uploaded: %r\n' % uri, status=201)


##### HTML for the load ###################################################

upload_html = '''\
<html>
<head>
    <title>Upload Document</title>
</head>
<body>
    <h2> Select a Document to Upload </h2>
    <hr>
    <form method="post" action="/upload" enctype="multipart/form-data">
        <label>URI: <input type="text" name="uri" value=""> </label><br>
        <label>File: <input type="file" name="document"> </label><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
'''

if __name__ == '__main__':
    print 'Start!'
    run_itty()

