# beer2beer
A working demo of a peer 2 peer system and relative protocols

## How to start

Before doing anything you must configure your account, in particular you need to **generate**_ a new **ssh key** and **add** that to your github account in order to be able to intarct with (cloning, committing) this repo.

Please follow these links:
1. [Generate a new ssh key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
2. [Add a new ssh key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

After doing that you should be able to clone thw whole codebase hosted here.

## About the system

We'd like to implement an old style peer to peer system composed by an indexing server and multiple clients acting as peers.
Indexing server will be used just as central storing system by all peers in order to make queries and searching for a specif filename. A server response will produce enough informations for a peer in order to contact peers that really host that searched filename so downloading operations will be handled by peers that will act as client in search operations and as a server after being contacted by a peer for getting a file.

## About Protocol

Each message exchanged between server and peers will be composed by two parts: `header` + `payload`

**header** is built in this way:

```
+----------------+-----------------+
| payload length | type of message |
| (in bytes)     | (in bytes)      |
+----------------+-----------------+
```

**payload** is just a string encoded with **utf-8** charset. Payload depends on the type of message.
Please, see down below table for informations about payload contents of each message.


### Client
| message type      | payload                                                                          |
| ----------------- |----------------------------------------------------------------------------------|
| **LOGIN**         | ```username\npassword\nid```                                                     |
| **REGISTER**      | ```usernmae\npassword\nfilename1\|dimension_in_mb\|sha1\nfilename2\|dimension_in_mb\|sha1```|    
| **KEEP_ALIVE**    | ```id```                                                                         |



### Server

| message type        | payload                  |
| ------------------- |--------------------------|
| **LOGIN_OK**        | ```LOGIN SUCCESS```      |
| **LOGIN_KO**        | ```Insert here a description of error occurred on the server side``` |
| **REGISTER_OK**     | ```REGISTER SUCCES```    |
| **REGISTER_KO**     | ```Insert here a description of error occurred on the server side``` |
| **KEEP_ALIVE_OK**   | ```KEEP ALIVE SUCCESS``` |
| **KEEP_ALIVE_KO**   | ```Insert here a description of error occurred on the server side``` |

## About server

* Register and Indexing
  ```
  Each peer needs to announce itself to the indexing server with a register call.
  During current process a peer must communicate to the server all the files that 
  it wants to share with all the other peers.
  For each file in this list it must provide the following informations:
  
  1. filename
  2. dimension in Mb
  3. sha1
  
  As a result of this registration process an unique id will be released by server
  to current peer. Peer will use this id in login call. A login call to indexing se-
  rver is mandatory each time a registered peer wants to connect to the network.
  Peer's id will be used as key in server's index and as identifier for  a peer  in 
  the network.
  
  A peer can't interact with another peer in the network if it didn't make  a login 
  call (in other words its status is set to offline).
  
  Each registration has a TTL (time to live).
  TTL works in this way: it is set to 30 days but it is refreshed each time current
  peer makes a login call. So  TTL will expire only if a peer does not make a login
  call in 30 days.
  
  If a peer needs to update its list, it can perform a update register call sending
  its id end a new list. A peer can need to send a new registration call (NOT inclu
  ding its old id in the request) it can be done but the old one will be lost because
  of TTL in 30 days. A new fresh id will be released and  the  old one  will be deleted
  together with the old indexes for the current peer.
  ```
  
* Login
  ```
  Before doing any calls to the server or any interactions with other peers, each re-
  istered peer needs to make a login call to the server.
 
  During a login call a peer just send its id (obtained during registration process) 
  to the server. After that, server will set peer's status to online value.
  Every 5 minutes an active peer must send a keep alive call in order to maintain its
  online status.
  ```

* Keep Alive
  ```
  After a login call a peer must send a keep alive call to maintain its online status in-
  side the network
  ```

* Logout
  ```
  A peer before quitting must send a logout call to set itself as offline
  ```

* Show Peers
  ```
  Show online/offline/all peers
  ```
  
* Browse Peer
  ```
  Show all the indexes for a peer. In other words, show all the shared files of current peer in the network
  1. filename
  2. dimension
  3. sha1
  ```
  
* Search

  ```
  As a reply to a searching call coming from a peer, indexing server must provide at least a couple (ip_peer, port_peer)
  containing ip_addr and port_addr of the peer in the network that hosts that specific searched filename
  ```

  
## About peers

* Register
  ```
  username
  password
  filename1|dimension|sha1
  filename2|dimension|sha1
  ...
  filenameN|dimension|sha1
  ```

* Login
  ```
  username\npassword\nid
  ```

* Keep Alive
  ```
  id
  ```

* Logout
  ```
  username\npassword\id
  ```

* Search

* Download




