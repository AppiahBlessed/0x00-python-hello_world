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







