import os, requests
P = '\x1b[1;97m'
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print('%s\nBAD INTERNET CONNECTION\n'%(P))
	exit()

if __name__ == "__main__":
	os.system("git pull")
	if "Indonesia" == fc:
		__import__("brute").main()
	else:
		__import__("brute").main()
