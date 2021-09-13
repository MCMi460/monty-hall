# monty-hall
*I don't believe this, so I'm going to prove it wrong.* - Me, 34 minutes ago

The situation is clear: You are on a gameshow, and you are given the choice to choose between 3 doors.

One has a sports car behind it, but the other two have goats behind them.

<table>
  <tr>
    <th rowspan="1">🚪Door 1</th>
    <th rowspan="1">🚪Door 2</th>
    <th rowspan="1">🚪Door 3</th>
  </tr>
  <tr>
    <td align="center">❌Goat</td>
    <td align="center">✅Car</td>
    <td align="center">❌Goat</td>
  </tr>
</table>

So you pick a door (let's say Door 3), but then the gameshow host reveals a goat behind one of the doors you did not choose.

<table>
  <tr>
    <th rowspan="1">🚪Door 2</th>
    <th rowspan="1">🚪Door 3</th>
  </tr>
  <tr>
    <td align="center">✅Car</td>
    <td align="center">❌Goat</td>
  </tr>
</table>

He asks if you'd like to switch doors or keep your current choice.

Now, here's your big choice: **Switch or Stay?**

It seems kind of obvious that the difference is miniscule, right? After all, now it's a 50/50 chance of choosing the right door, so staying should be good, right?

Well, as it turns out, switching doors has about a 17% increase in getting the sports car.

The commonly accepted answer is that the choice was once a 1/3 (33.3%), and now that you have a 1/2 chance (50%), you should switch doors otherwise you're still at 1/3.


<table>
  <tr>
    <th rowspan="1">Staying</th>
    <th rowspan="1">Switching</th>
  </tr>
  <tr>
    <td align="center">33.3%</td>
    <td align="center">50%</td>
  </tr>
</table>

And this is, for the most part, completely accurate (for whatever bizarre reason). You'll see a [quick simulation written in Python](/main.py) in this repository.

Sure enough, it proves the theory. 33.3% (on average) of the time, staying wins, and 50% of the time, switching wins. Why this is is still to be determined, as I'm going to prove why this makes no sense in any sort of logic.

However, you'll notice that that isn't the only file on this repository. There are still more files. [100.py](/100.py) is just the same experiment as above, but with 100 doors in total, and instead of removing one door, the gameshow host removes 98. This proves the same percentages as the original experiment.

The real kicker and kick in the nuts to reality is [switch.py](/switch.py). This is the same old door trick, but I removed staying. Instead, I replaced it with a twist on switching. Switching will let you choose between the new door and your first choice.

I'm going to let the data speak for itself:

<table>
  <tr>
    <th rowspan="1">Switching</th>
    <th rowspan="1">'Switching'</th>
  </tr>
  <tr>
    <td align="center">50%</td>
    <td align="center">50%</td>
  </tr>
</table>

**THIS MEANS** that you could literally just say *"I'm switching my door"* and choose the same door and you'd have a 17% higher chance of winning than just saying "I'm keeping my choice". What the frick.

I understand that that isn't exactly what that means, but the problem never ceases to mystify me.

(EDIT: Here's a quick note to mention, and that's that my NEW 'SWitching' method actually just mixes switching and staying, and the average between 33.3% and 66.6% is about 50%, so I didn't prove anything by saying you could choose the same door and get a +17% chance of winning. Thanks Ray for explaining this to me!)
