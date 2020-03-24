import re

token_regexes = {
    "PUNCTUATOR": r"[\`\!\$\(\)(\.\.\.)\:\=\@\[\]\{\|\}\`]",
    "NAME": r"[_A-Za-z][_0-9A-Za-z]+",
    "INT": r"\d+",
    "FLOAT": r"\d+\.?\d+",
    "STRING": r"\"[_A-Za-z][_0-9A-Za-z]*\"",

    "WHITE_SPACE": r"\s+",
    "LINE_TERMINATOR": r"[\n|\r]",
    "COMMENT": r"#(.+?)[\n|\r]",
    "COMMA": r",",
}


def parse_document_string(string):
    tokens = []
    while string:
        print(string)
        for (key, value) in token_regexes.items():
            match = re.match(value, string)
            if match:
                print("Match")
                string = string[len(match[0]):]
                tokens.append({"text": match[0], "type": key})
                break
        else:
            print("No match")
            break
    print(tokens)


class Token:
    pass


test = "{ item1(df:as) { dsd }}"
parse_document_string(test)