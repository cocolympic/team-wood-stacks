mydict = {
	111: 104, # o -> h
	114: 111, # r -> o
	105: 110, # i -> n
}

txt = "hey, pytori" # hey, python

print(txt.translate(mydict))