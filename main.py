from flask import *
import os

webp = Flask(__name__)

@webp.route('/')
def index():
 return render_template('index.html', terms=None)



@webp.route('/start')
def start():
 os.system('cd servers && java -Xmx1G -jar server.jar')
 return render_template('index.html', terms="Server is ready!")


@webp.route('/stop')
def stop():
 os.system('pkill -f "java -Xmx1G -jar server.jar"')
 return render_template('index.html', terms="Server is stoped!")

webp.run()