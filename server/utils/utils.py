def clean_and_process_string(res: str) -> str:
    cleaned_res = "".join(c if c.isalpha() or c.isspace() else "" for c in res).strip()

    final_res = cleaned_res.replace("\n", " ").replace('"', "'").replace(",", "")

    return final_res
