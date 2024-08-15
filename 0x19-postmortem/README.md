Issue Summary
Duration of Outage:
August 10, 2024, 15:15 - 16:45 WAT (1 hour 30 minutes)
Or, as we like to call it, the “Hour and a Half of Pure Panic.”

Impact:
75% of our users suddenly became the proud recipients of the “HTTP 500 Club” membership. Websites were slower than a Monday morning, and the remaining 25% were probably just enjoying the chaos. Sadly, this wasn’t a special promotion.

Root Cause:
Turns out, our Apache HTTP server and a new SSL certificate had a little disagreement, resulting in a server mutiny. No humans were harmed, but our uptime sure took a hit.

Timeline
15:15 WAT - Ding ding! Engineer notices a surge in HTTP 500 errors. (At least it wasn’t an alarm clock.)
15:20 WAT - Monitoring alerts start blowing up our phones. Chaos ensues.
15:25 WAT - Everyone's thinking, “It’s gotta be a DDoS attack, right?” Nope.
15:40 WAT - Network team gives the all-clear. Cue the collective head-scratching.
15:50 WAT - Apache logs read: "SSL handshake errors." Someone quips, “Guess it’s not as friendly as a handshake.”
16:00 WAT - DevOps steps in, realizing the SSL certificate was trying to break up with Apache.
16:15 WAT - We fix the Apache configuration, tell the SSL certificate to play nice, and restart everything.
16:45 WAT - Victory! Everything’s back to normal. Crisis averted, sanity restored.
Root Cause and Resolution
Root Cause:
The new SSL certificate was like the fancy new kid at school, but Apache wasn’t ready for its high standards. The certificate demanded an up-to-date protocol, while Apache was still using an old directive. This mismatch led to SSL handshake failures and the resulting server chaos. Picture Apache servers throwing a tantrum—only less cute.

Resolution:
We updated the Apache configuration to match the SSL certificate’s demands. After a stern talking-to and a few tweaks, the servers were restarted, and order was restored. The SSL certificate and Apache are now back on speaking terms.

Corrective and Preventative Measures
Improvements:

Improve communication so that SSL updates don’t sneak up on us like a bad surprise party.
Enhance our monitoring tools to catch SSL handshake issues before they spiral out of control.
Tasks:

Patch Apache Server Configuration: We’ll give our servers a fresh coat of paint, aka updated SSL protocols and cipher suites.
Add Monitoring for SSL Handshake Errors: Because nobody likes surprises, especially not our servers.
Run SSL Compatibility Checks: Before introducing a new SSL certificate, we’ll make sure everyone plays nice.
Document SSL Update Procedure: Step-by-step instructions, so no one is left guessing.
Postmortem Review Meeting: Time to gather, laugh about the chaos (or cry), and make sure this doesn’t happen again.
Visual Summary
(Imagine a playful diagram here with the SSL certificate and Apache in a wrestling ring, finally shaking hands in the end. Maybe throw in a “Server Down” emoji for good measure.)

By making these improvements, we’re not just fixing today’s problems—we’re ensuring a future where our servers and SSL certificates live happily ever after. Or at least, until the next update.