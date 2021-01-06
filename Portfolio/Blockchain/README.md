![bitcoin](bitcoin_pic.png)

## Create a local Blockchain

## 8/24/2020

Steps to creating your own coin with MyCrypto using puppeth and the command line tool, geth / "testnet"

1. First step is to go into the Terminal and "cd" into the folder Blockchain-Tool, that should have been installed on the computer already.

- when you are in the folder, type in " ./pippeth " to the command line.

2. Enter the network as "WHATEVER_YOU_LIKE" or something of your choice.

3. Enter the number 2 into the command line next to configure New genesis.

4. Enter 1 to create one from scratch.

5. Enter 2 for Clique, hit Enter when it asks for the amount of seconds.

6. Copy your Public Address without the "Ox" and paste into the Terminal

7. Then hit Enter 2x

8. Should the precompiler . wei... type "no" then press Enter.

9. Specifiy chain/ network: 822 or the number you chose earlier.

** The Block is now Configured **

10. Enter 2 , Enter 2 , Then it asks which folder would you like to save to? Hit Enter

- Should see ( 4 items saved)

11. Control C to quit out of that part.

- in the Terminal list the files in the folder with " ls " to see the recently created files - labeled fintech822

---

Part-2

Steps:

1. Run the command: ./geth account new --datadir node1
   ./geth account new --datadir node2

2. Enter a Password.

3. Copy and save Public Access Key & Secret Key file path. (2x, for 2 nodes)

4. Run the command: ./geth init **\_**.json --datadir node1
   ./geth init **\_\_\_**.json --datadir node2

5. Run the next command:  
   ./geth --datadir node1 --mine --minerthreads 1

   - Quickly copy the " Enode" starts with self= ....

** You are now mining your very own coin **

---

6. Open a 2nd Terminal window and "cd" into Blockchain-Tools again.

7. Run the following command:
   .geth --datadir node2 --port 30304 -- rpc --bootnodes "copy and paste your enode here"

8. To finish and close out go back to MyCrypto and change wallet - logout.

9. Change the network to Custom and then add a custom node.

10. Enter the URL & NODE Name

fintech822
http://127.0.0.1:8545

( To reOpen the nodes from the command line enter the following command to Terminal )
./geth --datadir node1 "PublicAddress" --mine --rpc

---

Web3 Intro: 8/25/2020

Keypair = "public/private keys"

Remove Nodes:

rm -Rf node1/geth node2/geth

Create new nodes:

./geth account new --datadir node1
./geth account new --datadir node2

NODE_1 : password = scottcoin

Public address of the key:  
0x4FDB49e5c0e800D53Bb4b3C8c57300f9135d5f9A

Path of the secret key file: node1/keystore/UTC--2020-08-26T00-17-36.704952000Z--4fdb49e5c0e800d53bb4b3c8c57300f9135d5f9a

NODE_2; password = scottcoin

Public address of the key: 0x60A55442B632ec8a6f44a0af4f7bffD5e6e0626b

Path of the secret key file: node2/keystore/UTC--2020-08-26T00-18-51.197602000Z--60a55442b632ec8a6f44a0af4f7bffd5e6e0626b

Initialize Directory:

./geth init fintech822.json --datadir node1
./geth init fintech822.json --datadir node2

RUN IN SECOND TERMINAL WINDOW:

./geth --datadir node2 --port 30304 --rpc --bootnodes
enode://0cff933ef0cf7572a50dc2baeeb6ae735e5f46383f45edc51d9cb8febfe70322107725253f1cbf763578605ff23602f205d1d9be6ea17174929c49c0ec9e9805@127.0.0.1:30303
