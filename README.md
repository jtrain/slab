# slab
A full webapp, running on your desktop.

Slab is a sample application that you can extend to make a webapp that runs on a desktop.
The browser is connected to the server via localhost. Deploying is just running the `run.py` file
and seeing the browser open to the `localhost:8080` page.

Slab will detect when the host has been closed, and display a message asking the user to start it again.

Slab was built with Python's bottle, purecss.

### run a slab app
```
python run.py
```
If you were to include the bottle source, then nothing else is required.

- no virtualenv
- no pip
- no connection to the internet

### slab compared to

#### Electron
Yeah. Its like electron. Both the client and the server are on the same machine. 
The main difference is that you don't get the nice things electron gives you:
 - easily bundle for multi platform distribution
 - node.js

You can of course bundle this, but you'd just zip up your folder and send it to someone, and they can run it.
No install required, so long as Python is on their system. You couldn't send a slab app to a non-developer and
expect to get away with it. While you could send an electron app to that same person.

#### Django
Well, you could do this same thing with Django. slab apps only require bottle. bottle is a single file, and you can
easily zip up and send the app to someone.

### where was this made with love?
Oh you ran the app and it didn't say "made with 💗" anywhere on it?
I didn't make it with any 💗, but I'm willing to accept PRs from people who do have 💗 to give to this project.
