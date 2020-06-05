### Plushie Tycoon

#### Description
Well, it's meant to copy that anyway. Inspired by Neopets' plushie tycoon
business simulator game sometime in 2000s, the original game has the player
adopting the role of a manager of a plushie business. Resources are bought
on an open market, employees and factory space are rented to produce the
plushies, and they are then sold in an upgradable storefront with prices
also based on an open market. The idea behind it is that once players scale
, their buying and selling decisions start to have an impact on market prices
for other players and for themselves. Player decisions, say to buy 10 aisha or
make 20 beta, are collated and executed all together at month's end, adding some stochastic noise to execution, such as price
fluctuations leading to you buying less than what you want, or selling
plushies at a lower price than you expect. Yeah that's painful, since
plushies can and often sell for below cost. 

Here, we adopt something similar. The ultimate goal is to have a global
market server, with client players connecting to it. Each client create a
set of decisions, and these are sent to the market server per turn to decide
on what the results are going to be. For instance, a client may send 10,000
dollars to purchase 1,000 aisha, but end up with 800, or 1000 aishas and a
refund of 1000, or 1,200 aisha, depending on whether it's a cost order to
use up all funds or a quantity order. 

Interesting bits that separate it from being an order execution system are in
its market pricing and player strategy evolution. Markets are cleared
dynamically with these forces:
1. Players, driven by human decisions. This change both demand and supply. 
2. Speculators. These buy and sell immediately when prices of products are
significantly below or above cost, and do the same on the resource side
. Cash capacity is limited. This change both demand and supply. 
3. Physical Hoarders. Similar to speculators, but with a longer time delay
and limited moving quantity per turn. Time delays lead to behaviour that
follow trend prices more than spot prices. This change both demand and
supply, and is dependent on how much there is in storage earlier
. Storage capacity is limited. 
4. Producers and consumers. Even longer time delay, requires significant
deviation over a non-singular period of time to execute, whether
cutting down or ramping up production. This change both demand and
supply, but ramping up production for product increase demand for
constituent resources. Unlimited capacity. 
5. Random noise
6. Base sinusoidal fluctuation in market. 
7. Spikes and troughs, only in prices, sudden and not tied to any factors. For
example, a price spike in aisha product does not mean increased demand for
resources immediately, it is not a production spike, just prices. Although
you should expect market players to respond in the next turn. Uncommon, not
meant to be planned for, rather to be reacted to. Storage cost makes hoarding
 untenable, but if you do just-in-time you may be hurt badly.

Final price is determined by a clearing house that change prices until
quantity bought at price == quantity sold. Player buyers for example are
price-independent for now, while speculators have linear price-quantity
curves. Players cannot see any of these behaviour, only the final clearing
price. 

There's also things like move-in and move-out cost for items, storage cost
, tier list for storage that changes storage capacity and possibly movement
 cost, prices for such upgrades, and similar stuff on the production side.

That's the eventual goal, for now it's nowhere near. 


#### Requirements
Bokeh 2.0, although it should work from 0.13. Python 3.6+, Maven 3.6.3
, libprotoc 3.11.4, python -m grpc_tools.protoc
 --version libprotoc 3.11.2, openjdk 14.0.1 2020-04-14

#### How To Use
Select Buy/Sell/Make, select Resource/Res or Product/Prod, and select item
. Key in quantity, and click send. Next on the other side ends the turn. Back
roll back uncommitted changes, so once you select Next you can't undo. Save
and Load works locally, maybe. Quit is meant to quit. 
  
#### Detailed Description

##### Java Server
(see python first) Simplified by removing GS layer, moving all to GE
. Otherwise the two are largely similar, at time of port. It has MockService
 and MockGE for testing and debugging. 

##### Python Server<br>_Deprecated_

GE is game engine, GS is game state. GE implements commands like buy and sell
, GS stores current state information such as inventory and market prices
, and implements certain backend and maintenance methods. Each player has
their own GE and a local GS, to give feedback on what their uncommitted
decisions will do. At the end, these decisions are collapsed (2 buys on
same product into a single one), movement and storage costs are added in
, and the decisions are sent to GlobalGS. GlobalGS settles clearing house
and etc, obtain actual player changes, and send back the "real" inventory
, prices, and budget to the players. That ends a turn.

Inventory object settles movement, storage costs calculation, keep quantity
. Market object keep prices, local has static prices, global has clearing
house. GS therefore keeps a copy of these. GSHistory tracks all
uncommitted changes (only in local), to implement back function. Parameters
such as resource ratios, storage cost, kept static for now
. UI settles ui, using bokeh. 

#### To run
To build python grpc, cd to src, run python -m grpc_tools.protoc --proto_path . --python_out=. --grpc_python_out=. ./grpc.proto 
To build java grpc, cd to maven, run mvn package

To run java server, run PlushieServer.java
To run python frontend, at project directory with src in folder, run bokeh serve --show src

#### Developer Notes
1. Don't bother trying to get java to work without mvn, it's a pita. Grpc
 support for java compilation for grpc (not protobuf, that one is fine
 ) without gradle or maven build systems is very weak, and online
  documentation is crap. Stick to this for now, I know it sucks.

2. Don't attempt to integrate python into maven build system for now, maven
 has sparse multi-language support, and if it breaks it's hard to debug
 . Again, I know the current directory structure sucks.

3. To build grpc-generated classes in java, change `.proto` then run `mvn
 package`. To run manually, I have a `./support/executables/protoc-gen-grpc
 -java.exe` executable. To use this, move this to same folder as your `.proto
  ` file, then run `protoc --plugin=protoc-gen-grpc-java=./protoc-gen-grpc-java.exe  --grpc-java_out=. --proto_path=. --java_out=. ./grpc.proto`. What this does is it uses the executable as plugin to generate the grpc generated classes. If you drop `--grpc-java_out=.`, then it's a purely protobuf call and doesn't need the plugin, but this means you don't have the grpc generated classes. The executable comes from here:
`https://mvnrepository.com/artifact/io.grpc/protoc-gen-grpc-java.`

4. As of 04062020, the helloworld example in `https://grpc.io/docs/languages
/java/quickstart/`, breaks when you try to run `./gradlew installDist`. No
 idea why, probably something to do with java JDK/SDK + gradle + grpc + protobuf versions not being compatible. Do __not__ try to debug. 
  
5. The package name in .proto and in java classes need to be the same. I don't think python need anything here.

6. I have a `./support/server_mock.py` to help debugging the backend side
. Frontend mock is just the original UI for now. 

7. Note that in protoc3, everything is optional by default, but not nullable
. You do not therefore need to fill up everything when debugging, depending
 on caller/receiver ofc. 
 
8. Grpc does not carry out type-checking. If you find that your UI values
 suddenly go to zero, see if the same .proto has been compiled on both java and
  python side. A int32 on one side to double on the other reads as 0. 

#### Todo List
In chronological order:
1. Tune and update java backend, provide original python backend as option
2. Move frontend to spring boot/react stack
2. Further implement features.
3. Tests, linters, CI/CD, dockerfile, docs. Maybe a description landing page
? As if I will reach here.
