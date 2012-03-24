%{}
unsigned int c_opened = 0;
int lines = 1;
enum {
t_And = 128,
t_Array,
t_Begin,
t_Bool,
t_Char,
t_Delete,
t_Dim,
t_Do,
t_Done,
t_Downto,
t_Else,
t_End,
t_False,
t_Float,
t_For,
t_If,
t_In,
t_Int,
t_Let,
t_Match,
t_Mod,
t_Mutable,
t_New,
t_Not,
t_Of,
t_Rec,
t_Ref,
t_Then,
t_To,
t_True,
t_Type,
t_Unit,
t_While,
t_With,
t_Func,
t_RealPlus,
t_RealMinus,
t_RealMul,
t_RealDiv,
t_Pow,
t_AND,
t_OR,
t_DomEQ,
t_LEQ,
t_GEQ,
t_EQ,
t_NOT,
t_ASSIGN,
t_Constructor,
t_Const_str,
t_Const_int,
t_Const_float,
t_Const_char,
t_Identifier };
%}


%x COMMENT

D [0-9]
L [A-Za-z]
DLU [a-zA-Z0-9_]
BL [A-Z]
SL [a-z]
W [ \t]
NL [\n\r]
CL --
%%

"and"                           { return t_And; }
"array"                         { return t_Array; }
"begin"                         { return t_Begin; }
"bool"                          { return t_Bool; }
"char"                          { return t_Char; }
"delete"                        { return t_Delete; }
"dim"                           { return t_Dim; }
"do"                            { return t_Do; }
"done"                          { return t_Done; }
"downto"                        { return t_Downto; }
"else"                          { return t_Else; }
"end"                           { return t_End; }
"false"                         { return t_False; }
"float"                         { return t_Float; }
"for"                           { return t_For; }
"if"                            { return t_If; }
"in"                            { return t_In; }
"int"                           { return t_Int; }
"let"                           { return t_Let; }
"match"                         { return t_Match; }
"mod"                           { return t_Mod; }
"mutable"                       { return t_Mutable; }
"new"                           { return t_New; }
"not"                           { return t_Not; }
"of"                            { return t_Of; }
"rec"                           { return t_Rec; }
"ref"                           { return t_Ref; }
"then"                          { return t_Then; }
"to"                            { return t_To; }
"true"                          { return t_True; }
"type"                          { return t_Type; }
"unit"                          { return t_Unit; }
"while"                         { return t_While; }
"with"                          { return t_With; }

[=\+\-\*\/\|\;!<>\[\]\\,:()]    { return yytext[0]; }
"−>"                            { return t_Func; }
"+."                            { return t_RealPlus; }
"−."                            { return t_RealMinus; }
"*."                            { return t_RealMul; }
"/."                            { return t_RealDiv; }
"**"                            { return t_Pow; }
"&&"                            { return t_AND; }
"||"                            { return t_OR; }
"<>"                            { return t_DomEQ; }
"<="                            { return t_LEQ; }
">="                            { return t_GEQ; }
"=="                            { return t_EQ; }
"!="                            { return t_NOT; }
":="                            { return t_ASSIGN; }

<*>{NL}                         { ++lines; }
{W}*                            { /* nothing */ }
{W}*--.*                        { ++lines; }
<COMMENT>[^"(*""*)"{NL}]        { /* nothing */ }
<*>"(*"                         { if( c_opened++ == 0) BEGIN(COMMENT); }
<COMMENT>"*)"                   { if( --c_opened == 0) BEGIN(INITIAL); }
<<EOF>>                         { return 0; }
\".*\"                          { return t_Const_str; }
{SL}{DLU}*                  { return t_Identifier; }
{BL}{DLU}*                  { return t_Constructor; }
{D}*                            { return t_Const_int; }
\'\\?.*\'                          { return t_Const_char; }
.                               { return -1; }

%%
