<h1 align="center">WeConverse</h1>

<br>

<h2 align="center">Overview</h2>

<p>This is an online messaging service using Flask, similar in spirit to Slack. Users will be able to sign into the site with a display name, create channels (i.e. chatrooms) to communicate in, as well as see and join existing channels. Once a channel is selected, users will be able to send and receive messages with one another in real time.</p>

<h2 align="center">Features</h2>
 
 <p><b>Display Name:</b> When a user visits the web application for the first time, they should be prompted to type in a display name that will eventually be associated with every message the user sends. If a user closes the page and returns to the app later, the display name should still be remembered.</p>
 
 <p><b>Channel Creation:</b> Any user can create a new channel, so long as its name doesn’t conflict with the name of an existing channel.</p>
 
 <p><b>Channel List:</b> Users can to see a list of all current channels, and selecting one should allow the user to view the channel.</p>
 
 <p><b>Messages View:</b> Once a channel is selected, the user can see any messages that have already been sent in that channel, up to a maximum of 100 messages. The app will only store the 100 most recent messages per channel in server-side memory.</p>
 
 <p><b></b></p>
 
 <p><b>Sending Messages:</b> Once in a channel, users can send text messages to others in the channel. When a user sends a message, their display name and the timestamp of the message will be associated with the message. All users in the channel can then see the new message (with display name and timestamp) appear on their channel page. Sending and receiving messages does NOT require reloading the page.</p>
 
 <p><b>Remembering the Channel:</b> If a user is on a channel page, closes the web browser window, and goes back to the web application, the application will remember what channel the user was on previously and take the user back to that channel.</p>
