import pikepdf

file = pikepdf.open("mpass.pdf", "password of file")

new_file = file.save("pass.pdf")
