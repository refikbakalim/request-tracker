import base64
import io

folder= r"Write folder path containing base64 named files here"

ascii_string = ""
for i in range(0,494):
    with open(folder + "\\" + (base64.b64encode(bytes(str(i), 'ascii'))).decode("utf-8") ) as text_file:
        contents = text_file.read()
        binary_values = contents.split()
        for binary_value in binary_values:
            an_integer = int(binary_value, 2)
            ascii_character = chr(an_integer)
            ascii_string += ascii_character

#uncomment below lines if you want to output as txt file

#with io.open("Output.txt", "w", encoding="utf-8") as f:  
#    f.write(ascii_string)

print(ascii_string)