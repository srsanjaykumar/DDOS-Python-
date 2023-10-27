const fs = require('fs')
const a = require('http')
fs.writeFileSync("hello.c","#include <stdio.h> \n \
int main() \n \
{ \n\
    printf(\"Hello world \");\n \
} \n\
")





