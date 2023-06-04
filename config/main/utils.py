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
