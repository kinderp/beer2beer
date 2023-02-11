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




