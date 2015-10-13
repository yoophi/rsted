
어쩌고 저쩌고.
---------------

**Example Request**

.. sourcecode:: http

   POST /api/v1.0/me/customer/inquiry HTTP/1.1
   Accept: application/json
   Accept-Encoding: gzip, deflate
   Authorization: Bearer 7J5dcdZjegYT22iKxZKwN5jDD6Jndy
   Connection: keep-alive
   Content-Length: 157
   Content-Type: application/json
   Host: localhost:8006
   User-Agent: HTTPie/0.9.2
   
   {
       "app_version": "134",
       "body": "xxx",
       "device": "SAMSUNG",
       "email": "xxx",
       "mobile_os_version": "111",
       "phone_no": "xxx",
       "telecom": "olleh",
       "type": "1"
   }

**Example Response**

.. sourcecode:: http
   
   HTTP/1.0 200 OK
   Content-Length: 295
   Content-Type: application/json
   Date: Tue, 13 Oct 2015 05:11:27 GMT
   Server: Werkzeug/0.10.4 Python/2.7.9
   
   {
       "inquiry": {
           "body": "xxx",
           "created_at": "2015-10-13 14:11:27",
           "email": "xxx",
           "id": 6,
           "phone_no": "xxx",
           "type": "1",
           "updated_at": "2015-10-13 14:11:27",
           "user_type": "user",
           "user_uuid": "7052cf99-5d07-11e5-babf-10ddb1d407f7"
       },
       "result": true
   }
