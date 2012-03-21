D [0-9]
L [A-Za-z]
W [ \n\r\t]
%%
a{L}*   {if ( strlen(yytext)>5 ) return 1;}
{W}*    { /* nothing */}
{L}*    { /* nothing */}

%%
