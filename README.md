# Server-side-templet-injection-

Above Vulnerable source code will help you to understand SSTI attack. 



Summary
Web applications commonly use server side templating technologies (Jinja2, Twig, FreeMaker, etc.) to generate dynamic HTML responses. Server Side Template Injection vulnerabilities (SSTI) occur when user input is embedded in a template in an unsafe manner and results in remote code execution on the server. Any features that support advanced user-supplied markup may be vulnerable to SSTI including wiki-pages, reviews, marketing applications, CMS systems etc. Some template engines employ various mechanisms (eg. sandbox, whitelisting, etc.) to protect against SSTI.


Detection : 
After detecting template injection, the next step is to identify the template engine in use. This step is sometimes as trivial as submitting invalid syntax, as template engines may identify themselves in the resulting error messages. However, this technique fails when error messages are supressed, and isn't well suited for automation. We have instead automated this in Burp Suite using a decision tree of language-specific payloads. Green and red arrows represent 'success' and 'failure' responses respectively. In some cases, a single payload can have multiple distinct success responses - for example, the probe {{7*'7'}} would result in 49 in Twig, 7777777 in Jinja2, and neither if no template language is in use.

How to install.
1. Download Flask_Code.py on local server. 
2. Run Command python flask.py 
3. Access application http://localhost:1337/?name="injection"

Referance : 
https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/18-Testing_for_Server_Side_Template_Injection
https://portswigger.net/kb/papers/serversidetemplateinjection.pdf
https://portswigger.net/research/server-side-template-injection

