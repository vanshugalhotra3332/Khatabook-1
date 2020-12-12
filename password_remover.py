import subprocess
try:
  import pikepdf
except ModuleNotFoundError:
  data_ = subprocess.call(['pip', 'install', 'pikepdf'])     # this will install the module by themselves
  import pikepdf

file = pikepdf.open("mpass.pdf", "password of file")

new_file = file.save("pass.pdf")
