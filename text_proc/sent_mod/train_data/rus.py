sentences_pos = [
    ("Сегодня прекрасная погода, идеальная для прогулки в парке.", "pos"),
    ("Я очень рад получить такое замечательное предложение.", "pos"),
    ("Вчера я завершил свой проект успешно и получил похвалу от начальника.", "pos"),
    ("Моя семья всегда поддерживает меня во всем, и я очень благодарен им за это.", "pos"),
    (
        "Мой лучший друг согласился провести выходные со мной, и мы планируем отлично провести время.",
        "pos",
    ),
    (
        "Я сегодня получил отличные оценки на экзамене, на который так много готовился.",
        "pos",
    ),
    (
        "В моей жизни произошли замечательные изменения, и я чувствую себя счастливым и удовлетворенным.",
        "pos",
    ),
    ("Моя маленькая сестра научилась читать, и я горжусь ее достижением.", "pos"),
    ("Вчера я встретил старого друга, и мы провели вечер в приятной беседе и веселье.", "pos"),
    (
        "В моей команде работают талантливые и дружелюбные люди, и каждый день я рад работать с ними.",
        "pos",
    ),
]

sentences_neg = [
    ("Сегодня погода плохая, идет дождь.", "neg"),
    ("Я очень расстроен отказом в получении работы.", "neg"),
    ("Вчера я потерпел неудачу и не смог достичь своей цели.", "neg"),
    ("Моя семья постоянно критикует меня, и я чувствую себя несчастным(ой).", "neg"),
    ("Мой лучший друг отменил наши планы на выходные, и я разочарован.", "neg"),
    ("Я не смог сдать экзамен, хотя много готовился.", "neg"),
    (
        "В моей жизни произошли неприятные события, и я чувствую себя угнетенным и несчастным.",
        "neg",
    ),
    ("Моя маленькая сестра постоянно мне мешает, и я раздражен ее поведением.", "neg"),
    (
        "Вчера я случайно потерял ценную вещь, и теперь чувствую себя очень неудачливым.",
        "neg",
    ),
    (
        "В моей команде работают неотзывчивые и негативные люди, и каждый день я разочаровываюсь в них.",
        "neg",
    ),
]

sentences_rus = sentences_pos + sentences_neg