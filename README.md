# BefungeIntepreter by Ben Myers

### About Befunge

[Befunge](http://esolangs.org/wiki/Befunge) is a stack-based esoteric programming language created by Chris Pressey in 1993 with the express goal of being as difficult to compile as possible. It attempts this by a) being multidimensional with its grid-based structure and b) by allowing for self-modifying code.

##### Befunge-93 Specifications:

| Instruction       | Function |
| ------------- |----------|
| `0`-`9`      | Push this number on the stack|
| `+` | Addition: Pop _a_ and _b_, then push _a+b_ |
| `-` | Subtraction: Pop _a_ and _b_, then push _b-a_ |
| `*` | Multiplication: Pop _a_ and _b_, then push _a*b_ |
| `/` | Integer division: Pop _a_ and _b_, then push _b/a_, rounded towards 0 |
| `%` | Modulo: Pop _a_ and _b_, then push _b%a_ |
| `!` | Logical NOT: Pop a value, then push 1 if the value is a zero and 0 otherwise |
| <code>`</code> | Greater than: Pop _a_ and _b_, then push 1 if _b>a_ and 0 otherwise |
| `>` | Start moving right |
| `<` | Start moving left |
| `^` | Start moving up |
| `v` | Start moving down |
| `?` | Start moving in a random cardinal direction |
| `_` | Pop a value, and move right if it's zero, and left otherwise |
| <code>&#124;</code> | Pop a value, and move down if it's zero, and up otherwise |
| `"` | Start string mode: push each character's ASCII value all the way up until the next `"` |
| `:` | Duplicate the value on top of the stack |
| `\` | Swap two values on top of the stack |
| `$` | Pop value from the top of the stack and discard it |
| `.` | Pop value and output as an integer followed by a space |
| `,` | Pop value and output as ASCII character |
| `#` | Bridge: Skip next cell |
| `p` | A "put" call: Pop _y_, _x_, and _v_, then change the character at _(x,y)_ to _v_ |
| `g` | A "get" call: Pop _y_ and _x_, then push ASCII value of the character at that position in the program |
| `&` | Ask user for a number and push it |
| `~` | Ask user for a character and push its ASCII value |
| `@` | End the program |
| ` ` | No-op |

##### A _"Hello World!"_ Program in Befunge-93:

```befunge
>              v
v  ,,,,,"Hello"<
>48*,          v
v,,,,,,"World!"<
>25*,@
```

##### TODO:

- Implement Funge-98 specifications

    - Dynamic grid sizing

    - The `[` ("turn left") and `]` ("turn right") instructions

    - User should be able to specify Befunge-93 or Funge-98

- Implement GUI
