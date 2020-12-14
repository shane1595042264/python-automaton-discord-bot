# python discord bot
## Introduction
I am a cannon school student who is doing this project called. My most code ideas are from documentation of discord.py. I basically just browse through it and see what I can do about my bot. Whenever I encounter problems, I would first figure out by myself. If that doesn’t work,  I would throw that question on Stackoverflow. But I usually solved it by myself while waiting for an answer. One of the dumbest questions is about the role reaction thing. I posted chunks of code to expect an answer, but as someone pointed out that my method name is wrong. I wrote “add_role”, but it should be “add_roles”, this little “s” wasted me half an hour of debugging.


## Feature list:
* Get role by reacting. I used on_reacion method and add_roles method. It’s fairly easy, but I struggled on different variables' names.
* Remove role by dis-reacting (remove_roles)
* Get a banana picture by reacting banna. For this, you need to import the banana.jpg in the same folder as your code’s.
* !time for how long you’ve been in this server. This is from documentation, there are some new classes and methods such as @property, super(). I don’t quite understand what those are so I just used it.
* !poke, somebody, reason -> Poke someone and say something. For this command, I used random.choice so that it can randomly pick members.
* !food -> tell everybody what you want to eat
* !add -> add number
* !up (para) - > to transform words into uppercase
* Language detection system, which can also memorize how many times people swore and give different reactions. I basically created a word list that contains the bad words, and an on_message function that could detect if there’s any word in that message, then it could delete that message and send some warnings. Once the user violates the rule, the counter will ++, so that it could give different warnings. It can’t store the times when a specific person says bad words.
* Detect insecure message attachment in chat. It’s the same principle as the above.
* !Hello for hello
* !server-> to get server name
* !botinfo -> to get the bot information
* Type minecraft to get speedrun encouragement
* !counter-> check how many times you violate the language rules
* End sentence with “?” to get search link.
* End sentence with “!” to get thumbs up reaction
* Type “create channel” to create a channel.
