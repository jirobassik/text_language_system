from langid import classify


def langid_method(text):
    return classify(text)[0]
