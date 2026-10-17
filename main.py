from os import system, popen

def file_name(link):
    file = popen(f"basename {link}")
    return file.read().strip()

def download_file(link, filename):
    try:
        system(f"curl {link} -o {filename}")
    except:
        print("An Error Occurred")
        exit(1)

def remove_bg(filename, output):
    try:
        system(f"backgroundremover -i {filename} -o {output}")
    except:
        print("Error! Please Retry")
        exit(1)

def main():
	link = input("Input image link: ")
	input_filename = file_name(link)
	
	output_filename = input("Output file name: ")
	download_file(link, input_filename)
	remove_bg(input_filename, output_filename)
	
main()
