var exec = require("child_process").exec;
let a;
const uId = 60;
const command = "python test.py "+ uId ;
exec(command,function(error,stdout,stderr){
    if(stdout.length >1){
    a = stdout;
    
    console.log(a)
    } else {
    console.log("you don\’t offer args");
    }
    if(error) {
    console.info('stderr :', stderr);
    }
    });

  