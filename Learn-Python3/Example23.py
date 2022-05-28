import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        # print_line(line, encoding, errors)
        decode_print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<==>", cooked_string)


def decode_print_line(line, encoding, errors):
    # Since the file is escaped, decode it twice.
    next_lang = line.strip()
    escaped_line = next_lang.encode(encoding, errors=errors)
    medium_string = escaped_line.decode(encoding, errors=errors)
    # well_string = str(medium_string).decode(encoding, errors=errors)
    print(f"{escaped_line} <==> {medium_string}")
    # print(f"{medium_string} <==> {well_string}")


# languages = open("./languages.txt", encoding="utf-8")
languages = open("./languages_raw.txt")
main(languages, input_encoding, error)
