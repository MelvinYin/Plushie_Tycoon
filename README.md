##Plushie Tycoon

####Description
<p>
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
</p>
<p>
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
</p>

####Requirements
Bokeh 2.0, although it should work from 0.13. Python 3.6+. To run, cd to
project directory, in conda env run bokeh serve --show src. This executes
main.py in src. 

####How To Use
Select Buy/Sell/Make, select Resource/Res or Product/Prod, and select item
. Key in quantity, and click send. Next on the other side ends the turn. Back
roll back uncommitted changes, so once you select Next you can't undo. Save
and Load works locally, maybe. Quit is meant to quit. 
  
####Detailed Description
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
 
####Todo List
In chronological order:
1. Migration of backend to Java, keeping frontend as python for now, using
 py4j to interface between the two. This requires simplifying certain
  features initially to make transition easier.
2. Move frontend to spring boot/react stack
2. Further implement features.
3. Tests, linters, CI/CD, dockerfile, docs. Maybe a description landing page?