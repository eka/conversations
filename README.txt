an app that provides conversations a la FB between users

entities:

User
Conversation
Message

definitions

Conversation:
has many users
has many messages

User:
has many conversations
has many messages

Message:
has 1 conversation
has 1 user

