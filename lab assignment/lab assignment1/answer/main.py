import json
import random
import string
from typing import *

from sympy import re
import config
import mimetypes
from framework import HTTPHeader, HTTPServer, HTTPRequest, HTTPResponse


def random_string(length=20):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def default_handler(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    response.status_code, response.reason = 404, 'Not Found'
    print(f"calling default handler for url {request.request_target}")


def task2_data_handler(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 2: Serve static content based on request URL (20%)
    if(request.method == 'GET') :
        try :
            #成功获取文件的status_code和reason应该设置为200，OK
            response.status_code, response.reason = 200, 'OK'
            #add_header中参数都为str类型，mimetypes.guess_type返回的第一个元素（index为0）是string的文件类型
            response.add_header("Content-Type",mimetypes.guess_type(request.request_target)[0])
            #以二进制格式、采用只读模式打开文件，response中body类型为byte
            file=open("."+request.request_target,'rb')
            response.body=file.read()
            #len返回值为int类型，故进行类型转换
            response.add_header("Content-Length",str(len(response.body)))
            file.close()
        except FileNotFoundError :
            #当文件不存在时返回404，Not Found
            response.status_code, response.reason = 404, 'Not Found'
        print(f"calling task2_data_handle for url {request.request_target}")
    elif(request.method == 'HEAD'):
        #HEAD并不返回请求对象，所以以下部分并没有response.body=file.read()
        try :
            #成功获取文件的status_code和reason应该设置为200，OK
            response.status_code, response.reason = 200, 'OK'
            #add_header中参数都为str类型，mimetypes.guess_type返回的第一个元素（index为0）是string的文件类型
            response.add_header("Content-Type",mimetypes.guess_type(request.request_target)[0])
            #以二进制格式、采用只读模式打开文件，response中body类型为byte
            file=open("."+request.request_target,'rb')
            #len返回值为int类型，故进行类型转换
            response.add_header("Content-Length",str(len(file.read())))
            file.close()
        except FileNotFoundError :
            #当文件不存在时返回404，Not Found
            response.status_code, response.reason = 404, 'Not Found'
        print(f"calling task2_data_handle for url {request.request_target}")
    else:
        #当请求方式为POST时
        print('The method is not allowed ')
    pass


def task3_json_handler(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 3: Handle POST Request (20%)
    response.status_code, response.reason = 200, 'OK'
    if request.method == 'POST':
        binary_data = request.read_message_body()
        obj = json.loads(binary_data)#json.loads返回的对象是python里面字典对象，请求报文实体含有data key和其他key
        # TODO: Task 3: Store data when POST

        #Content-Length always exists in every POST
        request.headers.append(HTTPHeader("Content-Length",str(len(binary_data))))
        #request.headers.append(HTTPHeader("Content-Type",mimetypes.guess_type(obj)[0]))
        #json.loads返回的对象是python里面字典对象,键值对都用""囊括，而server.task3_data是str，故要进行一个转换
        print(obj["data"])#检验
        server.task3_data=str(obj["data"])

        pass
    else:
        obj = {'data': server.task3_data}#将上次post的内容储存到obj中
        return_binary = json.dumps(obj).encode()#json.dumps将obj转换成字典对象，再编码成进行传输

        #返回的类型应该是编码前的类型,即返回json类型，返回的长度应该是编码成byte后的长度
        response.add_header("Content-Type","application/json")
        response.add_header("Content-Length",str(len(return_binary)))
        response.body=return_binary
        pass


def task4_url_redirection(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 4: HTTP 301 & 302: URL Redirection (10%)
    #set the status_code and reason of response
    response.status_code,response.reason=302,'Found'
    #add "Location" and new URL to the header lines of response
    response.add_header("Location",'http://127.0.0.1:8080/data/index.html')
    pass


def task5_test_html(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    response.status_code, response.reason = 200, 'OK'
    with open("task5.html", "rb") as f:
        response.body = f.read()


def task5_cookie_login(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 1 Login Authorization
    obj = json.loads(request.read_message_body())
    if obj["username"] == 'admin' and obj['password'] == 'admin':
        # If equal, set the status_code and reason of response to 200 and OK, and response Set-Cookie: Authenticated=yes
        response.status_code,response.reason = 200, 'OK'
        response.add_header("Set-Cookie","Authenticated=yes")
        pass
    else:
        # If don't equal, set the status_code and reason of response to 403 and Forbidden
        response.status_code,response.reason = 403, 'Forbidden'
        pass


def task5_cookie_getimage(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 2 Access Protected Resources
    # test if cookie in header lines
    for sub_header in request.headers:
        if sub_header.name == "Cookie" and sub_header.value == "Authenticated=yes":
            #if header lines contains cookie and the Authenticated field is yes
            #set the status_code and reason of response to 200 and OK , and response content, content_length and conteny_type
            response.status_code,response.reason = 200, 'OK'
            file=open(".\\data\\test.jpg",'rb')
            response.body=file.read()
            response.add_header("Content-Type",mimetypes.guess_type(".\\data\\test.jpg")[0])
            response.add_header("Content-Length",str(len(response.body)))
            file.close()        
        else:
            #f the Authenticated Cookie doesn't exist or isn't yes, set the status_code and reason of response to 403 and Forbidden
            response.status_code,response.reason = 403, 'Forbidden'
    pass


def task5_session_login(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 1 Login Authorization
    obj = json.loads(request.read_message_body())
    if obj["username"] == 'admin' and obj['password'] == 'admin':
        session_key = random_string()
        while session_key in server.session:
            session_key = random_string()

        # If equal, set the status_code and reason of response to 200 and OK, and response Set-Cookie: SESSION_KEY=xxxxx
        response.status_code,response.reason = 200, 'OK'
        response.add_header("Set-Cookie","SESSION_KEY="+session_key)
        #将生成的session_key以{'SESSION_KEY': 'SESSION_KEY=xxxxx'}的形式储存在server.session
        server.session.update({'SESSION_KEY': 'SESSION_KEY=' + session_key})
       
        pass
    else:
        # If don't equal, set the status_code and reason of response to 403 and Forbidden
        response.status_code, response.reason = 403, 'Forbidden'


def task5_session_getimage(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 2 Access Protected Resources

     # test if cookie in header lines
    for sub_header in request.headers:
        if sub_header.name == "Cookie" and sub_header.value == server.session["SESSION_KEY"]:
            #if header lines contains cookie and the SESSION_KEY is valid
            #set the status_code and reason of response to 200 and OK , and response content, content_length and conteny_type
            response.status_code,response.reason = 200, 'OK'
            file=open(".\\data\\test.jpg",'rb')
            response.body=file.read()
            response.add_header("Content-Type",mimetypes.guess_type(".\\data\\test.jpg")[0])
            response.add_header("Content-Length",str(len(response.body)))
            file.close()        
        else:
            #f the Authenticated Cookie doesn't exist or isn't yes, set the status_code and reason of response to 403 and Forbidden
            response.status_code,response.reason = 403, 'Forbidden' 
    pass


# TODO: Change this to your student ID, otherwise you may lost all of your points
YOUR_STUDENT_ID = 12011923

http_server = HTTPServer(config.LISTEN_PORT)
http_server.register_handler("/", default_handler)
# Register your handler here!
http_server.register_handler("/data", task2_data_handler, allowed_methods=['GET', 'HEAD'])
http_server.register_handler("/post", task3_json_handler, allowed_methods=['GET', 'HEAD', 'POST'])
http_server.register_handler("/redirect", task4_url_redirection, allowed_methods=['GET', 'HEAD'])
# Task 5: Cookie
http_server.register_handler("/api/login", task5_cookie_login, allowed_methods=['POST'])
http_server.register_handler("/api/getimage", task5_cookie_getimage, allowed_methods=['GET', 'HEAD'])
# Task 5: Session
http_server.register_handler("/apiv2/login", task5_session_login, allowed_methods=['POST'])
http_server.register_handler("/apiv2/getimage", task5_session_getimage, allowed_methods=['GET', 'HEAD'])

# Only for browser test
http_server.register_handler("/api/test", task5_test_html, allowed_methods=['GET'])
http_server.register_handler("/apiv2/test", task5_test_html, allowed_methods=['GET'])


def start_server():
    try:
        http_server.run()
    except Exception as e:
        http_server.listen_socket.close()
        print(e)


if __name__ == '__main__':
    start_server()
