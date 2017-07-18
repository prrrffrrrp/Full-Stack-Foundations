from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlalchemy.exc
import cgi
from restaurants_queries import allRest, newRest, restId, renameRest


class webserverHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith('/restaurants'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ''
                output += "<h2><a href='/restaurants/new'>Make your own restaurant</a></h2>"
                output += "<br><br>"
                restData = allRest()
                for rest in restData:
                    output += "<html><body>"
                    output += "<h3>{}</h3>".format(rest)
                    output += "<a href='/restaurants/{}/edit'>Edit</a><br>".format(restId(rest))
                    output += "<a href=#>Delete</a><br><br>"

                self.wfile.write(output.encode("utf-8"))
                return

            if self.path.endswith('restaurants/new'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ''
                output += '<html><body>'
                output += """
                <form method ='POST' enctype='multipart/form-data'>
                <h1>make a new restaurant<h1>
                <input name='rest_new_name' type='text'>
                <input type='submit' value='create' >
                </form>"""
                output += "</body></html>"
                self.wfile.write(output.encode("utf-8"))
                return

            if self.path.endswith('/edit'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += """
                <form method='POST' enctype='multipart/form-data'>
                <h1>change the restaurant name</h1>
                <input name='change_name' type='text'>
                <input type='submit' value='edit'>
                </form>"""
                output += "</body></html>"
                self.wfile.write(output.encode("utf-8"))
                return

        except IOError:
            self.send_error(404, 'File not found %s' % self.path)
        except sqlalchemy.orm.exc.MultipleResultsFound:
            self.send_error(500, 'There is more than one restaurant with this name')


    def do_POST(self):
        try:
            if self.path.endswith('restaurants/new'):
                ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('rest_new_name')

                newRest(messagecontent[0].decode("utf-8"))

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()



            if self.path.endswith('/edit'):
                ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('change_name')

                new_name = messagecontent[0].decode("utf-8")
                renameRest(new_name)

                self.send_response(301)
                self.send_header('Content-type', 'text-html')
                self.end_headers()



        except:
            print("No no, no no no no!")


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print("Web server running on port {}".format(port))
        server.serve_forever()

    except KeyboardInterrupt:
        print("^C entered, stopping web server...")
        server.socket.close()

if __name__ == '__main__':
    main()
