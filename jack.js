 const { Module } = require('module');
const os = require('os');
//  console.log(os);
const user = os.userInfo()
// console.log(user);
console.log(os.uptime());
console.log("1 ===============tmpdir()=================");
console.log(os.tmpdir());
console.log("2 ==============version()==================");
console.log(os.version());
console.log("3 ==============type()==================");
console.log(os.type());
console.log("4 ==============totalmem()==================");
console.log(os.totalmem());
console.log("5 ================================");
// console.log(os.setPriority());
console.log("6 =============release()===================");
console.log(os.release());
console.log("7 ==============platform()==================");
console.log(os.platform());
console.log("8 ==============networkInterfaces()==================");
console.log(os.networkInterfaces());
console.log("9 =============loadavg()===================");
console.log(os.loadavg());
console.log("10 ================hostname()================");
console.log(os.hostname());
console.log("11 ==============homedir()==================");
console.log(os.homedir());
console.log("12 ===============getPriority()=================");
console.log(os.getPriority());
console.log("13 ==============freemem()==================");
console.log(os.freemem());
console.log("14 ==============endianness()==================");
console.log(os.endianness());
console.log("15 =============cpus()===================");
console.log(os.cpus());
console.log("16 ================arch()================");
console.log(os.arch());


console.log(Module);



















