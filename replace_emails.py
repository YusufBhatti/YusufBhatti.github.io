def commit_callback(commit):
    old_emails = [b"ybhatti@int4.local.snellius.surf.nl", b"ybhatti@int5.local.snellius.surf.nl", b"ybhatti@int6.local.snellius.surf.nl"]
    for old_email in old_emails:
        if commit.author_email == old_email:
            commit.author_email = b"yusuf.bhatti@hotmail.com"
            commit.author_name = b"Yusuf Bhatti"
        if commit.committer_email == old_email:
            commit.committer_email = b"yusuf.bhatti@hotmail.com"
            commit.committer_name = b"Yusuf Bhatti"

