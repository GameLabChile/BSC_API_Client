# Create game instance

+ url: `[server]/api/newalone/`
+ protocol: https
+ method: POST

## Variables

### 'player' : name of the player to use in the game
+ accepts only letters uppercase & lowercase, numbers, underscore and dash. (regex: [a-zA-Z0-9 -])
+ use a reasonable length to prevent overflow in the interface

---
### 'teacher' : the username of the teacher

---
### 'esc' : the id of the scene(setting)
+ must be integer

---
### 'time' : unique time or number
+ must be integer
+ it can't repeat

---
### 'classid' : external id for posterior filter on [Get class list](https://github.com/GameLabChile/BSC_API_Client/blob/docs/get_class_list.md)
+ must be integer

---
### 'playerid' : external id to identify players
+ must be integer

---
### 'timeout' : time to live to the game instance
+ in seconds
+ must be integer
+ optional parameter
+ default value is 1209600(14 days)

---
### 'sign' : sign to authenticate the request

#### how to generate it?
+ 1) create a json with the variables (without sign variable)
+ 2) sort the keys alfabetically
+ 3) make an rsa signature with SHA-1 encoding of the json ( the json must be generated like [python](https://docs.python.org/2/library/json.html) does, it uses ": " and ", " separators)
  + the private key is provided by Gamelab
  + more documentation about rsa on python: https://stuvel.eu/files/python-rsa-doc/reference.html#rsa.PrivateKey
+ 4) encode the signature in base64 with urlsafe
  + more documentation about base64: https://docs.python.org/2/library/base64.html

---

## Output

### on success
+ code: 302
+ header with Location redirect ( example: `Location {{server}}/api/startgame/{{game instance hash code}}` )

### on exception
+ code: 400
+ content: posible cause

### on fatal error
+ code: 500
