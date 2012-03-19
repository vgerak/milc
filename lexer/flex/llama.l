D [0-9]
L [A-Za-z]
W [ \n\r\t]
%%

/* keywords */
"and"               { return t_And; }
"array"             { return t_Array; }
"begin"             { return t_Begin; }
"bool"              { return t_Bool; }
"char"              { return t_Char; }
"delete"            { return t_Delete; }
"dim"               { return t_Dim; }
"do"                { return t_Do; }
"done"              { return t_Done; }
"downto"            { return t_Downto; }
"else"              { return t_Else; }
"end"               { return t_End; }
"false"             { return t_False; }
"float"             { return t_Float; }
"for"               { return t_For; }
"if"                { return t_If; }
"in"                { return t_In; }
"int"               { return t_Int; }
"let"               { return t_Let; }
"match"             { return t_Match; }
"mod"               { return t_Mod; }
"mutable"           { return t_Mutable
"new"               { return t_New; }
"not"               { return t_Not; }
"of"                { return t_Of; }
"rec"               { return t_Rec; }
"ref"               { return t_Ref; }
"then"              { return t_Then; }
"to"                { return t_To; }
"true"              { return t_True; }
"type"              { return t_Type; }
"unit"              { return t_Unit; }
"while"             { return t_While; }
"with"              { return t_With; }  

/* operators */
[=\+\-\*\/\|\;!<>\[\](),:]  { return yytext[0];}
"−>"                { return t_Func; }
"+."                { return t_RealPlus; }
"−."                { return t_RealMinus; }
"*."                { return t_RealMul; }
"/."                { return t_RealDiv; }
"**"                { return t_Pow; }
"&&"                { return t_AND; }
"||"                { return t_OR; }
"<>"                { return t_DomEQ; }
"<="                { return t_LEQ; }
">="                { return t_GEQ; }
"=="                { return t_EQ; }
"!="                { return t_NOT; }
":="                { return t_ASSIGN; }

%%

