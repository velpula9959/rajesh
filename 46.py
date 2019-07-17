r=input("")
r=r.casefold()
rev=reversed(r)
if list(r) == list(rev):
	print("yes")
else:
	print("no")
