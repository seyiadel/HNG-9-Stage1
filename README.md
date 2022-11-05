# HNG-9
<h1>HNG 9 STAGE 1 Task </h1>
<h3>Task directory - HNG9-Intern</h3>
<b>Task Description</b>

- Setup a server (Hosted)
- Create an **(GET)** api endoint that returns the following  json response:
{ "**slackUsername**": String,
     "**backend**": Boolean,
        "**age**": Integer,
        "**bio**": String }
        
- Push to **GitHub**
- URL Link to project - https://seyiadel-hng9-stage1.herokuapp.com/
<br>
<h1>HNG 9 STAGE 2 Task </h1>
<h3>Task directory - HNG9_Stage2</h3>
<b>Task Description</b>

- Using the same server setup from stage one
- Create an (POST) api endoint that takes the following sample json:
  { “operation_type”: Enum <addition | subtraction | multiplication> , 
  “x”: Integer, 
  “y”: Integer }
- Operation can either be addition, subtraction or mutiplication
x can be a number and Integer datatype
y can be a number and Integer datatype
- Based on the operation sent, perform a simple arithmetic operation on x and y
- Return a response with the result of the operation and your slack username
{ “slackUsername”: String, "operation_type" : Enum. value, “result”: Integer }
- Push to GitHub
- - URL Link to project - https://seyiadel-hng9-stage1.herokuapp.com/task/ (Tested using Postman)
