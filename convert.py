from tabula import read_pdf, convert_into

#can convet into csv , json
filename = "name of file"
d = convert_into(filename, "test.csv", output_format="csv" , pages="all")
