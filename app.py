#we're going to make our first flask app using python
from flask import Flask
from flask import send_file
from flask import render_template_string
##create an instance of flask class
#creates an objec we can use
#__name__ determines root path of application 
#route path is main directory of application or default route
app = Flask(__name__)
##now create route that will be main page of app
##route is url that application will respond to our client browser request
#use route decorator to create a route
@app.route('/')
def index():
    #whatever we return will be returned on browser
    return "<h2>The Mysterious Bookstore</h2> <br> <p>Welcome to the Mysterious bookstore. We're glad you are here. Our current selection of books includes: <br><br><br><br> The Mysterious Tree <hr> The Mysterious Forest <hr> The Mysterious Mountain <hr> The Mysterious Farm <hr> The Mysterious Lake</p>"

#now create another route that will be the about page of the app
#use route decorator to create route
@app.route('/greet/<name>')
def greet(name):
    #now return the name
    return f"<h1>Greetings {name}</h1><p>Welcome to the Mysterious bookstore. We're glad you are here.</p>"

#let's create another route to read and download short story The Mysterious Forest
@app.route('/download_mysteriousforest_ebook')
#let's do one story per file
def download_mysteriousforest_ebook():
    #create path to file
    file_path = "mysteriousforestebook.txt"
    #now send file to client browser for download
    return send_file(file_path, as_attachment=True)

#now users need to be able to see download link
#create route to display download link
@app.route('/read_mysteriousforest')
def read_mysteriousforest():
    html_content = """
    <h1>Download the story Mysterious Forest</h1>
    <p>Click link below to download</p>
    <a href="/download_mysteriousforest_ebook">Download the story The Mysterious Forest</a>
    """
    #now send html template to client browser
    return render_template_string(html_content)

#let's create another route to read and download short story The Mysterious Forest
@app.route('/download_mysteriousforest_audiobook')
#let's do one story per file
def download_mysteriousforest_audiobook():
    #create path to file
    file_path = "mysterious_forest_ebook.mp3"
    #now send file to client browser for download
    return send_file(file_path, as_attachment=True)

#now users need to be able to see download link
#create route to display download link
@app.route('/listen_mysteriousforest')
def listen_mysteriousforest():
    html_content = """
    <h1>Download the story The Mysterious Forest audiobook.</h1>
    <p>Click link below to download</p>
    <a href="/download_mysteriousforest_audiobook">Download the audio version of the story The Mysterious Forest.</a>
    """
    #now send html template to client browser
    return render_template_string(html_content)

#let's create another route to read and download short story The Mysterious Tree
@app.route('/download_mysterioustree')
#let's do one story per file
def download_mysterioustree():
    #create path to file
    file_path = "mysterioustreeebook.txt"
    #now send file to client browser for download
    return send_file(file_path, as_attachment=True)

#now users need to be able to see download link
#create route to display download link
@app.route('/read_mysterioustree')
def read_mysterioustree():
    html_content = """
    <h1>Download the story Mysterious Tree</h1>
    <p>Click link below to download</p>
    <a href="/download_mysterioustree">Download the story The Mysterious Tree</a>
    """
    #now send html template to client browser
    return render_template_string(html_content)

#let's create another route to read and download short story The Mysterious Farm
@app.route('/download_mysteriousfarm')
#let's do one story per file
def download_mysteriousfarm():
    #create path to file
    file_path = "mysteriousfarmebook.txt"
    #now send file to client browser for download
    return send_file(file_path, as_attachment=True)

#now users need to be able to see download link
#create route to display download link
@app.route('/read_mysteriousfarm')
def read_mysteriousfarm():
    html_content = """
    <h1>Download the story Mysterious Farm</h1>
    <p>Click link below to download</p>
    <a href="/download_mysteriousfarm">Download the story The Mysterious Farm</a>
    """
    #now send html template to client browser
    return render_template_string(html_content)


#let's create another route to read and download short story The Mysterious Lake
@app.route('/download_mysteriouslake')
#let's do one story per file
def download_mysteriouslake():
    #create path to file
    file_path = "mysteriouslakeebook.txt"
    #now send file to client browser for download
    return send_file(file_path, as_attachment=True)

#now users need to be able to see download link
#create route to display download link
@app.route('/read_mysteriouslake')
def read_mysteriouslake():
    html_content = """
    <h1>Download the story Mysterious Lake</h1>
    <p>Click link below to download</p>
    <a href="/download_mysteriouslake">Download the story The Mysterious Lake</a>
    """
    #now send html template to client browser
    return render_template_string(html_content)


#let's create another route to read and download short story The Mysterious Lake
@app.route('/download_mysteriousmountain')
#let's do one story per file
def download_mysteriousmountain():
    #create path to file
    file_path = "mysteriousmountainebook.txt"
    #now send file to client browser for download
    return send_file(file_path, as_attachment=True)

#now users need to be able to see download link
#create route to display download link
@app.route('/read_mysteriousmountain')
def read_mysteriousmountain():
    html_content = """
    <h1>Download the story Mysterious mountain</h1>
    <p>Click link below to download</p>
    <a href="/download_mysteriousmountain">Download the story The Mysterious Mountain</a>
    """
    #now send html template to client browser
    return render_template_string(html_content)

#start application
#entry point of application for python
if __name__ == "__main__":
    #now start flask application server
    #listen for incoming request from client browser
    #if there are no errors this will keep running until we stop it
    app.run()