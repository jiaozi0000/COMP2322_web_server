COMP2322 Mu2 Multi-thread Web Server
Project README File
Course:Comp2322 Computer Networking
Author:LI Zhifei 24101856D
1. Project Description
This project implements a multi-threaded Web server in Python that can
handle HTTP GET and HEAD requests. The server supports serving text files
(HTML, TXT) and image files (JPG, PNG, GIF). It returns appropriate HTTP
status codes including 200, 400, 403, 404, and 304.

2. Project File Structure
comp2322-web-server/
|-- server.py              # Main server program
|-- README.txt             # This file
|-- www/                   # Directory for web resources
|   |-- index.html         # Default home page
|   |-- test.txt           # Text file for testing
|   |-- test.jpg           # Image file for testing
|   |-- test.png           # Image file for testing
|-- log.txt                # Server log file

3. How to Run the Server
Step 1: Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux)
Step 2: Navigate to the project directory
        Example: cd C:\Users\YourName\comp2322_web_server
Step 3: Run the server with a port number
        Example: python server.py 8080
Step 4: The server will display "Server is running on 127.0.0.1:8080"

4.How to Test the Server
Open a web browser and enter the following URLs:

  (A) Test GET request for text file (200 OK):
      http://127.0.0.1:8080/index.html

  (B) Test GET request for image file (200 OK):
      http://127.0.0.1:8080/test.jpg

  (C) Test 404 Not Found:
      http://127.0.0.1:8080/nonexistent.html

  (D) Test HEAD request (using command line):
      curl -I http://127.0.0.1:8080/index.html

5.How to Stop the Server
Press Ctrl + C in the terminal window.
