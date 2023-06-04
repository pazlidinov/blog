def check_read_articles(request):
    try:
        read_articles = request.session["read_articles"]
    except:
        request.session["read_articles"] = []
        read_articles = request.session.get("read_articles")
    return read_articles


def check_article_view(request, pk):
    request.session.modified = True
    a_list = check_read_articles(request)
    if pk in a_list:
        print("article read..")
        return False
    else:
        a_list.append(pk)
        print("article views updated")
        return True


def check_like_articles(request):
    try:
        read_articles = request.session["like_articles"]
    except:
        request.session["like_articles"] = []
        read_articles = request.session.get("like_articles")
    return read_articles


def check_like_view(request, n):
    request.session.modified = True
    a_list = check_like_articles(request)
    if n in a_list:
        print("article liked..")
        return False
    else:
        a_list.append(n)
        print("article like updated")
        return True


def check_like_detail(request, n):
    request.session.modified = True
    a_list = check_like_articles(request)
    if n in a_list:
        print("article liked..")
        return True
    else:
        return False