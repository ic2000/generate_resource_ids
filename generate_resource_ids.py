import argparse
import sys
import os

def get_ids(rc_file_path):
  with open(rc_file_path, 'r') as rc_file:
    rc_file_contents = rc_file.read()
    ids = []
    
    for i in range(len(rc_file_contents)):
      if rc_file_contents.startswith("ID", i):
        if rc_file_contents[i + 2] == "_" or rc_file_contents[i + 3] == "_":
          id_end = 0
          
          for j in range(i + 3, len(rc_file_contents)):
              id_end = j
              
              if rc_file_contents[j].isspace() or rc_file_contents[j] == ",":
                break

          _id = rc_file_contents[i:id_end]

          if _id not in ids:
            ids.append(_id)
                        
    return ids

def main(input_file_path, output_file_path):
  ids = get_ids(input_file_path)
  header_file_name = os.path.splitext(os.path.basename(output_file_path))[0].upper()
  output_file_contents = ["#ifndef {0}_H\n#define {0}_H\n".format(header_file_name)]

  for i, v in enumerate(ids):
    output_file_contents.append("#define {} {}".format(v, i))

  output_file_contents.append("\n#endif // {}_H\n".format(header_file_name))

  with open(output_file_path, "w") as output_file:
    output_file.write("\n".join(output_file_contents))

  return 0

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Generate a header file containing macro definitions for the IDs of a resource file.")
  parser.add_argument("inputfile", help="the path of the resource file")
  parser.add_argument("outputfile", help="the path where the header file will be generated")
  args = parser.parse_args()
  sys.exit(main(args.inputfile, args.outputfile))
