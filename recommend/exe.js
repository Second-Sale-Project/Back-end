var exec = require("child_process").exec;
let a;
exec('python test.py 1 ',function(error,stdout,stderr){
    if(stdout.length >1){
    console.log(stdout);
    a = stdout;
    console.log(a)
    console.log(typeof(a))
    a = a.split('[ ]')
    console.log(a)
    } else {
    console.log("you don\’t offer args");
    }
    if(error) {
    console.info('stderr :', stderr);
    }
    });