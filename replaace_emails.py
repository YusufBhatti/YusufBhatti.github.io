def replace_email(commit):
    if b"hatti" in commit.author_email.lower():
        commit.author_email = b"yusuf.bhatti@hotmail.com"
        commit.author_name = b"Yusuf Bhatti"
    if b"hatti" in commit.committer_email.lower():
        commit.committer_email = b"yusuf.bhatti@hotmail.com"
        commit.committer_name = b"Yusuf Bhatti"

