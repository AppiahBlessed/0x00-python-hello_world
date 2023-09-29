Task zero 
====================================================================

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

The size must be displayed in bytes
You have to use curl

====================================================================
curl -sI "$1":

curl is a command-line tool for making HTTP requests.
-s stands for "silent" and is used to suppress progress and error messages, so we only get the output we need.
-I tells curl to send a HEAD request instead of the default GET request. A HEAD request fetches the response headers but not the actual body of the response. This is more efficient when you're only interested in the headers.
"$1" is a placeholder for the first command-line argument passed to the script, which is the URL you want to request.
grep -i 'content-length:':

grep is a command that searches for text patterns in the input it receives.
-i makes the search case-insensitive.
'content-length:' is the pattern we're searching for in the output of curl. Specifically, we're looking for the line that contains "Content-Length."
awk '{print $2}':

awk is a text processing tool that splits input lines into fields and performs actions on them.
{print $2} tells awk to print the second field of each line. In this case, it extracts the value of the "Content-Length" header.



Task 1
===========================================================================
1. cURL to the end
mandatory
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

Display only body of a 200 status code response
You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000
===========================================================================
A 302 status code in HTTP is a "Found" or "Temporary Redirect" response. It indicates that the requested resource has been temporarily moved to a different URL, and the client should continue to request the resource from that new URL in the future.

Here's a brief explanation:

When a server sends a 302 response, it typically includes a Location header in the response, specifying the new URL to which the client should redirect.

The client (usually a web browser or another HTTP client like curl) then automatically makes a new request to the URL provided in the Location header.

The new request is usually a GET request to the new URL, and the server at that new URL may respond with the actual content or another redirect.

302 redirects are often used for scenarios like:

Temporary maintenance or load balancing: When a web application or service is temporarily unavailable at a specific URL, it might redirect users to another server or location that can handle their requests while maintenance is ongoing.

URL normalization: Servers may use 302 redirects to enforce a canonical URL format, redirecting users to the preferred URL.

It's important to note that a 302 response is temporary, and clients should continue to use the original URL in future requests unless instructed otherwise by the server. If you want the client to permanently use the new URL, you should use a 301 status code ("Moved Permanently") instead.


Redirect Handling: Make sure that your code is configured to follow redirects. In some cases, tools like curl may not automatically follow redirects unless you explicitly enable this behavior. With curl, you can use the -L or --location option to tell it to follow redirects:




Task 2
============================================================================
2. cURL Method
mandatory
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000
============================================================================

To send a DELETE request to a server using curl in Bash, you can use the following command:

bash
Copy code
curl -X DELETE "$url"
Replace "$url" with the URL where you want to send the DELETE request.

Here's a breakdown of the command:

curl: Invokes the curl command for making HTTP requests.

-X DELETE: Specifies the HTTP method as DELETE. The -X option is used to set the HTTP request method to DELETE explicitly.

"$url": This is where you should provide the URL to which you want to send the DELETE request.

For example, if you want to send a DELETE request to "https://example.com/resource/123," you would use:

bash
Copy code
curl -X DELETE "https://example.com/resource/123"
This command will send a DELETE request to the specified URL, indicating that you want to delete the resource located at that URL.





Task 3
===========================================================================
3. cURL only methods
mandatory
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

==============================================================================
awk '{$1 = ""; sub(/^ /, ""); print $0}' filename

{$1 = ""}: This command sets the first field ($1) to an empty string.

sub(/^ /, ""): This command removes the leading space at the beginning of the line.

print $0: This command prints the modified line.

This way, it removes the first field and the leading space, producing the desired output without a space before the first word




Task 4
============================================================================
4. cURL headers
mandatory
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

A header variable X-School-User-Id must be sent with the value 98
You have to use curl
============================================================================
In the curl command, the -H option is used to specify custom HTTP headers to include in the request. In the script I provided earlier, -H is used to add the X-School-User-Id header with the value 98 to the GET request.

Here's a breakdown of how -H works:

-H "X-School-User-Id: 98": This option adds an HTTP header to the request. The header is specified as a string in the format "Header-Name: Header-Value". In this case, it sets the X-School-User-Id header to 98.
HTTP headers are used to convey additional information in an HTTP request or response. In this script, the X-School-User-Id header is added to the request to fulfill the requirement of sending the header variable with the value 98 along with the GET request. This allows you to include custom information that the server may expect or require in the request headers.


Task 5
=============================================================================
5. cURL POST parameters
mandatory
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

A variable email must be sent with the value test@gmail.com
A variable subject must be sent with the value I will always be here for PLD
You have to use curl

============================================================================

OST Request with Form Data:

In a POST request, you can pass name-value pairs as form data using the -d or --data option in curl. The data is typically sent in the request body, and you specify the data in the format name=value.
Example: curl -d "param1=value1&param2=value2" -X POST "https://example.com/api"
