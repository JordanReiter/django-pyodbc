
def _parse_version(text):
    version_code = int(text.split('.')[0])
    if version_code >= 10:
        return 2008
    elif version_code == 9:
        return 2005
    else:
        return 2000

def get_version(cursor):
    cursor.execute("SELECT CAST(SERVERPROPERTY('ProductVersion') as varchar)")
    return _parse_version(cur.fetchone()[0])
