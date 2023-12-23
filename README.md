Task 1 

Combine code into a unified format using Python
Combine code into a unified format using Python

Task 2

Analyse the client's data
Create a dashboard using Tableau

The background information the task


Having your data unification algorithm, Daikibo's tech team has converted all telemetry data collected from the 4 factories of the company:

Daikibo Factory Meiyo (Tokyo, Japan)
Daikibo Factory Seiko (Osaka, Japan)
Daikibo Berlin (Berlin, Germany)
Daikibo Shenzhen (Shenzhen, China)
Each location has 9 types of machines, sending a message every 10 min.
Daikibo has been collecting this data for 1 month (May 2021) and they've just shared this data in the form of a single JSON file.

The reason this client wanted to collect telemetry was to answer 2 questions:

In which location did machines break the most?
What are the machines that broke most often in that location?


Task 3

How to turn a client's desires for a project into a proposal

Write a proposal for creating a dashboard 


Task 4

How to support a client in a cybersecurity breach
How to read web activity logs

Help a client determine the source of a data breach
Answer questions to identify suspicious user activity

the background information on the task

A big news publication has revealed sensitive private information of Daikibo Industrials' – a production problem has caused their assembly lines to stop, threatening the smooth operation of supply chains relying on Daikibo’s products. The client suspects the security of their new status board may have been breached.

In this task you will be joining our Cyber Security team. Your job is to:

Determine if the alleged breach could have happened from an attacker on the Internet, directly (no access to Daikibo's VPN).
Hint: go back to the scope requirements of the status dashboard (previous task) and look for the answer there
Inspect a web_requests.log file (listing only data from a period when the alleged attack has to have happened):
Try to spot suspicious requests
Hint: in the Resources section you can find a diagram example on how to read the logs file
Hint: Look for longer sequences of user requests
Hint: notice the order of request from Login → to requests for the dashboard page's resources (styles, scripts, images, etc.) → to api requests for the actual statuses of the machines
Hint: How would you recognize if an automated request to the API happens at an exact interval of time (assume no such functionality is available in the dashboard)
 
If you've identified such requests - make sure to write down the id of the user (it's part of the requests)
Here is how the web_requests.log file is structured:

There is a sequence of blocks of text, divided by an empty line
Each block represents the activity of a unique IP address (no 2 blocks have the same IP)
The block starts with the IP address followed by a table of the requests made to Daikibo's telemetry dashboard by the device with this IP address, sorted by time
The IP addresses are from the internal Daikibo's network and are static
1 block can represent 1 or multiple browsing sessions
Sessions made on different dates require new login
There is no continuous polling/pushing of data between client & server - the users need to refresh the page to get the latest
Hint: For an easier visual inspection, open up the file in a code editor like Sublime Text or Visual Studio Code, expand the window to the full width of your screen and decrease font size until you no text breaks on new line
When you believe you have answered the 2 questions above - submit the task by taking a quick quiz to check your discoveries. Start the quiz by clicking 'Start your quiz' below. Good luck!


Task 5

After a worrisome number of internal complaints on gender inequality (in terms of pay), Daikibo Industrials wants us to help them investigate.

The Forensic Tech team has built an algorithm to quantify “level of gender pay equality” for most/all job roles within the company, in all company locations. Our Forensics lead thinks it will be a great welcoming task for you to finish the job.

We have processed all data on employee compensation and we've generated an excel file (Equality Table.xlsx, available in the Resources) containing 3 columns:

Factory
Job Role
Equality Score (integer; ranging between -100 and +100; 0 is ideal)
Here is your final task:

Create a 4th column (Equality class), classifying the equality score in those 3 types:
Fair (+-10)
Unfair (<-10 AND >10)
Highly Discriminative (<-20 AND >20)
Examples:

6 → Fair
-9 → Unfair
-30 → Highly Discriminative


 
