from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

import db


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        with open("index.html", "r") as file:
            html = file.read()

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(html.encode())


    def do_POST(self):

        if self.path == "/employee":

            content_length = int(self.headers["Content-Length"])

            body = self.rfile.read(content_length).decode()

            form = parse_qs(body)

            employee = {

                "employee_name": form["employee_name"][0],

                "dob": form["dob"][0],

                "total_experience": float(form["total_experience"][0]),

                "relevant_experience": float(form["relevant_experience"][0]),

                "employer_name": form["employer_name"][0],

                "notice_period": int(form["notice_period"][0]),

                "serving_notice":
                    form["serving_notice"][0] == "Yes",

                "last_working_day":
                    form.get("last_working_day", [""])[0] or None,

                "email": form["email"][0],

                "phone": form["phone"][0]
            }

            db.save_employee(employee)

            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()

            self.wfile.write(b"""
            <html>
            <head>
                <title>Success</title>
            </head>

            <body>

                <h2>Employee data saved successfully.</h2>

                <a href="/">Add Another Employee</a>

            </body>

            </html>
            """)


server = HTTPServer(("0.0.0.0", 8080), MyHandler)

print("Server started on http://localhost:8080")

server.serve_forever()