import datetime as dt
import readline  # noqa: F401  # pyright: ignore[reportUnusedImport]


def identifier():
    curr_time = dt.datetime.now(dt.timezone.utc)
    id_str = curr_time.strftime("%Y%m%dT%H%M%S")
    formatter_time = curr_time.strftime("[%Y-%m-%d %a %H:%M]")
    return id_str, formatter_time


def get_title():
    title_string = input("Enter Title > ")
    title_lower = title_string.lower()
    title_final = "-".join(title_lower.split())
    return title_final, title_string


def get_keyword():
    keyword_string = input("Enter Keyword > ")
    keyword_lower = keyword_string.lower()
    words = keyword_lower.split()
    keyword_formatted = "_".join(keyword_lower.split())
    keyword_final = keyword_formatted

    # Example: ['key1', 'key2'] becomes ":key1:key2:"
    if words:
        keyword_org = ":" + ":".join(words) + ":"
    else:
        keyword_org = ""
    return keyword_final, keyword_org


def file_name(id_val: str, title_val: str, keyword_val: str, file_extension: str):
    file_name_str = f"{id_val}--{title_val}__{keyword_val}"
    file_ex = f"{file_name_str}.{file_extension}"
    return file_ex


def front_matter(fornt_id: str, fornt_date: str, fornt_title: str, fornt_keyword: str):
    front_matter_template = f"""#+TITLE:      {fornt_title}
#+DATE:       {fornt_date}
#+FILETAGS:   {fornt_keyword}
#+IDENTIFIER: {fornt_id}\n
    """
    return front_matter_template


def new_note(filename: str, content: str):
    # Open file with "w" to write content
    with open(filename, "w", encoding="utf-8") as note:
        _ = note.write(content)  #  writes the file here


def main():
    id_str, formatter_time = identifier()
    title_val, title_string = get_title()
    keyword_val, keyword_string = get_keyword()

    filename = file_name(id_str, title_val, keyword_val, file_extension="org")
    content = front_matter(id_str, formatter_time, title_string, keyword_string)

    new_note(filename, content)
    print(f"created note: {filename}")


if __name__ == "__main__":
    main()

# TODO
# DONE make keyword enclosed with :: eg | :2:key2:
