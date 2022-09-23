#!/bin/bash
# causes the server to respond with a message
curl -sLX PUT -H "origin:You got me!" -d "user_id=98" 0.0.0.0:5000/catch_me
