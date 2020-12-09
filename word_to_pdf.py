from docx2pdf import convert

def main():
  convert("./alex_converter/files_to_convert", "./alex_converter/converted_files")

if __name__ == "__main__":
  main()