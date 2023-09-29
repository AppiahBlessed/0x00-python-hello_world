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








