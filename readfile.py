
fh = open("test.toml","w")
lines_of_text = ["One line of text here\n", "and another line here", "and yet another here", "and so on and so forth"] 
fh.writelines(lines_of_text) 
fh.close() 
